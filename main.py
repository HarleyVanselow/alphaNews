import json
import sys

#
from alphaNews.crawler import getCompaniesData
from alphaNews.sentiment import sentiment
from alphaNews.stock import getStockDeltas


# def getCorrelation(companyResults):
#     for company in companyResults['companies']:

def searchTopic(topic):
    load = json.load(open("../../key.json", 'r'))
    sentiment_api_key = load["sentimentApiKey"]
    search_api_key = load["searchApiKey"]
    stock_api_key = load["stockApiKey"]

    company_results = getCompaniesData(search_api_key, topic)
    with_sentiment = sentiment(company_results, sentiment_api_key)
    with_stocks = getStockDeltas(with_sentiment, stock_api_key)
    # with_correlation = getCorrelation(with_stocks)
    return with_stocks
