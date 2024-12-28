import matplotlib.pyplot as plt
import numpy as np


def rect(t, tau, a):
	t = t % tau
	return np.ones(len(t)) * (t < (tau / a))


def rect_fourier(t, n, tau, a):
	series = 1 / a * np.ones(len(t))
	# Angular frequency
	w = 2 * np.pi / tau
	for m in range(1, n):
		arg1 = m * (2 * np.pi / a - w * t)
		arg2 = m * w * t
		series += (1 / (m * np.pi)) * (np.sin(arg1) + np.sin(arg2))

	return series


def graph(t, min_t, max_t, ns, tau, a):
	# Format
	update_dict = {'font.family': 'Times New Roman'}
	plt.rcParams.update(update_dict)
	xticks = np.arange(min_t, max_t, tau)

	# Plots
	fig, axs = plt.subplots(len(ns))
	for ax, n in zip(axs, ns):
		ax.plot(t, rect(t, tau, a), color = '#300', label='Onda cuadrada')
		ax.plot(t, rect_fourier(t, n, tau, a), 'r', alpha = 0.7, label=f"Serie con {n =}")
		
		ax.set(ylabel = "Amplitud (m)", xticks=xticks)
		ax.grid(True, linestyle='--', color='#bbb')
		ax.legend(loc=1, fontsize=8)

	axs[-1].set(xlabel="Tiempo (s)")
	fig.suptitle('Serie de Fourier para una onda cuadrada\ncon distinto número de términos (n)',
				fontsize=15)
	plt.subplots_adjust(hspace=0.25)
	plt.savefig('Ejercicio 3.pdf')


def main():
	tau = 1
	a = 5
	min_t = -5
	max_t = 5
	t = np.linspace(min_t, max_t, 10000)
	ns = [5, 15, 30]

	graph(t, min_t, max_t, ns, tau, a)


if __name__ == '__main__':
	main()