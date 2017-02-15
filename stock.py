import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


#fig = plt.figure()
#ax1 = fig.add_subplot(1, 1, 1)


close_px_all = pd.read_csv('../ch09/stock_px.csv', parse_dates = True, index_col = 0)
#print close_px_all.head()
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
close_px = close_px.resample('B').ffill()
#print close_px['AAPL']
#close_px['AAPL'].index
#data = close_px.pivot_table('AAPL', index = '')
close_px['AAPL'].plot(label = 'AAPL')

#ax1.legend(loc = "best")

#close_px.ix['2009'].plot()

#print close_px.ix['2009']
plt.show()

#plt.savefig("/Users/tianyi/project/pydata-book/code/test.svg")
