import pandas as pd
from glob import glob
from config


def example_process(tickers):
	for ticker in tickers:
		data = pd.read_csv(csv_path)
		data.head(5)


if __name__ == "__main__":
	example_process()
