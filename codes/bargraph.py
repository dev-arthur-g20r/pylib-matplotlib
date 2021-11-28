# This shows how to create line graphs.

import numpy as np
import matplotlib.pyplot as plt

xPoints = np.array(["Male", "Female"]) # X-axis representing the genders to compare
yPoints = np.array([25, 45]) # Y-axis representing numbers per gender.

plt.bar(xPoints, yPoints) # Create bar graph by just passing the data for x-axis and y-axis.
plt.title("Number of Boys and Girls in Class")

plt.show()