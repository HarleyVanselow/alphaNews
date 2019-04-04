import time
from datetime import datetime

import requests


def getStockDeltas(companyResults, key):
    for company in companyResults['companies']:
        results = getCompanyStockData(company['name'], key)
        if len(results) == 0: return companyResults
        # Consider 1 week
        for article in company['articles']:
            start = article['date']
            end = start + 604800
            startDate = datetime.utcfromtimestamp(start).strftime('%Y-%m-%d')
            endDate = datetime.utcfromtimestamp(end).strftime('%Y-%m-%d')
            print("Start date: {}".format(startDate))
            print("End date: {}".format(endDate))
            if int(time.time()) < end :
                continue
            while startDate not in results:
                start -= 86400
                startDate = datetime.utcfromtimestamp(start).strftime('%Y-%m-%d')
            while endDate not in results:
                end += 86400
                endDate = datetime.utcfromtimestamp(end).strftime('%Y-%m-%d')
            article['open'] = results[startDate]["1. open"]
            article['close'] = results[endDate]["4. close"]
    return companyResults


def getCompanyStockData(company, key):
    symbol = getSymbol(company, key)
    if symbol is None: return []
    print("Getting stock data for " + symbol)
    r = requests.get(
        "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + symbol + "&outputsize=full&apikey=" + key)
    results = r.json()["Time Series (Daily)"]
    return results


def getSymbol(company, key):
    print("Getting symbol for " + company)
    r = requests.get(
        "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=" + company + "&apikey=" + key)
    matches = r.json()["bestMatches"]
    if len(matches) == 0: return None
    symbol = matches[0]["1. symbol"]
    return symbol
