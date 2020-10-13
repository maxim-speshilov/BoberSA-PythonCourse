# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 19:46:35 2020

@author: Maxim Speshilov
"""

import numpy as np
import matplotlib.pyplot as plt
import argparse
import os


if __name__ == '__main__':
    
    coefs = [1., 0, -2.,  -2.]
    file_name = 'newton_fractal.png'
    cmap = 'magma'
    
    parser = argparse.ArgumentParser(description='Create Newton fractals for \
                                     polynomials') 
    parser.add_argument('--coefs',  type=float, default=coefs, nargs='+',
                   help='coefs of polynomial') 
    parser.add_argument('--max_iter', type=int, default=100,
                   help='max number of iterations')
    args = parser.parse_args()
    
    #%%
    os.system('python newton.py')
    
    #%%
    Z = np.load('newton.npy')
    plt.figure(figsize=(16, 16))
    plt.imshow(Z, cmap='magma')
    plt.axis('off')
    plt.savefig('newton.png')


    
    