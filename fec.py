import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fec = pd.read_csv('../ch09/P00000001-ALL.csv')
unique_cands = fec.cand_nm.unique()
#print fec.shape
fec = fec[fec.contb_receipt_amt > 0]

#print fec.contbr_occupation.value_counts()[:10]
#print fec

bins = np.array([0, 1, 10, 100,1000,10000, 100000, 1000000, 1000000])

fec_mrbo = fec[fec.cand_nm.isin(['Obama, Barack', 'Romney, Mitt'])]

#print fec_mrbo

print fec[:10]
#by_occupation = fec.pivot_table('contb_receipt_amt', index = 'contbr_occupation', columns = 'party', aggfunc = sum)
