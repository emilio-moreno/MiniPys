import cplot
from scipy.special import gamma
import matplotlib.pyplot as plt
import sys
import numpy as np
sys.path.insert(0, '../formatter')
import minipy_formatter as MF
MF.Format().rcUpdate()

# fig, ax = plt.subplots()
# x = np.linspace(-6, 1, 10000)

# for i, y in enumerate(x):
# 	if abs(gamma(y)) > 10:
# 		x[i] = np.nan

# ax.plot(x, gamma(x), color='red')
# for i in range(-6, 1):
# 	ax.axvline(i, color='#999', linestyle='--')

# ax.set(title='$\\Gamma(z)$', xlabel='$x$', ylabel='$\\Gamma(z)$')
# ax.set_ylim(-10, 10)
# plt.savefig("real_gamma.png", dpi=300)

# plt = cplot.plot(gamma, (-4, 4, 400), (-4, 4, 400))
# plt.suptitle('Argumento y valor absoluto de $\\Gamma(z)$')
# plt.savefig("complex_gamma.png", dpi=300)

plt = cplot.plot_arg(gamma, (-4, 4, 400), (-4, 4, 400))
plt.suptitle('Argumento de $\\Gamma(z)$')
plt.savefig("complex_gamma_arg.png", dpi=300)