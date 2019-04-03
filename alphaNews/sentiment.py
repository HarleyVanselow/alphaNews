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
        texts = [text for group in
                 [[article['text'] for article in company['articles']] for company in companiesData['companies']] for
                 text in group]
        documents = []
        for text in texts:
            documents.append({
                'text': text,
                'id': hash(text),
                'language': 'en'
            })
        for document in documents:
            print("Asking sentiment on '{}' (id: {})".format(document['text'], document['id']))

        response = client.sentiment(
            documents=documents
        )

        for document in response.documents:
            print("Found out that in document {}, sentiment score is {}:".format(document.id, document.score))
            for company in companiesData['companies']:
                for article in company['articles']:
                    if str(hash(article['text'])) == document.id:
                        print("Updating article details")
                        article['sentiment'] = document.score
        return companiesData
    except Exception as err:
        print("Encountered exception. {}".format(err))
