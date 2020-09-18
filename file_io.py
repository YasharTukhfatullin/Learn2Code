# 'r' is that there is a file already
# and we want the contents of it
# starts you at the beginning of an existing file
# default

# 'w' is that we want to create file
# regardless of whether it already exists or
# not
# starts you at the beginning of a NEW file

# 'a' is that we want to add to an already existing file
# this starts you at the end of an existing file

# '+' allows you to perform both operations regardless of mode

# 'b' reads and writes are in binary format

import json
# library for importing and exporting json files

import os
# library for dealing with file systems

import glob


# library for pattern matching paths (full filenames)

class Stock():

	def __init__(self, dict):
		self.ticker = dict["ticker"]
		self.price = dict["price"]
		self.high = dict["high"]
		self.low = dict["low"]

	def to_dictionary(self):
		return {
			"ticker": self.ticker,
			"price": self.price,
			"high": self.high,
			"low": self.low
		}

	def get_variance(self):
		return self.high - self.low


with open("tickers.json", "r+") as file:
	tickers = json.load(file)
	stocks = [Stock(symbol) for symbol in tickers]

	for stock in stocks:
		print(stock.ticker)

# stock_data = []
# list_of_file_names = glob.glob("data/*.json")
# for filename in list_of_file_names:
# 	with open(filename, "r+") as file:
# 		tickers = json.load(file)
# 		stock_data += [Stock(symbol) for symbol in tickers]
#
# print(stock_data)
