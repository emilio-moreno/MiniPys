import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.insert(0, '../Formatter')
import minipy_formatter as MF
MF.Format().rcUpdate()

colors = MF.Colors(("blue", "#0033ff"))

t = np.linspace(0, 2 * np.pi, int(1E6))

def r(t, A):
	return A / (np.sin(t / 2))**2

def R(t, A, U):
	sin = np.sin(t)
	sin_2 = np.sin(t / 2)
	return ((-A * sin_2 + np.sqrt(A**2 * sin_2 + 4 * U * A * sin)) / (2 * U * sin))**2

def R_minus(t, A, U):
	sin = np.sin(t)
	sin_2 = np.sin(t / 2)
	return ((-A * sin_2 - np.sqrt(A**2 * sin_2 + 4 * U * A * sin)) / (2 * U * sin))**2

fig, ax = plt.subplots(dpi=150, figsize=(10, 7))#subplot_kw={'projection': 'polar'})

U = 1
As = np.linspace(0, 5, 8)
lightness = np.linspace(-30, 30, 8)
for A, light in zip(As, lightness):
	x = R(t, A, U) * np.cos(t)
	y = R(t, A, U) * np.sin(t)
	#x_minus = R_minus(t, A, U) * np.cos(t) 
	#y_minus = R_minus(t, A, U) * np.sin(t) 
	ax.plot(x, y, label=f'$\\psi_0 = {A:.2f}$', color=colors.blue.light(light))
	#ax.plot(x_minus, y_minus, color=colors.blue.light(light))


ax.plot((0, 1000), (0, 0), color='black')
lims = (-10, 10)
ax.set(title=f"Líneas de corriente para $f(z) = Cz^{{1/2}} + Uz$, ${U = }$", xlim=lims, ylim=lims)
ax.legend()

U = "U=" + str(U).replace('.', '-')
plt.savefig(f"corriente_{U}.png")
plt.show()
