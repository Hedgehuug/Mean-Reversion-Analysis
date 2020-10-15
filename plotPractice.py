import numpy as np
import time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.style.use("ggplot")
import morePractice as mp
import xlsxwriter


#Defining Chart
plt.ion()
plt.show(block=True)
fig = plt.figure(figsize=(16,9))
ax = fig.add_subplot(1,1,1)


#Variables
#excelFile = open('diffFile.xlsx','w')
plottingDict = {}
checkStart = True
y = [0]
priceList = {}
plottingList = []




while True:
    preList = mp.getPricesDict(mp.getMatchingPairMarkets())
    btcPrice = mp.getBtcPrice()


    if checkStart == True:
        checkStart = False
        priceList = preList
        for i,z in zip(priceList.keys(),priceList.values()):
            priceList[i]['BTCPrice'] = [z['BTCPrice']*btcPrice]
            priceList[i]['USDPrice'] = [z['USDPrice']]
        print(priceList)
        for i,z in zip(priceList.values(),priceList.keys()):
            locI = i['USDPrice'][-1]
            if locI != 0:
                difference = (z,[(i['BTCPrice'][-1] - locI)/locI])
            else:
                difference = (z,[0])
            if difference[1][0] == -1:
                difference[1][0] = 0    
            plottingList.append(difference)
                

    else:
        #Loop to add new prices onto Y Arrays for plotting
        for i,z in zip(priceList.keys(),preList.values()):
            priceList[i]['BTCPrice'].append(z['BTCPrice']*btcPrice)
            priceList[i]['USDPrice'].append(z['USDPrice'])
            
        for i,z in zip(priceList.values(),enumerate(priceList.keys())):
            locI = i['USDPrice'][-1]
            if locI != 0:
                difference = (i['BTCPrice'][-1] - locI)/locI
            else:
                difference = (0)
            if difference == -1:
                difference = 0
            plottingList[z[0]][1].append(difference)
        
        

    
    workbook = xlsxwriter.Workbook('diffFile.xlsx')
    worksheet = workbook.add_worksheet()
    col = 0
    for i,z in zip(plottingList,enumerate(plottingList)):
        row = 0
        worksheet.write(row,col,i[0])
        for item in i[1]:
            row+=1
            worksheet.write(row,col,item)
        col += 1
        ax.plot(y,i[1],color="Red")
        #ax.legend(priceList.keys())
    plt.pause(2)
    y.append(y[-1]+1)
    #for item in plottingList:

    workbook.close()