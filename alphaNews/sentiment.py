# main
import json

from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials


def sentiment(companiesData, subscription_key):
    """Sentiment.
    Scores close to 1 indicate positive sentiment, while scores close to 0 indicate negative sentiment.
    """
    endpoint = "https://australiaeast.api.cognitive.microsoft.com"
    client = TextAnalyticsClient(endpoint=endpoint, credentials=CognitiveServicesCredentials(subscription_key))

    try:
        # documents = [company.articles for company in companiesData]
        documents = [{
            'language': 'en',
            'id': 0,
            'text': "I had the best day of my life."
        }]

        for document in documents:
            print("Asking sentiment on '{}' (id: {})".format(document['text'], document['id']))

        response = client.sentiment(
            documents=documents
        )

        for document in response.documents:
            print("Found out that in document {}, sentiment score is {}:".format(document.id, document.score))

    except Exception as err:
        print("Encountered exception. {}".format(err))


