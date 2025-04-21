import matplotlib.pyplot as plt
import sys
import numpy as np
from scipy.special import lambertw
sys.path.insert(0, '../Formatter')
import minipy_formatter as MF
MF.Format().rcUpdate()


# a, b, k = 1, 1, 1
def DGas(v, T):
	return np.e**(-1 / (v * T)) * T / (v - 1)

def idealGas(v, T):
	return T / v

def DGasTv(P, v):
	return 1 / (v * lambertw(1 / (P * v * (v - 1))))

def idealGasTv(P, v):
	return P * v


x = np.linspace(1.001, 500, int(1E5))
X = np.linspace(0.001, 500, int(1E5))

fig, axs = plt.subplot_mosaic([['Pv'], ['PT'], ['Tv']], dpi=350, figsize=(10, 12))
fig.suptitle("Gas de Dieterici vs Gas Ideal")

# Pv
for T in [5, 10, 20, 30, 50]:
	if T == 50:
		axs['Pv'].plot(x, DGas(x, T), color='r', label='Gas de Dieterici')
		axs['Pv'].plot(X, idealGas(X, T), color='b', label='Gas ideal')
	else:
		axs['Pv'].plot(x, DGas(x, T), color='r')
		axs['Pv'].plot(X, idealGas(X, T), color='b')
axs['Pv'].set(xlim=[0, 10], ylim=[-1, 70], title='Diagrama $Pv$',
			  xlabel='Volumen ($v$)', ylabel='Presión ($P$)')
axs['Pv'].axvline(1, color='k', linestyle='--', label='$v = b$')
axs['Pv'].legend()

# Tv
for P in [5, 10, 20, 30, 50]:
	if P == 50:
		axs['Tv'].plot(x, DGasTv(P, x), color='r', label='Gas de Dieterici')
		axs['Tv'].plot(X, idealGasTv(P, X), color='b', label='Gas ideal')
	else:
		axs['Tv'].plot(x, DGasTv(P, x), color='r')
		axs['Tv'].plot(X, idealGasTv(P, X), color='b')
axs['Tv'].set(xlim=[0, 10], ylim=[-1, 70], title='Diagrama $Tv$',
			  xlabel='Volumen ($v$)', ylabel='Temperatura ($T$)')
axs['Tv'].axvline(1, color='k', linestyle='--', label='$v = b$')
axs['Tv'].legend()

# PT
X = np.linspace(0, 1, int(1E5))
for V in [2, 5, 8]:
	if V == 2:
		axs['PT'].plot(X, DGas(V, X), color='r', label='Gas de Dieterici')
		axs['PT'].plot(X, idealGas(V, X), color='b', label='Gas ideal')
	else:
		axs['PT'].plot(X, DGas(V, X), color='r')
		axs['PT'].plot(X, idealGas(V, X), color='b')
axs['PT'].set(title='Diagrama $PT$',
			  xlabel='Temperatura ($T$)', ylabel='Presión ($P$)')
axs['PT'].legend()

plt.subplots_adjust(hspace=0.5)
plt.savefig('dieterici.png')
