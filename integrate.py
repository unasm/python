# -*- coding:utf-8 -*- 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import scipy.optimize as spo
import scipy.integrate as sci

def f(x):
    return np.sin(x) + 0.5 * x

a = 0.5
b = 9.5
x = np.linspace(0, 10)
y = f(x)
fig, ax = plt.subplots(figsize = (7, 5))
plt.plot(x, y, 'b', linewidth = 1.5)
plt.ylim(ymin = 0)
Ix = np.linspace(a, b)
Iy = f(Ix)

verts = [(a, 0)] + list(zip(Ix, Iy)) + [(b, 0)]
poly = Polygon(verts, facecolor = '0.7', edgecolor = '0.9')
ax.add_patch(poly)

#plt.text(0.75 * (a + b), 1.5 , "$\int_a^c f(x)dx$", horizontalalignment = 'center', fontsize = 20)
#plt.figtext(0.9, 0.075, '$x$')
#plt.figtext(0.075, 0.9, '$f(x)$')

#ax.set_xticks((a, b))
#ax.set_xticklabels(('$a$', '$b$'))
#ax.set_yticks([f(a), f(b)])
#plt.show()

print sci.fixed_quad(f, a, b)
print sci.quad(f, a, b)
print sci.romberg(f, a, b)

tt = 0
size = 3000

#蒙特卡洛法求积分
for i  in range(1, size):
    np.random.seed(1000)
    x = np.random.random(i * 10) * (b - a) + a
    #print x
    tt += np.sum(f(x)) / (len(x)) * (b - a)
print tt  / (size - 1)
