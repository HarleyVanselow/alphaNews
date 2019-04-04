#!/usr/bin/env python

import sys
import os
from alphaNews.crawl import *

search_key = os.environ['AZURE_SEARCH_KEY']


def main():
    try:
        for article in search('medical robotics', search_key):
            text = getText(article['url'])
            print(text)

    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main()
