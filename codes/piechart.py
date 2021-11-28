# This shows how to create pie charts.

import numpy as np
import matplotlib.pyplot as plt

percents = np.array([75, 15, 10]) # Percents of the game choices
choices = np.array([
	"Mobile Legends: Bang Bang", 
	"League of Legends: Wild Rift", 
	"Arena of Valor"
]) # Game choices

plt.pie(percents, labels = choices) # Create pie chart with the `choices` as the label per data
plt.title("Mobile MOBA Game Preference")

plt.show()