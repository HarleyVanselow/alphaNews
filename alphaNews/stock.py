import requests
import json

def getStockPrices(companyName, requestDate,stockApiKey):
    file = "data.txt"
    file_object = open(file, "w")
    r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&outputsize=full&apikey=" + stockApiKey)
    if r.status_code == 200:
        file_object.write(r.content)
        print("done")
    else:
        print("Stock API call failed: code " + str(r.status_code))
    file_object.close()

