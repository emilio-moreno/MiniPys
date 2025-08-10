import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import physical_constants, eV, m_e, hbar, c, h, e, epsilon_0
from scipy.optimize import curve_fit
from uncertainties import ufloat, umath

# Constants
a0, _, _ = physical_constants["Bohr radius"] # m
E1 = hbar**2 / (m_e * 2 * a0**2) / eV
print(e**2 / (8 * np.pi * epsilon_0 * a0) / eV)

# Data
wavenumbers = 100 * np.array([38541, 39299, 39795, 40137, 40383, 40566, 40706, 40814]) # m^-1
relative_qnum = np.arange(0, len(wavenumbers))
# ΔE is of the form E1 / 3*^2 - E1 / n*^2.
ΔE = h * c * wavenumbers / eV # eV

# Fitting
f = lambda n_star, E3, n0_star: E3 - E1 / (n_star + n0_star)**2

popt, pcov = curve_fit(f, relative_qnum, ΔE, p0=[ΔE[-1], 3])
perr = np.sqrt(np.diag(pcov))

E3 = ufloat(popt[0], perr[0])
n3_star = umath.sqrt(E1 / E3)
n0_star = ufloat(popt[1], perr[1])
qnum = relative_qnum + n0_star.n

print(f"E3 = {E3} eV, n0* = {n0_star}, 3* = {n3_star}, δ₃ = {3 - n3_star}")


# Plots
plt.rcParams.update({"font.family": "Times New Roman", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(dpi=300)
ax.plot(qnum, E3.n - E1 / qnum**2, 'r')
ax.scatter(qnum, ΔE, marker='x', c='#b33')
ax.set(title="Energy differences for ultraviolet series for ground state of Sodium",
	   xlabel="Corrected quantum number ($n*$)", ylabel="$ΔE$ from ground state [eV]")
plt.savefig("ultraviolet_Na.png")
plt.show()
