import matplotlib.pyplot as plt
import numpy as np
from sympy.physics.hydrogen import R_nl
from sympy.abc import r
from sympy.utilities.lambdify import lambdify
# Sympy uses R_nl with a0 = 1.

r_sym = r

def numpy_R_nl(n, L, Z=1):
	return lambdify(r_sym, R_nl(n, L, r_sym, Z), 'numpy')

plt.rcParams.update({"font.family": "Times New Roman", "mathtext.fontset": "cm", "font.size": 9, "lines.linewidth": 1})

r = np.linspace(0, 5, 1000) # a0

aspect = 2
fig, ax = plt.subplots(figsize=(aspect * 3.54, 3.54), dpi=600)

ax.plot(r, numpy_R_nl(1, 0, Z=2)(r), label="$R_{1s}^{Z=2}$")
ax.plot(r, numpy_R_nl(2, 0, Z=1)(r), label="$R_{2s}^{Z=1}$")
ax.plot(r, numpy_R_nl(2, 1, Z=1)(r), label="$R_{2p}^{Z=1}$")
ax.set(title='Hydrogenic radial functions', xlabel="Radial distance $r$ [$a_0$]", ylabel="$R_{nl}^Z$")
ax.legend()

txt="Note the reduced overlap between $R_{2p}^{Z=1}$ and $R_{1s}^{Z=2}$ compared to $R_{2s}^{Z=1}$ and $R_{1s}^{Z=2}$."
plt.figtext(0.5, 0.05, txt, wrap=True, horizontalalignment='center', fontsize=8)

plt.subplots_adjust(bottom=0.25)
plt.savefig("3-6-a.png")
# plt.show()

