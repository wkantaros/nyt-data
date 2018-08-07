import requests
import csv
import genderPredictor

key = '75ecb8e663da46c2ad9759c147fe0812'

def getArticlesMonth(year, month):
    url = 'http://api.nytimes.com/svc/archive/v1/{}/{}.json?api-key={}'.format(str(year), str(month), key)
    json_data = requests.get(url).json()
    articles = json_data['response']['docs']
    return articles

def scrape(articles):
    ## I don't want this to go here, because then it has to remake the gp object each time
    ## which is very time consuming, but I don't really want to turn the scrape thing into
    ## an object, either, because then you'd run into scrape.scrape() scenarios which seem annoying

    gp = genderPredictor.genderPredictor()
    accuracy = gp.trainAndTest()

    filename = '{}.csv'.format(articles[0]['pub_date'][:7])

    with open('data/{}'.format(filename), mode='w') as csv_file:
        nyt_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        nyt_writer.writerow(['section_name', 'firstname', 'pub_date', 'gender'])
        for article in articles:
            try:
                nyt_writer.writerow([
                    article['section_name'],
                    article['byline']['person'][0]['firstname'],
                    article['pub_date'][:10],
                    gp.classify(article['byline']['person'][0]['firstname'])])
            except:
                continue

# will count backwards from year/month to startYear
def scrapeYears(year, month, startYear=2014):
    while(year > startYear):
        scrape(getArticlesMonth(year, month))
        if month == 1:
            year,month = year-1, 12
        else:
            month -= 1

if __name__ == "__main__":
    scrapeYears(2015, 12)
