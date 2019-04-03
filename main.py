import json
import sys

#
from alphaNews.crawler import getCompaniesData
from alphaNews.sentiment import sentiment


def main(topic):
    load = json.load(open("key.json", 'r'))
    sentiment_api_key = load["sentitmentApiKey"]
    search_api_key = load["searchApiKey"]

    company_results = getCompaniesData(search_api_key, search_api_key)
    with_sentiment = sentiment(company_results, sentiment_api_key)
    print(with_sentiment)


if __name__ == "__main__":
    main(sys.argv[1])
