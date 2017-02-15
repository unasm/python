import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
#
#ax1 = fig.add_subplot(2, 2, 1)
#ax2 = fig.add_subplot(2, 2, 2)
#ax3 = fig.add_subplot(2, 2, 3)
#
#ax1.plot(np.random.randn(50).cumsum(), 'r--')
#_ = ax2.hist(np.random.randn(100), bins = 20, color = 'k', alpha = 0.9)
#
#ax3.scatter(np.arange(5), np.arange(5) + 8 * np.random.rand(5))
#ax3.set_xticklabels(['', 'one', 'good', 'bad', 'four', 'sex'], rotation = 30, fontsize = 'small')
#ax3.set_xlabel("tests")
#plt.legend(loc = "betst")
#ax1.set_xlabel("tests")
#plt.subplots_adjust(wspace = 0.12, hspace = 0.32)

ax1 = fig.add_subplot(1, 1, 1)


ax1.plot(np.random.randn(5000).cumsum(), 'r--', label = 'red _test')
ax1.plot(np.random.randn(5000).cumsum(), 'k.', label = 'three')
#_ = ax2.hist(np.random.randn(100), bins = 20, color = 'k', alpha = 0.9)

ax1.legend(loc = "best")
ax1.set_xlabel("tests")
plt.subplots_adjust(wspace = 0.12, hspace = 0.32)

plt.show()
