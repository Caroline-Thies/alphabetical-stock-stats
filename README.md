# The Question

Are companies with names higher up in the alphabet more economically successful than others?

# Our data

The data contains a list of stock symbols and company names, as well as corresponding historical stock prices. Where possible, these prices reach back ten years and are measured monthly.

## How we got the data

1. get list of stocks and symbols from https://www.nasdaq.com/market-activity/stocks/screener
2. retrieve historical information from yahoo.finance.com for each symbol using yfinance library
   1. some of these did not download correctly, for example because their history was too short
