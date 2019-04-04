from datetime import datetime

import requests


def getStockDeltas(companyResults):
    for company in companyResults['companies']:
        results = getCompanyStockData(company['name'])
        if len(results) == 0: return companyResults
        # Consider 1 week
        for article in company['articles']:
            start = article['date']
            end = start + 604800
            startDate = datetime.utcfromtimestamp(start).strftime('%Y-%m-%d')
            endDate = datetime.utcfromtimestamp(end).strftime('%Y-%m-%d')
            while startDate not in results:
                start -= 86400
                startDate = datetime.utcfromtimestamp(start).strftime('%Y-%m-%d')
            while endDate not in results:
                end += 86400
                endDate = datetime.utcfromtimestamp(end).strftime('%Y-%m-%d')
            article['open'] = results[startDate]["1. open"]
            article['close'] = results[endDate]["4. close"]
    return companyResults


def getCompanyStockData(company):
    symbol = getSymbol(company)
    if symbol is None: return []
    print("Getting stock data for " + symbol)
    r = requests.get(
        "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + symbol + "&outputsize=full&apikey=5UY2LSENTP9DQQP8")
    results = r.json()["Time Series (Daily)"]
    return results


def getSymbol(company):
    print("Getting symbol for " + company)
    r = requests.get(
        "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=" + company + "&apikey=5UY2LSENTP9DQQP8")
    matches = r.json()["bestMatches"]
    if len(matches) == 0: return None
    symbol = matches[0]["1. symbol"]
    return symbol
