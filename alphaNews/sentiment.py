# main
import json

from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
import re


def sentiment(companiesData, subscription_key):
    """Sentiment.
    Scores close to 1 indicate positive sentiment, while scores close to 0 indicate negative sentiment.
    """
    global response
    endpoint = "https://canadacentral.api.cognitive.microsoft.com"
    client = TextAnalyticsClient(endpoint=endpoint, credentials=CognitiveServicesCredentials(subscription_key))

    texts = [text for group in
             [[article['text'] for article in company['articles']] for company in companiesData['companies']] for
             text in group]
    texts = set(texts)
    for text in texts:
        average = 0
        toAnalyze = []
        for sentence in text.split('.'):
            if 10 < len(sentence) < 5000:
                sentence = re.sub(' +', ' ', sentence)
                toAnalyze.append({
                    'text': sentence,
                    'id': hash(sentence),
                    'language': 'en'
                })
        try:
            response = client.sentiment(documents=toAnalyze)
            for result in response.documents:
                score = result.score
                if score > .65 or score < .35:
                    average += score
            average = average / len(text.split('.'))
            for company in companiesData['companies']:
                for article in company['articles']:
                    if str(hash(article['text'])) == str(hash(text)):
                        article['sentiment'] = average
        except Exception as err:
            print(err)
    return companiesData
