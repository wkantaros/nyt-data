import requests
import csv

key = '75ecb8e663da46c2ad9759c147fe0812'

def getArticlesMonth(year, month):
    url = 'http://api.nytimes.com/svc/archive/v1/{}/{}.json?api-key={}'.format(str(year), str(month), key)
    json_data = requests.get(url).json()
    articles = json_data['response']['docs']
    return articles

def scrape(articles):
    filename = '{}.csv'.format(articles[0]['pub_date'][:7])

    with open('data/{}'.format(filename), mode='w') as csv_file:
        nyt_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        nyt_writer.writerow(['section_name', 'firstname', 'pub_date'])
        for article in articles:
            try:
                nyt_writer.writerow([
                    article['section_name'],
                    article['byline']['person'][0]['firstname'],
                    article['pub_date'][:10]])
            except:
                continue

def scrape2015on(year, month):
    if (year < 2015):
        return
    else:
        scrape(getArticlesMonth(year, month))
        if month == 1:
            scrape2015on(year - 1, 12)
        else:
            scrape2015on(year, month - 1)

scrape2015on(2016, 12)
