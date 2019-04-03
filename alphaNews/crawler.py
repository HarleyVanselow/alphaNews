def getCompaniesData(key, topic):
    result = {'topic': topic,
              'companies': [
                  {'name': 'Samsung',
                   'articles': [{'date': 123874872, 'text': "Some text is good!"},
                                {'date': 1235232, 'text': "Some text is bad!"}
                                ]
                   },
                  {
                      'name': 'Huawai',
                      'articles': [{'date': 23418142, 'text': "Evil corp"}]
                  }
              ]}
    return result
