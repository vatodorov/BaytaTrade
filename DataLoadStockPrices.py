#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This code is used to download stock prices data from Yahoo Finance

Author: Valentin Todorov

"""


import pandas as pd
import io
import requests
import os
import glob


# Stock parameters and source URL
yearParameter = 1970
yahooUrl1 = "http://ichart.finance.yahoo.com/table.csv?s="
yahooUrl2 = "&c="

# Stock symbols location from BATS
batsExchangeUrl = "http://www.batstrading.com/market_data/symbol_listing/csv/"

# Locations to save the data
stockExchangeSymbols = "/Users/valentin/Documents/AlgoTrades/Development/Data/ExchangeSymbols/BATS/bats_exchange_symbols.csv"
stockPricesDataLoc = "/Users/valentin/Documents/AlgoTrades/Development/Data/StockPrices/"


####################################################################

# Pull the stock prices for the symbols in the list
stockSymbols = pd.read_csv(stockExchangeSymbols)
symbols = stockSymbols["Symbols"][1:5].tolist()


# Download and save the stock symbols data
# If data is not available, print a warning message
for i in range(len(symbols)):
    stockTicker = symbols[i]
    stockUrl = yahooUrl1 + stockTicker + yahooUrl2 + str(yearParameter)

    try:
        s2 = requests.get(stockUrl).content
        stockTickerDf = pd.read_csv(io.StringIO(s2.decode('utf-8')))
    except:
        print("WARNING: Data for symbol " +  stockTicker + " is not available")
    else:
        print('\n')
        print("Downloading symbol ->> " + stockTicker + " (remaining: " + str(len(symbols) - i) + ")")
        # print(stockTickerDf.head(1))
        stockTickerDf.to_csv(stockPricesDataLoc + stockTicker + ".csv", index = False)
        
        # Rename the fields
        # All fields except for date should be called [originalName_STOCKNAME]
        Date Open High Low Close Volume "Adj Close"
        
        
    
print('\n')
print("->> END of data download process <<-") 


# Merge the data from all CSV files
listFiles = glob.glob(os.path.join(stockPricesDataLoc, "*.csv"))

tempDf = (pd.read_csv(f) for f in listFiles)
stocksDf = pd.concat(tempDf, axis = 1)


        
    
for i in range(create a list with all filenames in the local repository):
    
    # Append columns to create a wide dataframe
    # Match the columns by "Date"
    # When matching append the stock name to the end of each column, except for "Date"
    # Remove empty spaces from all columns
    
    

    

