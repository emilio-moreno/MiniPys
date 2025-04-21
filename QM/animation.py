import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.set(xlim=(min(x), max(x)), ylim=(-2, 2))
animated_plot, = ax.plot([], [])

def update(frame):
	animated_plot.set_data(x -  frame, y)

	return animated_plot

animation = FuncAnimation(fig, func=update, frames=len(x), interval=30)


plt.show()