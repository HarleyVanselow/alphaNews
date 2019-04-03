# main
import json
import os

from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials

SUBSCRIPTION_KEY_ENV_NAME = "TEXTANALYTICS_SUBSCRIPTION_KEY"
TEXTANALYTICS_LOCATION = os.environ.get("TEXTANALYTICS_LOCATION", "westcentralus")


def sentiment(subscription_key):
    """Sentiment.
    Scores close to 1 indicate positive sentiment, while scores close to 0 indicate negative sentiment.
    """
    endpoint = "https://australiaeast.api.cognitive.microsoft.com"
    client = TextAnalyticsClient(endpoint=endpoint, credentials=CognitiveServicesCredentials(subscription_key))

    try:
        documents = [{
            'language': 'en',
            'id': 0,
            'text': "I had the best day of my life."
        }, {
            'language': 'en',
            'id': 1,
            'text': "This was a waste of my time. The speaker put me to sleep."
        }, {
            'language': 'es',
            'id': 2,
            'text': "No tengo dinero ni nada que dar..."
        }, {
            'language': 'it',
            'id': 3,
            'text': "L'hotel veneziano era meraviglioso. È un bellissimo pezzo di architettura."
        }]

        for document in documents:
            print("Asking sentiment on '{}' (id: {})".format(document['text'], document['id']))

        response = client.sentiment(
            documents=documents
        )

        for document in response.documents:
            print("Found out that in document {}, sentimet score is {}:".format(document.id, document.score))

    except Exception as err:
        print("Encountered exception. {}".format(err))


load = json.load(open("key.json", 'r'))
key = load["apiKey"]
print(key)
sentiment(key)