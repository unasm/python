import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

years = range(1880, 2011)
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
    path = '/Users/tianyi/project/pydata-book/ch02/names/yob%d.txt' % year
    frame = pd.read_csv(path, names = columns)
    frame['year'] = year
    pieces.append(frame)
names = pd.concat(pieces, ignore_index = True)

get_last_letter = lambda x:x[-1]

last_letters = names.name.map(get_last_letter)
last_letters.name = 'last_letters'

#print last_letters

table = names.pivot_table('births', index = last_letters, columns = ['sex', 'year'], aggfunc = sum)

#print table.head()

subtable = table.reindex(columns = [1910, 1960, 2010], level = 'year')
#print subtable.head()

letter_prop = subtable / subtable.sum().astype(float)

#print letter_prop.head()

#fig, axes = plt.subplots(2, 1, figsize = (10, 6))
#letter_prop['M'].plot(kind = 'bar', rot = 0, ax = axes[0], title = "Male")
#letter_prop['F'].plot(kind = 'bar', rot = 0, ax = axes[1], title = "Female", legend = False)

letter_prop = table / table.sum().astype(float)

letter_prop.name = 'letter_prop'

#dny_ts = letter_prop.ix[['d', 'n', 'y'], 'M'].T

dny_ts = letter_prop['M'].T
print dny_ts.head()
print dny_ts.shape
print dny_ts.ndim

#dny_ts.plot(title = "d,n,y is changing")



plt.savefig("/Users/tianyi/project/pydata-book/code/test.svg")
