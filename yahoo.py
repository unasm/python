import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from pandas_datareader import data 
#from pandas.io.data  import DataReader

yahoo = data.get_data_yahoo('SPY', '2006-01-01')
#yahoo = data.get_data_yahoo('SPY', '2006-01-01')
#data = pd.io.data.get_data_yahoo('SPY', '2006-01-01')
#print yahoo.head()
px = yahoo['Adj Close']
returns = px.pct_change()
def to_index(rets):
    print rets
    index = (1 + rets).cumprod()
    first_loc = max(index.notnull().argmax() - 1, 0)
    index.values[first_loc] = 1
    return index

def trend_signal(rets, lookback, lag):
    #print rets.head()
    signal = rets.rolling(min_periods = lookback - 5, window = lookback, center = False).sum()
    #signal = pd.rolling_sum(rets, lookback, min_periods = lookback - 5)
    return signal.shift(lag)

signal = trend_signal(returns, 100, 3)
