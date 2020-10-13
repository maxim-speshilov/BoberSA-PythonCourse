# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 20:48:44 2020

@author: Maxim Speshilov
"""

import numpy as np
from multiprocessing import Pool


def newton_n(z_0):
    z = z_0
    f =  np.polynomial.Polynomial([1., 0, -2.,  -2.])
    df = f.deriv()
    roots = f.roots()
    max_iter = 100
    
    for n in range(max_iter):
        z = z - f(z) / df(z)
        
    k = np.argmin(np.abs(np.ones_like(roots) * z - roots))
    
    return k


if __name__ == '__main__':
    
     with Pool() as pool:
    
         x = np.linspace(-1., 1., 1000)
         y = np.linspace(-1., 1., 1000)
         xx, yy = np.meshgrid(x, y)
         points = np.vstack(np.vstack([xx.ravel(), yy.ravel()])).T
         points = points[:, 0] + 1.0j * points[:, 1]
         
         result = np.array(pool.map(newton_n, points)).reshape((1000, 1000))
        
         with open('newton.npy', 'wb') as fout:
             np.save(fout, result)
        
         print('Result in newton.npy')