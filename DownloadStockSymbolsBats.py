#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This code pulls a list with stock symbols from the BATS exchange

Author: Valentin Todorov
"""

import pandas as pd
import io
import requests



# Stock symbols location from BATS
batsExchangeUrl = "http://www.batstrading.com/market_data/symbol_listing/csv/"

# Locations to save the data
stockExchangeSymbols = "/Users/valentin/Documents/AlgoTrades/Development/Data/ExchangeSymbols/BATS/bats_exchange_symbols.csv"
stockPricesDataLoc = "/Users/valentin/Documents/AlgoTrades/Development/Data/StockPrices/"


####################################################################

# Get a list with stock symbols from the BATS exchange
stockSymbolsUrl = batsExchangeUrl
s = requests.get(stockSymbolsUrl).content
stockSymbols = pd.read_csv(io.StringIO(s.decode('utf-8')))

# Save the CSV file to a local repository - add a date to the filename
stockSymbols.to_csv(stockExchangeSymbols)


