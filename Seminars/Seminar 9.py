
#%%

import matplotlib.pyplot as plt
from numba import njit
import numpy as np
from functools import partial
import os

#%%
def mandelbrot(x_0, y_0, r=10, max_iter=100):
    c = x_0 + 1j*y_0
    z = 0
    for n in range(max_iter):
        z = z**2 + c
        if np.abs(z) > r:
            break
    return n

def mbr_xy(x, y, r=10, max_iter=100):
    f = partial(mandelbrot, r=r, max_iter=max_iter)
    return np.vectorize(f)(*np.meshgrid(x, y, sparse=True))


#%%


@njit('i8(f8,f8,f8, i8)')
def mandelbrot_njitted(x_0, y_0, r, max_iter):
    x, y = 0., 0.
    r_squared = r**2
    for n in range(max_iter):
        x, y = x*x - y*y + x_0, 2*x*y + y_0
        if x*x + y*y > r_squared:
            break
    return n

@njit('f8[:,:](f8[:],f8[:],f8, i8)')
def mbr_xy_njitted(x, y, r, max_iter):
    result = np.empty((y.shape[0], x.shape[0]))
    for i, x_0 in enumerate(x):
        for j, y_0 in enumerate(y):
            result[j, i] = mandelbrot_njitted(x_0, y_0, r, max_iter)
    return result


#%%

x = np.linspace(-1.5, 0.5, 200)
y = np.linspace(-1., 1., 200)


#%%


mandelbrot(x[0], y[0])


#%%


mandelbrot_njitted(x[0], y[0], 10, 100)


#%%


Z = mbr_xy_njitted(x, y, 10, 100)


#%%


plt.figure(figsize=(10, 10))
plt.imshow(Z, cmap='magma')
plt.axis('off');


#%%


os.system('python mandelbrot.py')


#%%

Z = np.load('mandelbrot.npy')
plt.figure(figsize=(16, 16))
plt.imshow(Z, cmap='magma')
plt.axis('off')


