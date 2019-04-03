import json
import os
import sys

from alphaNews.crawler import getText
from alphaNews.sentiment import sentiment


def main(companyname):
    load = json.load(open("../key.json", 'r'))
    key = load["apiKey"]
    texts = getText(key, companyname)
    sentiment(texts, key)


if __name__ == "__main__":
    main(sys.argv[0])
