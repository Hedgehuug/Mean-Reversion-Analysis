import statsmodels
from statsmodels.tsa.stattools import adfuller
import pandas as pd
import numpy as np

df1 = pd.read_excel(r'Kleinsdata/BTCUSDT_Graph.xlsx')

print(statsmodels.tsa.stattools.coint(df1['close'],df1['open']))


class StationarityTests:
    def __init__(self,significance=.05):
        self.significaneLevel = significance
        self.pValue = None
        self.isStationary = None

    def adfStationarityTest(self, timeseries, printResults = True):
        #ADF
        adf = adfuller(timeseries, autolag='AIC')

        self.pValue = adf[1]

        if self.pValue < self.significaneLevel:
            self.isStationary = True
        else:
            self.isStationary = False

        if printResults == True:
            adfResults = pd.Series(adf[0:4], index=["Statistic","P-Value","Lags used","Observations used"])
            print(adfResults)


stTest = StationarityTests()

stTest.adfStationarityTest(df1['close'])




