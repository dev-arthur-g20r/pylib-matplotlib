# This shows how to create line graphs, add labels of axes in the graph and display title of the graph.

import numpy as np
import matplotlib.pyplot as plt

xPoints = np.array(["Mon", "Tue", "Wed", "Thu", "Fri"]) # X-axis representing days
yPoints = np.array([100, 150, 300, 250, 575]) # Y-axis representing sales of that day

plt.plot(xPoints, yPoints) # This automatically creates a line graph.

plt.title("Sales of the Week") # Display the overall meaning of the graph.

plt.xlabel("Day") # Indicate that the data represented in horizontal axis is days.
plt.ylabel("Total Sales") # Indicate that the data represented in vertical axis is sales of the day.

plt.show()