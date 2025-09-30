import yfinance as yf
import pandas as pd
import datetime as dt

'''
Method for getting the current value of a specified stock.
'''
def getCurrentStockValue(ticker: str):
    stockData = yf.Ticker(ticker)
    currentVal = stockData.info['regularMarketPrice']
    return currentVal


def scrapeStockData(ticker: str, period):
    dataFrame = yf.download(ticker, period=period)
    dataFrame = dataFrame[["Close"]].reset_index()

    dataFrame["Date"] = pd.to_datetime(dataFrame["Date"])
    dataFrame["Date_Ordinal"] = dataFrame["Date"].map(dt.datetime.toordinal)
    print(dataFrame)
    return dataFrame