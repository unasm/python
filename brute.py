# -*- coding:utf-8 -*- 

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as spo

def fo((x, y)):
    z = np.sin(x) + 0.05 * x ** 2 + np.sin(y) + 0.05 * y ** 2
    return z

opt1 = spo.brute(fo, ((-10, 10.1, 1), (-10, 10.1, 1)), finish = spo.fmin, full_output = False)
#opt1 = spo.brute(fo, ((-10, 10.1, 0.1), (-10, 10.1, 0.01)), finish = None, full_output = False)

print opt1

print fo(opt1)

opt2 = spo.fmin(fo, opt1, xtol = 0.1, ftol = 0.01)
print opt2

print fo(opt2)

opt2 = spo.fmin(fo, (2.0, 2.0), maxiter = 250)
print opt2
