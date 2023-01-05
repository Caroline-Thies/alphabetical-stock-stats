import pandas as pd 

# read data
symbols_df = pd.read_csv("symbols.csv")
print(symbols_df)

# drop names that start with a digit - not interesting for us
indices_to_drop = []
for i in symbols_df.index:
    stock_name = symbols_df.iloc[i]["Name"]
    if stock_name[0].isdigit():
        indices_to_drop.append(i)
symbols_df.drop(symbols_df.index[indices_to_drop], inplace=True)
sorted_symbols_df = symbols_df.sort_values(by="Name")
print(sorted_symbols_df)