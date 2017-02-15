import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({
    'key1' : ['a', 'a', 'b', 'b', 'a'],
    'key2' : ['one', 'two', 'one', 'two', 'one'],
    'data1' : np.random.randn(5),
    'data2' : np.random.randn(5)
    })
def test(data):
    print data
#    print "hello"
    return data
#print df['data1']

#print df['data1'].groupby(df['key1']).apply(test)
