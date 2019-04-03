import json
import sys

#
from alphaNews.crawler import getCompaniesData
from alphaNews.sentiment import sentiment
from alphaNews.stock import getStockPrices

def main(companyname):
    load = json.load(open("key.json", 'r'))
    key = load["apiKey"]
    company_results = getCompaniesData(key, companyname)
    withSentiment = sentiment(company_results, key)
    print(withSentiment)
    price = getStockPrices(1,2)

if __name__ == "__main__":
    main(sys.argv[1])
