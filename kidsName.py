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
total_births = names.pivot_table('births', index = 'year', columns = 'sex', aggfunc = 'sum')

#print names.tail()
#print total_births.tail()
#total_births.plot(title = "title birth by sex and year")
#

def add_prop(group):
    births = group.births.astype(float)
#    print births
    group['prop'] = births / births.sum()
    return group
sexName = names.groupby(['year', 'sex']).apply(add_prop)

#print np.allclose(sexName.groupby(['year', 'sex']).prop.sum(), 1)

def get_top1000(group):
    return group.sort_values(by = 'births', ascending = False)[: 1000]

grouped = sexName.groupby(['sex', 'year'])
#grouped = sexName.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)

print top1000.head()
total_births = top1000.pivot_table('births', index = 'year', columns = 'name', aggfunc = sum)
print total_births.head()

#subset = total_births[['John', 'Harry', 'Mary', 'Marilyn', 'Wing']]
#subset = total_births[['John', 'Harry', 'Mary', 'Marilyn', 'Julia']]


#subset.plot(subplots = True, figsize = (8, 10), grid = False, title = "number of births per year")
#print top1000;
#print subset
#print total_births


#table = top1000.pivot_table('prop', index = 'year', columns = 'sex', aggfunc = sum)
#table.plot(title = "title", yticks = np.linspace(0, 1.2, 13), xticks = range(1880, 2020, 10))

def get_quantitle_count(group, q = 0.5):
    group = group.sort_values(by = 'prop', ascending = False)
    #print group.prop.cumsum().searchsorted(q)[0]
    return group.prop.cumsum().searchsorted(q)[0] + 1
diversity = top1000.groupby(['year', 'sex']).apply(get_quantitle_count)
#print diversity.head()
diversity =  diversity.unstack('sex')
#print diversity.head()
#diversity.plot(title = "Nuber of popular names in top50%")
#plt.savefig("/Users/tianyi/project/pydata-book/code/test.svg")

