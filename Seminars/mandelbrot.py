# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 20:29:03 2020

@author: ПК
"""

from multiprocessing import Pool
import numpy as np
from numba import njit

@njit('i8(f8[:])')
def mandelbrot_njitted(point):
    r, max_iter = 100, 100
    x_0, y_0 = point[0], point[1]
    x, y = 0., 0.
    r_squared = r**2
    for n in range(max_iter):
        x, y = x*x - y*y + x_0, 2*x*y + y_0
        if x*x + y*y > r_squared:
            break
    return n
    
if __name__ == '__main__':
    
    with Pool() as pool:
        x = np.linspace(-1.5, 0.5, 2048)
        y = np.linspace(-1., 1., 2048)
        xx, yy = np.meshgrid(x, y)
        points = np.vstack(np.vstack([xx.ravel(), yy.ravel()])).T
        
        result = np.array(pool.map(mandelbrot_njitted, points)).reshape((2048, 2048))
        
        with open('mandelbrot.npy', 'wb') as fout:
            np.save(fout, result)
        
        print('Result in mandelbrot.npy')
    
        