import os
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

APIKey = "VPNQRTV7WSSWRFWK"

def getStockData(symbol):
    try:
        print("Looking up symbol...")
        timeSeries = TimeSeries(key=APIKey,output_format='pandas')
        data, meta_data = timeSeries.get_intraday(symbol=symbol,interval='1min')
        return str(data.tail(1).iloc[0]['4. close'])
    except:
        return "Symbol Not Found"

def main():
    while 1:
        userinput = input("Enter stock symbol or type QUIT to quit: ").upper()
        if userinput != "QUIT":
            serverinfo = "The current price of {} is {}\n".format(userinput, getStockData(userinput))
            print(serverinfo)
            f = open('japi.out', 'a')
            f.write("\n"+serverinfo)
        else:
	    print("Stock Quotes retrieved successfully!")
            f.close()
            exit()

main()
