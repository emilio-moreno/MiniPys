import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.insert(0, '../Formatter')
import minipy_formatter as MF
MF.Format().rcUpdate()
colors = MF.Colors(("blue", "#0033ff"))

# Bound to delta
fig, ax = plt.subplots(figsize=(10, 7))

def f(x, A):
	return np.sqrt(A) * np.e**(-abs(x) * A)
x = np.linspace(-10, 10, 10000)

for A in [1, 2, 2.5, 3]:
	E = -A**2 / 2
	plt.plot(x, f(x, A) + E, label=f'$\\lambda = {A}$')
plt.axhline(0, color='#aaa')
plt.vlines(0, ymin=-4.5, ymax=0, color='#aaa', label='$V(x)$')
ax.set(title="Estado ligado al pozo de delta de Dirac\npara distintas $\\lambda$",
	xlabel='Posición ($x$)', ylabel=r'Amplitud de probabilidad ($\psi_{\lambda}(x) + E_{\lambda}$)')
ax.legend()

plt.savefig("pozo_delta.png", dpi=200)
plt.show()