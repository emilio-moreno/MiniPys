'''Wavefunctions for exercise 3.3'''
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
sin = np.sin 
pi = np.pi

plt.rcParams.update({"font.family": "Times New Roman", "mathtext.fontset": "cm"})

L = 1
L_step = 0.05
u_A = lambda x1, x2: np.sqrt(2)/L * (sin(pi*x1/L) * sin(2*pi*x2/L) - sin(pi*x2/L) * sin(2*pi*x1/L))
u_S = lambda x1, x2: np.sqrt(2)/L * (sin(pi*x1/L) * sin(2*pi*x2/L) + sin(pi*x2/L) * sin(2*pi*x1/L))
us = [u_A, lambda x1, x2: u_A(x1, x2)**2, u_S, lambda x1, x2: u_S(x1, x2)**2]


X1, X2 = np.mgrid[0:L:L_step, 0:L:L_step]
fig, axs = plt.subplot_mosaic([["$u_A$", "$u_A^2$"], ["$u_S$", "$u_S^2$"]], subplot_kw={"projection": "3d"})
fig.suptitle("C. Foot - Exercise 3.3.d)")
for u, ax_label in zip(us, axs):
	axs[ax_label].plot_surface(X1, X2, u(X1, X2), lw=1, antialiased=True, cmap=cm.coolwarm)
	axs[ax_label].set(xlabel="$x1$", ylabel="$x2$", title=ax_label)

plt.subplots_adjust(hspace=0.5)
plt.savefig("3-3-d.png")
plt.show()

# From graphs we can tell u_A configuration likes to have particles separated,
# while u_S instead likes to keep them together.