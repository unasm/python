import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

dates = [
            datetime(2011,1,2), 
            datetime(2011,1,5),
            datetime(2011,1,7),
            datetime(2011,1,8),
            datetime(2011,1,10),
            datetime(2011,1,12),
        ]
#ts = pd.Series(np.random.randn(6), index = dates)
#print ts
index = pd.date_range('4/30/2012', '4/30/2012', freq = 'BM', normalize = True)
print index
print pd.date_range('1/1/2012 12:12:12', periods = 20, normalize = True)

