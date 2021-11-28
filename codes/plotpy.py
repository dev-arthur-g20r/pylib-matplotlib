# This shows the amazing use of Pyplot.

import numpy as np
import matplotlib.pyplot as plt

# Let's play by creating a graph that shapes the alphabet `M`.

xPoints = np.array([1, 2, 3, 4, 5]) # Points in the horizontal axis
yPoints = np.array([10, 20, 15, 20, 10]) # Points in the vertical axis

plt.plot(xPoints, yPoints) # Plot and connect the points
plt.show() # Show the figure