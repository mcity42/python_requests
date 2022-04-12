import requests
import pprint

curl = 'https://tradestie.com/api/v1/apps/reddit'

# dictionary of the json response
resp = requests.get(curl).json()


for ticker in resp:
    pprint.pprint(ticker['ticker'] + ":" + ticker['sentiment'])


# pprint.pprint(resp)
