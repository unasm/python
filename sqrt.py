import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
#print xs
#print ys
#print ys.head()

#z = np.sqrt(xs ** 2 + ys ** 2)
#trand = np.random.randn(1000, 1000)
#plt.imshow(trand, cmap = plt.cm.gray)
#plt.colorbar()
#plt.title("sqrt x ** 2 + y ** 2")
nsteps = 100000
draws = np.random.randint(0, 2, size = nsteps)
print draws
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()
ser = pd.Series(walk, index = np.arange(0, nsteps, 1))
#ser = pd.Series(np.random.randint(0, 1000, size = nsteps), index = np.arange(0, 1000, 1))
ser.plot()
#print walk
#plt.imshow(walk, cmap = plt.cm.gray)
#plt.colorbar()
#x=np.linspace(-4, 4, 30)
#y=np.sin(x)
#print y.shape
#print x.shape
#plt.plot(x,y, '--*b')

#walk.plot(title = "title")
plt.savefig("/Users/tianyi/project/pydata-book/code/test.svg")
