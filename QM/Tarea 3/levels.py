import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.insert(0, '../Formatter')
import minipy_formatter as MF
MF.Format().rcUpdate()
colors = MF.Colors(("blue", "#0033ff"))

# Probability graphs
fig, ax = plt.subplots(figsize=(10, 7))

omega = 1.5
t = np.linspace(0, 2 * np.pi, 10000)
p_1 = (np.cos(omega * t / 2))**2 # Starts at b
p_2 = (np.sin(omega * t / 2))**2 # Starts at e

ket_b = r"\left| b \right\rangle"
ket_e = r"\left| e \right\rangle"
ket_p = r"\left| \psi_0 \right\rangle"
braket = r"\left| \left\langle \psi(t) \right| b \right\rangle |^2"
ax.set(title="Distribuciones de probabilidad en el tiempo\n para sistema de dos niveles",
	xlabel="Tiempo ($t$)", ylabel=rf"Probabilidad: ${braket}$")
ax.plot(t, p_1, label=f"${ket_p} = {ket_b}$")
ax.plot(t, p_2, label=f"${ket_p} = {ket_e}$")
ax.axhline(0.5, ls=':', color='#888')
ax.axvline(np.pi / omega, label="$t = \pi / \Omega$", ls='--', color='black')
ax.axvline(2 * np.pi / omega, label="$t = 2 \pi / \Omega$", ls='-.', color='black')
ax.legend()

plt.savefig("dos_niveles.png", dpi=200)
plt.show()
