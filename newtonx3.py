# -*- coding: utf-8 -*-
import numpy as np

"""
Created on Mon Mar 30 12:24:21 2015

Do Newton's Method on x^3-1 = 0, starting at (complex) point x0.
Return a number for each solution:
    0: 1
    1:  -(-1)^(1/3)
    2: (-1)^(2/3)
    -1: no convergence

See Sternberg p. 18

@author: imkilgor
"""

# P(x) = x^3 - 1
# derivative P'(x) = 3x^2
# Iterate:
#   x_n+1 = x_n - P(x)/P'(x)

def slns():
    return np.array([
        1,
        -1*np.complex(-1)**(1./3.),
        np.complex(-1)**(2./3.)
    ])

def newtonx3(x0):
    MIN_DIST = 1e-5;   # Converge if |x_n+1 - x_n| <= 10^-5
    MAX_ITER = 40;     # Quit after 40 iterations

    dist = 99;
    niter = 0;
    x_n = x0;     # Initial point

    # Iterate Newton's method
    while (dist > MIN_DIST and niter < MAX_ITER):
        # compute next point
        x_np1 = x_n - np.true_divide((x_n**3 - 1),(3*x_n**2))

	# check convergence
        dist = abs(x_np1 - x_n)

	# Update
        niter += 1 
        x_n = x_np1

    # check which soln (or no convengence) and pick colour
    if (niter == MAX_ITER):
        return -1
    else:
        # Pick closest solution
        return np.argmin(abs(x_n - slns()))
