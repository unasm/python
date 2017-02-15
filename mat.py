import  matplotlib
import numpy as np

matplotlib.use('Agg')
from matplotlib.pyplot as plt 
#import plot,savefig 

x=np.linspace(-4, 4, 30)
y=np.sin(x)
plt.plot(x,y, '--*b')
#savefig("/Users/tianyi/project/pydata-book/code/test.svg")
show()
#x = linspace(-4, 4, 200)
#f1 = power(10, x)
#f2 = power(e, x)
#f3 = power(2, x)
#
#plot(x, f1, 'r', x, f2, 'b', x, f3, 'g', linewidth=2)
#
#axis([-4, 4, -0.5, 8])
#title("a simple test", fontsize=16)
#show()
