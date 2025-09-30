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