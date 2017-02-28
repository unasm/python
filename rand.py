# -*- coding:utf-8 -*- 

import numpy as np
import matplotlib.pyplot as plt

#S0 = 100
#r = 0.05
sigma = 0.25
#T = 2.0
#I = 10000
#ST1 = np.random.standard_normal(I)
#ST1 = S0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * np.random.standard_normal(I))
#plt.hist(ST1, bins = 400)
I = 10000
M = 5000
r = 0.05
T = 2.0
dt = T / M
S = np.zeros((M + 1, I))
S0 = 100
S[0] = S0

for t in range(1 , M+1):
    S[t] = S[t-1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * np.random.standard_normal(I))

plt.plot(S[:, :1], lw = 1.0)
#plt.plot(np.random.standard_normal(1000), lw = 1.0)
plt.xlabel('time')
plt.ylabel('index level')
plt.grid(True)
plt.show()
