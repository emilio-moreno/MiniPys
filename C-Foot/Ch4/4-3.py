import numpy as np
from scipy.constants import physical_constants, hbar, m_e, eV
import matplotlib.pyplot as plt

a0, _, _ = physical_constants["Bohr radius"]

E1 = hbar**2 / (2 * m_e * a0**2) / eV

quantum_numbers = np.array([3, 4, 5, 6])
binding_energies = np.array([5.14, 1.92, 1.01, 0.63])
corrected_quantum_numbers = (E1 / binding_energies)**(1/2)
quantum_defects = quantum_numbers - corrected_quantum_numbers

# Assuming same quantum deffect as 6s for 8s
E_8s = E1 / (8 - quantum_defects[-1])**2
E_8s_H = E1 / 8**2

print(f"{quantum_defects = }")
print(f"{E_8s = :.2f} eV")
print(f"{E_8s_H = :.2f} eV")
fig, ax = plt.subplots()
ax.scatter(quantum_numbers, quantum_defects)
plt.show()
