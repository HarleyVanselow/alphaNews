from alphaNews.stock import getSymbol

assert getSymbol("Microsoft") == "MSFT"
assert getSymbol("Wack Not a Company") is None
