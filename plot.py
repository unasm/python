import json
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


path = "/Users/tianyi/project/pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt"
records = [json.loads(line) for line in open(path)]

frame = DataFrame(records)

#clean_tz = frame['tz'].fillna('Missing')
#clean_tz[clean_tz == ''] = 'Unknown'
#tz_counts = clean_tz.value_counts()
#tz_counts[0:10].plot(kind='barh', rot=4)
#plt.title("here is a test", fontsize=16)

cframe = frame[frame.a.notnull()]
oper_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
#print cframe['a'].str.contains('Windows')
by_tz_os = cframe.groupby(['tz', oper_system])

#print by_tz_os
agg_counts = by_tz_os.size().unstack().fillna(0)
indexer = agg_counts.sum(1).argsort()
#print indexer[:10]

count_subset = agg_counts.take(indexer)[-10:]
#print count_subset
#agg_counts.plot(kind='barh')
count_subset.plot(kind='barh')
#print oper_system[: 5]
plt.savefig("/Users/tianyi/project/pydata-book/code/test.svg")
