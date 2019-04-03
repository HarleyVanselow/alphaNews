import json
import sys

#
from alphaNews.crawler import getCompaniesData
from alphaNews.sentiment import sentiment


def main(companyname):
    load = json.load(open("key.json", 'r'))
    sentimentApiKey = load["sentitmentApiKey"]
    searchApiKey = load["searchApiKey"]
    
    company_results = getCompaniesData(key, searchApiKey)
    sentiment(company_results, sentimentApiKey)


if __name__ == "__main__":
    main(sys.argv[0])
