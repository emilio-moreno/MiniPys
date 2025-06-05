from scipy.special import assoc_laguerre, genlaguerre
import matplotlib.pyplot as plt
import numpy as np
from math import factorial
rc_update = {'font.family': 'Times New Roman', 'mathtext.fontset': 'cm'}
plt.rcParams.update(rc_update)

r = np.linspace(0, 50, 1000)
fig, ax = plt.subplots()

for n in range(4, 5):
	for L in range(0, n):
		rho = 2 * r / n # a0, Z = 1
		normalization = np.sqrt((2 / n)**3 * factorial(n - L - 1) / (2 * n * factorial(n + 1)))
		Rnl = normalization * np.e**(-rho / 2) * rho**L * assoc_laguerre(rho, n=n - L - 1, k=2 * L + 1)
		ax.plot(r, Rnl, label=f"$R_{{{n,L}}}$")
ax.set(xlabel=r'Radio ($\rho$)', ylabel=r'$R_{n,l}$ (arb.) con $a_0, Z = 1$',
	   title='Funciones radiales para un átomo hidrogenoide con $n = 4$')
ax.legend()
plt.savefig('radiales_n=4.png')
plt.show()
