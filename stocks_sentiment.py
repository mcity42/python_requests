#!/usr/bin/python3

from locale import currency
from flask import render_template
from flask import request
from flask import redirect
from flask import Flask
from random import randint
import requests
import pprint
import config as con
import random


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
queryInput = ''
while queryInput == '':
    queryInput = input(
        "Enter 1 ticker from the above list: \n").upper()
print('\n')
# chart
# chart_url = f'https://yfapi.net/v6/finance/chart'
# chart_string = {"ticker": f"{queryInput}"}
# chart = requests.request(
#     "Get", chart_url, headers=con.headers, params=chart_string).json()
# pprint.pprint(chart)

# place user input into query
query_string = {"symbols": f"{queryInput}"}


# responder builds request with user input as query params
# it takes an api key registered for yahoo finance api and saved
# in the config.py file saved as
# headers = {'x-api-key':'YOUR-PERSONAL-API_KEY'}

responder = requests.request(
    "Get", yahoo_curl, headers=con.headers, params=query_string).json()


# pprint.pprint(responder)
# pretty print
print("Symbol: ", end='')
symbol = pprint.pformat(responder['quoteResponse']['result'][0]['symbol'])
print("Name: ", end='')
name = pprint.pformat(responder['quoteResponse']['result'][0]['displayName'])
print("52 WK Range: ", end='')
yearrange = pprint.pformat(responder['quoteResponse']
                           ['result'][0]['fiftyTwoWeekRange'])
print("Market Cap: ", end='')
cap = pprint.pformat(responder['quoteResponse']['result'][0]['marketCap'])
print("Currency: ", end='')
currencytype = pprint.pformat(
    responder['quoteResponse']['result'][0]['currency'])
print("Ask: ", end='')
ask = pprint.pformat(responder['quoteResponse']['result'][0]['ask'])
print("Bid: ", end='')
bid = pprint.pformat(responder['quoteResponse']['result'][0]['bid'])
print("Source: ", end='')
source = pprint.pformat(
    responder['quoteResponse']['result'][0]['quoteSourceName'])


print('\n')
# insights
insights_url = f'https://yfapi.net/ws/insights/v1/finance/insights'
insight_string = {"symbol": f"{queryInput}"}
insight = requests.request(
    "Get", insights_url, headers=con.headers, params=insight_string).json()

# print("Isnights:")
print('Longterm Trajectory: ', end='')
longterm = pprint.pformat(insight['finance']['result']
                          ['instrumentInfo']['technicalEvents']['longTerm'])
print('Midterm Trajectory: ', end='')
midterm = pprint.pformat(insight['finance']['result']
                         ['instrumentInfo']['technicalEvents']['midTerm'])
print('Shortterm Trajectory: ', end='')
shorterm = pprint.pformat(insight['finance']['result']
                          ['instrumentInfo']['technicalEvents']['shortTerm'])
print('Analyst: ', end='')
analyst = pprint.pformat(insight['finance']['result']
                         ['instrumentInfo']['technicalEvents']['provider'])


print('\n')

listofins = insight['finance']['result']['reports']
# save also caTCH INDEX
rand_insight = listofins.index(random.choice(listofins))

# get 1st summary from reports list --- change to choice() to get rand index/quote
pprint.pprint(insight['finance']['result']['reports'][rand_insight]['summary'])

# date of summary
print("Date: ", end='')
pprint.pprint(insight['finance']['result']['reports'][0]['publishedOn'])

print("------------------------------------------")

# -------------------------------------------------------


app = Flask(__name__)


@app.route("/")
def start():
    return render_template("postmaker.html")


@app.route("/login", methods=["POST"])
def login():
    if request.form.get("nm"):
        result = request.form.get("nm")
        if 1 > 0:
            return redirect("/correct")
        else:
            return redirect("/")
    else:
        return redirect("/")


@app.route("/correct")
def success():
    return f"Symbol: {symbol}\nName: {name}\n52 Week Range: {yearrange}\nMarket Cap: {cap}\nCurrency: {currencytype}\nAsk: {ask}\nBid: {bid}\Source: {source}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)  # runs the application
