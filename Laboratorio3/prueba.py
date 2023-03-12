import matplotlib.pyplot as plt
import numpy as np
import funciones as fs

DATA_SET_SIZE = 100
DATA_SET_SPARES_RATIO = 20
DATA_SET_X_LIM = 10

X = np.linspace(0,DATA_SET_X_LIM,DATA_SET_SIZE).reshape(())
Xr = np.hstack((
    np.ones((DATA_SET_SIZE,1)),
    X
))
y = 3 + 2 * X + np.rand(DATA_SET_SIZE,1) * DATA_SET_SPARES_RATIO

plt.plot(X,y,'ro')
plt.show()

print(X.shape)