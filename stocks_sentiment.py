#!/usr/bin/python3

# Imports if Flask endpoints are incorporated to application
# from flask import render_template, url_for
# from flask import request
# from flask import redirect
# from flask import Flask
import requests
import pprint
import config as con
import random

wallst_curl = 'https://tradestie.com/api/v1/apps/reddit'

# store response of the wall street bets stock ticker analysis API
resp = requests.get(wallst_curl).json()

# display only the ticker and sentiment for 50 prominent tickers numbered
i = 1
for ticker in resp:
    pprint.pprint(f"{i}. " + ticker['ticker'] + ": " + ticker['sentiment'])
    i += 1

print("------------------------------------------")

yahoo_curl = 'https://yfapi.net/v6/finance/quote'


# use user input to analyze the ticker/stock further using Yahoo Finance API

def searchByInput():
    queryInput = ''
    print("Choose ticker(s) above to analyze further")
    while queryInput == '':
        queryInput = input("Enter 1 ticker from the above list: \n").upper()

    print('\n')
    query_string = {"symbols": f"{queryInput}"}

    # responder builds request with user input as query params
    # it takes an api key registered for yahoo finance api and saved
    # in the config.py file saved as
    # headers = {'x-api-key':'YOUR-PERSONAL-API_KEY'}
    responder = requests.request(
        "Get", yahoo_curl, headers=con.headers, params=query_string).json()

    # pprint.pprint(responder)
    # pretty print all the wanted key-values from response
    print("Symbol: ", end='')
    symbol = pprint.pprint(responder['quoteResponse']['result'][0]['symbol'])
    print("Name: ", end='')
    name = pprint.pprint(responder['quoteResponse']
                         ['result'][0]['displayName'])
    print("52 WK Range: ", end='')
    yearrange = pprint.pprint(
        responder['quoteResponse']['result'][0]['fiftyTwoWeekRange'])
    print("Market Cap: ", end='')
    cap = pprint.pprint(responder['quoteResponse']['result'][0]['marketCap'])
    print("Currency: ", end='')
    currencytype = pprint.pprint(
        responder['quoteResponse']['result'][0]['currency'])
    print("Ask: ", end='')
    ask = pprint.pprint(responder['quoteResponse']['result'][0]['ask'])
    print("Bid: ", end='')
    bid = pprint.pprint(responder['quoteResponse']['result'][0]['bid'])
    print("Source: ", end='')
    source = pprint.pprint(
        responder['quoteResponse']['result'][0]['quoteSourceName'])

    print('\n')
    # insights
    insights_url = f'https://yfapi.net/ws/insights/v1/finance/insights'
    insight_string = {"symbol": f"{queryInput}"}
    insight = requests.request(
        "Get", insights_url, headers=con.headers, params=insight_string).json()

    # display the Insights
    print('Longterm Trajectory: ', end='')
    longterm = pprint.pprint(
        insight['finance']['result']['instrumentInfo']['technicalEvents']['longTerm'])
    print('Midterm Trajectory: ', end='')
    midterm = pprint.pprint(
        insight['finance']['result']['instrumentInfo']['technicalEvents']['midTerm'])
    print('Shortterm Trajectory: ', end='')
    shorterm = pprint.pprint(
        insight['finance']['result']['instrumentInfo']['technicalEvents']['shortTerm'])
    print('Analyst: ', end='')
    analyst = pprint.pprint(
        insight['finance']['result']['instrumentInfo']['technicalEvents']['provider'])

    print('\n')
    listofins = insight['finance']['result']['reports']
    # store a random index of list of reports
    rand_insight = listofins.index(random.choice(listofins))

    # get 1 random summary from reports list
    print("Review:")
    pprint.pprint(insight['finance']['result']
                  ['reports'][rand_insight]['summary'])

    # date of summary
    print("Date: ", end='')
    pprint.pprint(insight['finance']['result']['reports'][0]['publishedOn'])

    print("-------------------------------------------------")


# prompt user to choose another ticker

searchByInput()
