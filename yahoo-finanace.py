import yfinance as yf

BTC_Ticker = yf.Ticker("BTC-USD")

# type pandas.core.frame.DataFrame, data for 5 days
BTC_Data = BTC_Ticker.history(period="5d")

print('Ticket', BTC_Ticker.ticker)
print(BTC_Data.to_string())
