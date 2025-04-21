import matplotlib.pyplot as plt
import sys
import numpy as np
from scipy.special import lambertw
sys.path.insert(0, '../Formatter')
import minipy_formatter as MF
MF.Format().rcUpdate()

x = np.linspace(0.25, 50, int(1E5))

# a, b, k = 1, 1, 1
# R = 10
def cpcv(T, v):
	return 10 * np.e**(- 1 / (T * v)) * (T * v + 1)**2 / (T * (T * v**2 - (v - 1)))

fig, axs = plt.subplot_mosaic([['cpcv']], dpi=350, figsize=(10, 5))
axs['cpcv'].plot(x, cpcv(10, x))
axs['cpcv'].set(title='Gas de Dieterici: $c_P - c_V$', ylim=[9, 12],
			  xlabel='Volumen ($v$)', ylabel='$c_P - c_V$')
axs['cpcv'].axvline(1, color='k', linestyle='--', label='$v = b$')
axs['cpcv'].axhline(10, color='k', linestyle='-.', label='$c_P - c_V = R$')
axs['cpcv'].legend()

plt.savefig('cpcv.png')
#plt.show()
