from azure.cognitiveservices.search.newssearch import NewsSearchAPI
from msrest.authentication import CognitiveServicesCredentials
import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
import dateutil.parser as dp

def getCompaniesData(apiKey, searchPhrase):

    result = {'topic': searchPhrase,
              'companies': []}

    company = {'name': searchPhrase,
               'articles': []}

    result['companies'].append(company)

    for article in search(apiKey, searchPhrase):
        company['articles'].append(article)


    return result

    # result = {'topic': topic,
    #           'companies': [
    #               {'name': 'Samsung',
    #                'articles': [{'date': 1104537600, 'text': "Some text is good!"},
    #                             {'date': 1453420800, 'text': "Some text is bad!"}
    #                             ]
    #                },
    #               {
    #                   'name': 'Disney',
    #                   'articles': [{'date': 1453420800, 'text': "Evil corp"}]
    #               }
    #           ]}
    # return result



def search(apiKey, searchPhrase):
    client = NewsSearchAPI(CognitiveServicesCredentials(apiKey))
    news_result = client.news.search(query=searchPhrase, freshness='Week', market="en-us", count=15)

    if news_result.value:
        for article in news_result.value:

            parsed_t = dp.parse(article.date_published)

            yield {
                'url': article.url,
                'date_published': article.date_published,
                'date': int(parsed_t.timestamp()),
                'text': getText(article.url)
            }


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)


def getText(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        texts = soup.findAll(text=True)
        visible_texts = filter(tag_visible, texts)
        return u" ".join(t.strip() for t in visible_texts)

    except KeyboardInterrupt:
        return ''
