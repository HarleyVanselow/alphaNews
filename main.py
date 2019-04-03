import json
import sys

#
from alphaNews.crawler import getCompaniesData
from alphaNews.sentiment import sentiment
from alphaNews.stock import getStockPrices

def main(companyname):
    load = json.load(open("key.json", 'r'))
    stock_api_key = load['stockApiKey']
    sentiment_api_key = load["sentimentApiKey"]
    search_api_key = load["searchApiKey"]

    company_results = getCompaniesData(search_api_key, search_api_key)
    with_sentiment = sentiment(company_results, sentiment_api_key)
    print(with_sentiment)
    price = getStockPrices('apple','2019-03-03',stock_api_key)

if __name__ == "__main__":
    main(sys.argv[1])
