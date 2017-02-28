# -*- coding:utf-8 -*- 

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl

def fm((x,y)):
    return 1 - x - y
    #return np.sin(x) + 0.25 * x + np.sqrt(y) + 0.05 * y ** 2

#x = np.linspace(0, 10, 20)
x = np.linspace(-10 , 10, 40)
#y = np.linspace(0, 10, 20)
y = np.linspace(-10 , 10, 40)

X, Y = np.meshgrid(x, y)
Z = fm((x, y))

x = x.flatten()
y = y.flatten()

fig = plt.figure(figsize = (9, 6))
ax = fig.gca(projection = '3d')
surf = ax.plot_surface(X, Y, Z, rstride = 2, cstride = 2, cmap = mpl.cm.coolwarm, linewidth = 0.5, antialiased = True)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
fig.colorbar(surf, shrink = 0.5, aspect = 5)
plt.show()
