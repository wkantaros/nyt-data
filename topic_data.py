# script was primarily written by Miles McCain, it should be in a notebook but I'm lazy

import numpy as np
import pandas as pd
from datetime import datetime
import os
import csv
import pickle

# Category deduplication
REWRITE_CATEGORIES = {
    "Business Day": "Business",
    "nan": "Unknown",
    "New York and Region": "N.Y. / Region",
    "false": "Unknown",
    "Crosswords/Games":  "Crosswords & Games",
    "Multimedia/Photos": "Multimedia",
    "Home and Garden": "Home & Garden",
    "Autos": "Automobiles",
    "Great Homes and Destinations": "Great Homes, Destinations",
    "Style": "Fashion & Style",
    "Dining and Wine":	"Dining & Wine"
}

def _rewrite_category(category):
    """Standardize the category name by performing a
    rewrite if necessary.

    Arguments:
        category {string} -- the name of the category

    Returns:
        string -- the standardized category
    """

    if category in REWRITE_CATEGORIES:
        return REWRITE_CATEGORIES[category]
    return category

def _unpack_categories(reported_category):
    """Utility method to get all the subcategories,
    separated by a semicolon.

    Arguments:
        reported_category {string} -- semicolon-separated supercategory

    Returns:
        [String] -- array of subcategory strings
    """

    return [_rewrite_category(category.strip()) for category in reported_category.split(";")]

def _process_row(k):
    k['section_name'] = _unpack_categories(str(k['section_name']))
    k['pub_date'] = datetime.strptime(k['pub_date'], "%Y-%m-%d").date()
    return k

def load_all_data():
    """Load all the CSVs in /data into a single
    dataframe.

    Returns:
        dataframe -- all the data
    """

    dataframes = []
    for data_file in os.listdir("data/"):
        if '.csv' in data_file:
            data = pd.read_csv("data/" + data_file)
            dataframes.append(data)
    dataframe = pd.concat(dataframes)
    dataframe.apply(lambda k: _process_row(k), axis=1)
    return dataframe

def get_percent_by_women(dataframe, fil):
    total = 0
    matched = 0
    for index, row in dataframe.iterrows():
        if fil(row):
            total += 1
            if row["gender"] == "F":
                matched += 1
    if total == 0:
        return None
    return float(matched) / total

def get_total_num_women(dataframe, fil):
    """Counts total women in category

    Returns:
        [list] -- total number of women, total number in category
    """
    total = 0
    matched = 0
    for index, row in dataframe.iterrows():
        if fil(row):
            total += 1
            if row["gender"] == "F":
                matched += 1
    return matched


def _get_unique_categories(dataframe):
    """Utility method to get the unique categories in the dataframe, unpacked
    and standardized.

    Arguments:
        dataframe {dataframe} -- the dataframe which contains the NYT data

    Returns:
        [String] -- array of the unique categories
    """

    categories = set()
    for reported_category in dataframe.section_name.unique():
        for found_category in _unpack_categories(str(reported_category)):
            categories.add(found_category)
    return categories

def load_monthly_stats(data_dict):
    with open('monthly_stats.pickle', 'wb') as handle:
        pickle.dump(data_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

if __name__ == "__main__":
    data = load_all_data()
    # this will also dedup categories

    # Example: how to get example articles for any given month
    # get_percent_by_women(data, lambda k: k['pub_date'].month == 6 and k['pub_date'].year == 2013 and 'Sports' in k['section_name'])


    # Get all the unique categories
    all_unique_categories = set()
    for categories in data['section_name']:
        for subcategory in categories:
            all_unique_categories.add(subcategory)

    monthly_stats = {}
    for year in range(2011, 2017):
        monthly_stats[str(year)] = {}
        for month in range(1, 13):
            monthly_stats[str(year)][str(month)] = {}
            for category in all_unique_categories:
                monthly_stats[str(year)][str(month)][category] = {
                    "total": 0, # total number of articles
                    "women": 0  # number of those articles by women
                }

    for index, row in data.iterrows():
        year = str(row['pub_date'].year)
        month = str(row['pub_date'].month)
        for category in row['section_name']:
            monthly_stats[year][month][category]["total"] += 1
            if row["gender"] == "F":
                monthly_stats[year][month][category]["women"] += 1


    # with open('updated_stats823.csv', mode='w') as csv_file:
    #     nyt_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #     columns = ["Year", "Month"]
    #     columns.extend(all_unique_categories)
    #     nyt_writer.writerow(columns) # this is the line in question -- a bytes-like object is required, not 'str'
    #     for year in range(2011, 2017):
    #         for month in range(1, 13):
    #             row = [str(year), str(month)]
    #             for category in all_unique_categories:
    #                 women = float(monthly_stats[str(year)][str(month)][category]["women"])
    #                 total = float(monthly_stats[str(year)][str(month)][category]["total"])
    #                 if total == 0:
    #                     row.append(None)
    #                 else:
    #                     row.append(women/total*100.0)
    #             nyt_writer.writerow(row)
