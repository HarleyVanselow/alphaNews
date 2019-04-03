def getText(key, topic):
    result = {}
    result.topic = topic
    result.companies = [
        {'name': 'Samsung',
         'articles': [{'date': 123874872, 'text': "Some text is good!"},
                      {'date': 1235232, 'text': "Some text is bad!"}
                      ]
         }
    ]
    return result
