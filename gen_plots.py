# -*- coding: utf-8 -*-
"""
Created on Thu Apr 02 14:35:54 2015

@author: imkilgor
"""

from newton_basins import plot_basins
import matplotlib.pyplot as plt


n = 500;

plt1 = plot_basins((-1.1, 1.1), (-1.1, 1.1), n, True)
plt2 = plot_basins((-0.1, 0.7), (-0.01, 1.01), n, False)
plt3 = plot_basins((0.35, .45), (0.65, 0.75), n, False)

#plt1.savefig('newton_plt0.png', dpi = 600)

ax1 = plt1.axes[0]
ax1.add_patch(plt.Rectangle((-0.1, -0.01), 0.8, 1.01, fill=None, alpha=1))

ax2 = plt2.axes[0]
ax2.add_patch(plt.Rectangle((0.35, 0.65), 0.1, 0.1, fill=None, alpha=1))

plt.show()

plt1.savefig('newton_plt1.png', dpi = 600)
plt2.savefig('newton_plt2.png', dpi = 600)
plt3.savefig('newton_plt3.png', dpi = 600)
