import json

from alphaNews.crawler import getCompaniesData
from alphaNews.sentiment import sentiment
from alphaNews.stock import getStockDeltas


def searchTopic(topic):
    load = json.load(open("../../key.json", 'r'))
    sentiment_api_key = load["sentimentApiKey"]
    search_api_key = load["searchApiKey"]
    stock_api_key = load["stockApiKey"]
    entity_api_key = load["entityApiKey"]

    company_results = getCompaniesData(search_api_key,entity_api_key, topic)
    with_sentiment = sentiment(company_results, entity_api_key)
    print(with_sentiment)
    with_stocks = getStockDeltas(with_sentiment, stock_api_key)

    return with_stocks
