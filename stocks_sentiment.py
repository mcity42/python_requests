import requests
import pprint
import config as con

wallst_curl = 'https://tradestie.com/api/v1/apps/reddit'

# dictionary of the json response
resp = requests.get(wallst_curl).json()

# display the sentiment for 50 prominent tickers
for ticker in resp:
    pprint.pprint(ticker['ticker'] + ":" + ticker['sentiment'])


print("------------------------------------------")

yahoo_curl = 'https://yfapi.net/v6/finance/quote'


queryInput = input(
    "Enter 1 or more stock symbols separated by a comma,\n20 max.")

query_string = {"symbols": f"{queryInput}"}

querytest = {'symbols': 'AAPL'}

# responder builds request with user input as query params
# it takes an api key registered for yahoo finance api and saved
# in the config.py file
responder = requests.request(
    "Get", yahoo_curl, headers=con.headers, params=query_string).json()

# pretty print
pprint.pprint(responder)
