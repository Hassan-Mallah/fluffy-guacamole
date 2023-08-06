import yfinance as yf

BTC_Ticker = yf.Ticker("BTC-USD")

# type pandas.core.frame.DataFrame, data for 5 days
BTC_Data = BTC_Ticker.history(period="5d")

# print data
print(BTC_Data.to_string())

BTC_Data = BTC_Ticker.history(start="2023-07-17", end="2023-07-21", interval="15m")

# print ticket
print('Ticket', BTC_Ticker.ticker)


# BTC_Data keys Index(['Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits'], dtype='object')

# get one value
print(BTC_Data['Open'][0])

# get High
print(BTC_Data['High'])

# print rows
for index, row in BTC_Data.iterrows():
    print(index, row)
