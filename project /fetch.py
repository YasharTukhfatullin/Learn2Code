import yfinance as yf
import datetime as dt

default_tickers = ["GOOG", "MMM", "XOM"]


def fetch_weekly_csv(tickers):
	for ticker in tickers:
		symbol = yf.Ticker(ticker)
		data = symbol.history(period="1wk", interval="1d")
		data.to_csv(f"{ticker}_{dt.datetime.now()}.csv")


if __name__ == "__main__":
	fetch_weekly_csv(default_tickers)
