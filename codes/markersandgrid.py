# This shows the use of markers and grids.

import numpy as np
import matplotlib.pyplot as plt

''' 
Let's add some dots per point to see how it's done in the chart.
Remember Cartesian Coordinate Plane back then from your Geometry class?
'''

xPoints = np.array([1, 2, 3, 4, 5])
yPoints = np.array([10, 20, 15, 20, 10])

plt.plot(xPoints, yPoints, marker="o") # Display dots as a marker.

plt.grid() # Display horizontal and vertical guidelines for plotting in the graph.

plt.show()