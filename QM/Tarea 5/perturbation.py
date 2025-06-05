from scipy.special import assoc_laguerre, genlaguerre
import matplotlib.pyplot as plt
import numpy as np
from math import factorial
rc_update = {'font.family': 'Times New Roman', 'mathtext.fontset': 'cm'}
plt.rcParams.update(rc_update)

omega = np.linspace(0, 0.75, 1000)
E_1 = np.zeros(1000)
E_2 = -np.ones(1000)
E_12 = lambda omega: omega**2
E_22 = lambda omega: -(1 + omega**2)
E_1f = lambda omega: (-1 + np.sqrt(1 + 4 * omega**2)) / 2
E_2f = lambda omega: (-1 - np.sqrt(1 + 4 * omega**2)) / 2
fig, axs = plt.subplot_mosaic([[1, 2]])
axs[1].plot(omega, E_1, label='Cero y primer orden')
axs[1].plot(omega, E_12(omega), label='Segundo orden')
axs[1].plot(omega, E_1f(omega), label='Exacto')

axs[2].plot(omega, E_2, label='Cero y primer orden')
axs[2].plot(omega, E_22(omega), label='Segundo orden')
axs[2].plot(omega, E_2f(omega), label='Exacto')

for ax_label in axs:
	axs[ax_label].legend(fontsize=10)
	axs[ax_label].set(xlabel='Perturbación ($\Omega / \Delta $)', ylabel='Energías ($E(\Omega)$)')
plt.savefig('perturbación.png')
