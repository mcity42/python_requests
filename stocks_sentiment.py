import requests
import pprint
import config as con

#import pandas as pd

wallst_curl = 'https://tradestie.com/api/v1/apps/reddit'

# dictionary of the json response
resp = requests.get(wallst_curl).json()

ticker_list = []

# display the sentiment for 50 prominent tickers
i = 1
for ticker in resp:
    pprint.pprint(f"{i}. " + ticker['ticker'] + ": " + ticker['sentiment'])
    ticker_list += ticker['ticker'] + ": " + ticker['sentiment']
    i += 1

# pprint.pprint(pd.Series(ticker_list))

print("------------------------------------------")

yahoo_curl = 'https://yfapi.net/v6/finance/quote'


print("Choose ticker(s) above to analyze further")
queryInput = input(
    "Enter 1 or more tikers listed above separated by a comma,20 max: \n").upper()

# chart
chart_url = f'https://yfapi.net/v6/finance/chart?ticker={queryInput}'
chart_string = {"ticker": f"{queryInput}"}
chart = requests.request(
    "Get", chart_url, headers=con.headers, params=chart_string).json()


# place user input into query
query_string = {"symbols": f"{queryInput}"}


# insights
insights_url = f'https://yfapi.net/ws/insights/v1/finance/insights?symbol={queryInput}'

insight = requests.request(
    "Get", insights_url, headers=con.headers, params=query_string).json()
print("Isnights:")
pprint.pprint(insight)

# responder builds request with user input as query params
# it takes an api key registered for yahoo finance api and saved
# in the config.py file saved as
# headers = {'x-api-key':'YOUR-PERSONAL-API_KEY'}
responder = requests.request(
    "Get", yahoo_curl, headers=con.headers, params=query_string).json()


pprint.pprint(responder)
# pretty print
# pprint.pprint(responder['quoteResponse']['result'][0]['symbol'])
# pprint.pprint(responder['quoteResponse']['result'][0]['displayName'])
# pprint.pprint(responder['quoteResponse']['result'][0]['fiftyTwoWeekRange'])
# pprint.pprint(responder['quoteResponse']['result'][0]['marketCap'])
# pprint.pprint(responder['quoteResponse']['result'][0]['currency'])
# pprint.pprint(responder['quoteResponse']['result'][0]['ask'])
# pprint.pprint(responder['quoteResponse']['result'][0]['bid'])
# pprint.pprint(responder['quoteResponse']['result'][0]['quoteSourceName'])

print("------------------------------------------")


# pprint.pprint(chart)
