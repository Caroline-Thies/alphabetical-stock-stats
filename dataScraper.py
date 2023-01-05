import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr
yf.pdr_override()

def load_symbols_df(path):
    df = pd.read_csv(path, keep_default_na=False)
    return df

def get_data(symbols):
    last_one = symbols.index("MYTE")
    for symbol in symbols[last_one:]:
        print(symbol)
        if "^" not in symbol:
            data = pdr.get_data_yahoo(symbol, period="10y", interval="1mo")
            print(len(data))
            if len(data) > 1:
                filename = symbol.replace("/", "-")
                data.to_csv("data/"+filename+"_hist.csv")
    

symbols_df = load_symbols_df("./symbols.csv")
get_data(symbols_df["Symbol"].to_list())