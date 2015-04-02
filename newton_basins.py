#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import newtonx3

# Newton's method attractor basins for x^3 - 1
# roots are 1, (-1)^(2/3), and -(-1)^(1/3)

# Do Newton's method for x^3 - 1 on each point in a
# grid and plot the solutions reached

def plot_basins(xrange, yrange, n, plot_slns):
    # Grid dimensions/step
    stepx = (xrange[1]-xrange[0]) / n
    stepy = (yrange[1]-yrange[0]) / n
    x = np.arange(xrange[0], xrange[1], stepx); # real axis
    y = np.arange(yrange[0], yrange[1], stepy); # imag axis
    y = y[::-1]

    # Create grid and compute results
    grid = np.zeros((y.size,x.size))
    for ii in range(0, x.size):  # grid[ii,jj]
        for jj in range(0, y.size):
            x0 = np.complex(x[ii], y[jj])
            grid[jj,ii] = newtonx3.newtonx3(x0)

    # Plot
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    # Plot convergence results
    #%Aspect = 'auto'
   # if (plot_slns):
    Aspect = 'equal';
    ax1.imshow(grid, extent=[xrange[0],xrange[1],yrange[0],yrange[1]], aspect=Aspect)
    
    if (plot_slns):
        # Plot each solution
        slns = newtonx3.slns();
        plt.scatter(np.real(slns[0]), np.imag(slns[0]), marker='x', s=20, c='k')
        plt.scatter(np.real(slns[1]), np.imag(slns[1]), marker='x', s=20, c='k')
        plt.scatter(np.real(slns[2]), np.imag(slns[2]), marker='x', s=20, c='k')
        # Plot axes and unit circle
        circle = plt.Circle((0,0), 1, color='black', fill=False)
       # plt.plot((xrange[0], xrange[1]), (0, 0), 'k-')
       # plt.plot((0, 0), (yrange[0], yrange[1]), 'k-')
        fig.gca().add_artist(circle)


    return fig

if __name__ == "__main__":
    import sys

    ############## default grid
    XRANGE = (-1.1,1.1)
    YRANGE = (-1.1,1.1)
    N = 50 # N^2 grid points
    plot_slns = True
    ############## 

    if (len(sys.argv) == 6):
        XRANGE = (float(sys.argv[1]), float(sys.argv[2]))
        YRANGE = (float(sys.argv[3]), float(sys.argv[4]))
        N = int(sys.argv[5])
        plot_slns = False
    if (len(sys.argv) != 6 and len(sys.argv) != 1):
        sys.exit('Usage: %s xmin xmax ymin ymax N' % sys.argv[0])

    plt = plot_basins(XRANGE, YRANGE, N, plot_slns)
    plt.show()