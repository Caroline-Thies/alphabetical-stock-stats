# The Question

Are companies with names higher up in the alphabet more economically successful than others?

# How we got the data

1. get list of stocks and symbols from https://www.nasdaq.com/market-activity/stocks/screener
2. retrieve historical information from yahoo.finance.com for each symbol using yfinance library
   1. some of these did not download correctly, for example because their history was too short
