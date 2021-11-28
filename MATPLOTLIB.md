
# Matplotlib Guide
This is a guide regarding Matplotlib created by Arthur Tristan M. Ramos to be presented in 2021 Mini Workshop Series: Into Coding: Introduction to Python Libraries.

## Matplotlib
Matplotlib is a low level graph plotting library serving as a visualization utility.

## Pyplot
Pyplot is a submodule of Matplotlib that handles the plotting functionalities.

## Importing Pyplot and NumPy
For our graph programs to work, we need to import Pyplot and NumPy.

```
import matplotlib.pyplot as plt
import numpy as np
```

## Plotting
To plot a line, we need an array for the x (horizontal) points and the y (vertical points). We use *plot()* to plot the x and y points then we use *show()* to display the graph.

```
xPoints = np.array([1, 10])
yPoints = np.array([10, 50])

plt.plot(xPoints, yPoints)
plt.show()
```

## Markers
We call an optional keyword argument *marker* in plot() to show a point in the graph especially in line graphs.

```
yPoints = np.array([10, 20, 30, 40, 50])

plt.plot(yPoints, marker="o") # Dots
plt.show()
```

## Line Graphs
This is how we display line graphs. We can add an optional keyword argument in plot() called *linestyle* wherein we specify in a string if we want the line to be dotted or dashed.

```
# Dotted

yPoints = np.array([10, 20, 30, 40, 50])

plt.plot(yPoints, linestyle="dotted")
plt.show()
```

```
# Dashed

yPoints = np.array([10, 20, 30, 40, 50])

plt.plot(yPoints, linestyle="dashed")
plt.show()
```

## Labels
We use the method *xlabel()* to label the x-axis while *ylabel()* to label the y-axis.

```
xPoints = np.array(["Mon", "Tue", "Wed", "Thu", "Fri"])
yPoints = np.array([100, 150, 300, 250, 575])

plt.plot(xPoints, yPoints)
plt.xlabel("Day")
plt.ylabel("Total Sales")

plt.show()
```

## Title of the Graph
We use the method *title()* to display the title of the graph.

```
xPoints = np.array(["Mon", "Tue", "Wed", "Thu", "Fri"])
yPoints = np.array([100, 150, 300, 250, 575])

plt.plot(xPoints, yPoints)
plt.title("Weekday Sales of Corndogs")
plt.xlabel("Day")
plt.ylabel("Total Sales")

plt.show()
```

## Grid
We call the *grid()* method to add guidelines to the graph.

```
xPoints = np.array(["Mon", "Tue", "Wed", "Thu", "Fri"])
yPoints = np.array([100, 150, 300, 250, 575])

plt.plot(xPoints, yPoints)
plt.xlabel("Day")
plt.ylabel("Total Sales")

plt.grid()

plt.show()
```

```
# Only show guidelines of x-axis using the optional `axis` parameter.

xPoints = np.array(["Mon", "Tue", "Wed", "Thu", "Fri"])
yPoints = np.array([100, 150, 300, 250, 575])

plt.plot(xPoints, yPoints)
plt.xlabel("Day")
plt.ylabel("Total Sales")

plt.grid(axis="x")

plt.show()
```

## Bar Graph
We use the *bar()* method to display a bar graph.

```
xPoints = np.array(["Male", "Female"])
yPoints = np.array([25, 45])

plt.bar(xPoints, yPoints)
plt.title("Number of Boys and Girls in Class")

plt.show()
```

## Pie Chart
We use the *pie()* method to display a pie chart. We use optional keyword argument *labels* to show labels of the data compared to each other.

```
yPoints = np.array([75, 15, 10])
choices = np.array([
	"Mobile Legends: Bang Bang", 
	"League of Legends: Wild Rift", 
	"Arena of Valor"
])

plt.pie(yPoints, labels = choices)
plt.title("Mobile MOBA Game Preference")

plt.show()
```
> Written with [StackEdit](https://stackedit.io/).
