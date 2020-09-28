import json
import ccxt
import numpy as np
import matplotlib.pyplot as plt
import time



#the document file to write to
writeFile = open("info.json","w")

#returns all pairs with the chosen quote currency
def stripString(listOfStrings):
    chippedList = []
    for i in listOfStrings:
        if i[-4:] == "USDT":
            chippedList.append(i)
    return chippedList



exchange = ccxt.ftx()
exchangeMarkets = exchange.load_markets()
marketList = list(exchangeMarkets.keys())


def getOrderBook(market):
    return exchange.fetch_order_book(market)
    
writeCondition = False

if writeCondition == True:
    strippedList = stripString(marketList)
    marketKeys = {
        "Coinlist": strippedList
    }
    json.dump(marketKeys,writeFile,indent = 6)