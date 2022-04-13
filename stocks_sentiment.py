import requests
import pprint
import config as con
from tkinter import *

wallst_curl = 'https://tradestie.com/api/v1/apps/reddit'

# dictionary of the json response
resp = requests.get(wallst_curl).json()

# display the sentiment for 50 prominent tickers
for ticker in resp:
    pprint.pprint(ticker['ticker'] + ": " + ticker['sentiment'])


print("------------------------------------------")

yahoo_curl = 'https://yfapi.net/v6/finance/quote'

print("Choose ticker(s) above to analyze further")
queryInput = input(
    "Enter 1 or more tikers listed above separated by a comma,20 max: \n").upper()

# place user input into query
query_string = {"symbols": f"{queryInput}"}


# responder builds request with user input as query params
# it takes an api key registered for yahoo finance api and saved
# in the config.py file saved as
# headers = {'x-api-key':'YOUR-PERSONAL-API_KEY'}
responder = requests.request(
    "Get", yahoo_curl, headers=con.headers, params=query_string).json()

# pretty print
pprint.pprint(responder)


# class Window(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.master = master

#         self.pack(fill=BOTH, expand=1)

#         exitButton = Button(self, text="Exit", command=self.clickExitButton)

#         exitButton.place(x=0, y=0)

#     def clickExitButton(self):
#         exit()


# root = Tk()
# app = Window(root)
# root.wm_title("Stocks")
# root.geometry('320x200')
# root.mainloop()

# stats = Text(root)
# stats.insert(INSERT, resp)
# stats.pack()
