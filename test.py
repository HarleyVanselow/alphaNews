import json

from alphaNews.stock import getSymbol

load = json.load(open("key.json", 'r'))
sentiment_api_key = load["sentimentApiKey"]
search_api_key = load["searchApiKey"]
stock_api_key = load["stockApiKey"]

assert getSymbol("Microsoft", stock_api_key) == "MSFT"
assert getSymbol("Wack Not a Company", stock_api_key) is None
