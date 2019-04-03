from azure.cognitiveservices.search.newssearch import NewsSearchAPI
from msrest.authentication import CognitiveServicesCredentials
# from boilerpipe.extract import Extractor

import requests
import urllib.request


def getCompaniesData(key, topic):
    result = {'topic': topic,
              'companies': [
                  {'name': 'Samsung',
                   'articles': [{'date': 1104537600, 'text': "Some text is good!"},
                                {'date': 1453420800, 'text': "Some text is bad!"}
                                ]
                   },
                  {
                      'name': 'Disney',
                      'articles': [{'date': 1453420800, 'text': "Evil corp"}]
                  }
              ]}
    return result


# def primarySearch(searchPhrase, key):
#     listOfUrls = queryBing(searchPhrase, key);
#
#     listOfDocumentText = []
#
#     for url in listOfUrls:
#         response = requests.get(url)
#         extractor = Extractor(extractor='ArticleExtractor', html=response.text)
#         listOfDocumentText.append(extractor.getText())
#
#     return listOfDocumentText
#
#
# def queryBing(searchPhrase, key):
#     client = NewsSearchAPI(CognitiveServicesCredentials(key))
#     news_data = client.news.search(query=searchPhrase, market="en-us", count=10)
#     list = []
#
#     if hasattr(news_data, 'value'):
#
#         print("\r\nWebpage Results#{}".format(len(news_data.value)))
#         for page in news_data.value:
#             list.append(page.url)
#
#     else:
#         print("Didn't find any web pages...")
#     return list
