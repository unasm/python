# -*- coding:utf-8 -*- 

import numpy as np
import matplotlib.pyplot as plt

def bsm_mcs_valuation(strike):
    print strike
    S0 = 100; T = 1.0; r = 0.05; vola = 0.2
    M = 50; I = 20000
    dt = T/M
    #标准分布 矩阵
    rand = np.random.standard_normal((M + 1, I))
    S = np.zeros((M + 1, I));
    S[0] = S0
    for t in range(1, M + 1):
        S[t] = S[t-1] * np.exp((r - 0.5 * vola ** 2) * dt + vola * np.sqrt(dt) * rand[t])
        #print S[t]
    value = (np.exp(-r * T) * np.sum(np.maximum(S[-1] - strike, 0)) / I)
    return value

def seq_value(n):
    strikes = np.linspace(80, 120, n)
    option_values = []
    for strike in strikes:
        option_values.append(bsm_mcs_valuation(strike))
    return strikes, option_values

n = 100
strikes, option_values_seq = seq_value(n)

print len(strikes)
print len(option_values_seq)
plt.figure(figsize = (8, 4))
#plt.plot(strikes, option_values_seq, 'b')
plt.plot(strikes, option_values_seq, 'r.')

plt.grid(True)
plt.xlabel('strikes')
plt.ylabel('European call option values')
plt.show()
