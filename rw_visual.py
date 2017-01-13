import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a rand walk, and plot the points.
rw = RandomWalk()
rw.fill_walk()

plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()