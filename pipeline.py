#!/usr/bin/env python

import sys
import os
from pprint import pprint
from alphaNews.crawler import *

search_key = os.environ['AZURE_SEARCH_KEY']
analytics_key = os.environ['AZURE_ANALYTICS_KEY']


def main():
    try:
        result = getCompaniesData(search_key, analytics_key, 'medical robotics')

        pprint(result)


    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main()
