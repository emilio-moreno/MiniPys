import matplotlib.pyplot as plt
import numpy as np


def rect(t, T, A):
	t = t % T
	positives = A * np.ones(len(t)) * (t < (T / 2))
	negatives = -A * np.ones(len(t)) * ((T / 2) < t) * (t < T)
	return positives + negatives


def rect_fourier(t, n, T, A):
	series = 0
	# Angular frequency
	w = 2 * np.pi / T
	for m in range(1, n):
		if m % 2 == 1:
			arg = m * w * t
			series += 4 * A / np.pi * np.sin(arg) / m
	return series


def graph(t, min_t, max_t, n, T, A):
	# Format
	update_dict = {'font.family': 'Times New Roman', 'mathtext.fontset': 'cm'}
	plt.rcParams.update(update_dict)

	# Plots
	fig, ax = plt.subplots()
	ax.plot(t, rect(t, T, A), color = '#300', label='Onda cuadrada')
	ax.plot(t, rect_fourier(t, n, T, A), 'r', alpha = 0.7, label=f"Serie con {n =}")
	
	ax.set(ylabel = "Amplitud (m)", xlabel="Tiempo (MHz$^{-1}$)")
	ax.grid(True, linestyle='--', color='#bbb')
	ax.legend(loc=1, fontsize=8)

	fig.suptitle(f'Serie de Fourier para onda cuadrada\ncon máxima frecuencia de {n / T:.2f} MHz',
				fontsize=15)
	plt.subplots_adjust(hspace=0.25)
	plt.savefig('Ejercicio 4.pdf')


def main():
	# Fundamental frequency
	w_0 = 3 # MHz
	# Period
	T = 2 * np.pi / w_0
	A = 6
	min_t = -5
	max_t = 5
	t = np.linspace(min_t, max_t, 1000)
	n = 52

	graph(t, min_t, max_t, n, T, A)


if __name__ == '__main__':
	main()