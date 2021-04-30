import numpy as np
import pylab as pl

A = np.arange(1, 7, 1)
B = np.array([2, 4, 3, 5, 2, 3])
C = np.array([2, 3, 1, 4, 2, 5])

pl.plot(A, B, 'o', A, C, '-')
pl.show()
