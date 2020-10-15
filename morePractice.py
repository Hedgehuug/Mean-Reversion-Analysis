import json
import ccxt
import numpy as np
import matplotlib.pyplot as plt
import time

#This file currently gets all spot markets on binance, and finds all markets that have both USDT and BTC pairs



#the document file to write to
writeFile = open("info.json","w")

#returns all pairs with the chosen quote currency
def stripString(listOfStrings):
    chippedList = []
    for i in listOfStrings:
        if i[-4:] == "USDT":
            chippedList.append(i[:-5])
        if i[-3:] == "BTC":
           chippedList.append(i[:-4])
    return chippedList



exchange = ccxt.binance()
exchangeMarkets = exchange.load_markets()
marketList = list(exchangeMarkets.keys())

#getOrderBook
def getOrderBook(market):
    return exchange.fetch_order_book(market)


#gets any asset that has both the dollar and BTC as quote prices
def getMatchingAssets(assetList):
    counter = {i:assetList.count(i) for i in assetList}
    match = []
    for x in counter:
        if counter[x] == 2:
            match.append(x)
    return match



#Fetch all markets that have both USDT and BTC pairs
def getMatchingPairMarkets():
    pairList = []
    finalList = []
    for i in getMatchingAssets(stripString(marketList)):
        pairList.append(i+"/USDT")
        pairList.append(i+"/BTC")
    finalList = exchange.fetchTickers(symbols = pairList, params = {})
    for i in finalList.values():
        i = i['last']
    return finalList

def getPricesDict(rawPriceList):
    plottingDict = {}
    for i,z in zip(rawPriceList,rawPriceList.values()):
        a = ""
        if i[-3:] == "BTC":
            a = i[:-4]
            if (plottingDict.get(a)) == None:
                plottingDict.update({a:{'BTCPrice':z['last'],'USDPrice':0}})
            else:
                plottingDict[i[:-4]]['BTCPrice'] = z['last']
        elif i[-4:] == "USDT":
            a = i[:-5]
            if (plottingDict.get(a)) == None:
                plottingDict.update({a:{'BTCPrice':0,"USDPrice":z['last']}})
            else:
                plottingDict[i[:-5]]['USDPrice'] = z['last']
    return plottingDict


        

def getBtcPrice():
    btcDict = exchange.fetchTicker('BTC/USDT')
    return btcDict['last']




    
writeCondition = True
getMatchingPairMarkets()
priceDictDelivery = getPricesDict(getMatchingPairMarkets())
#Write to info files for analysis
if writeCondition == True:
    strippedList = getMatchingAssets(stripString(marketList))
    marketKeys = {
        "Coinlist": strippedList
    }
    json.dump(marketKeys,writeFile,indent = 6)