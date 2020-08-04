import random


# BUBBLE SORT
"""
El método de ordenación burbuja nos permíte ordenar la lista de manera lineal,
va buscando uno por uno y si el elemento actual es mayor al que sigue, intercambian su valor
"""
def bubble_sort(lista):
	n = len(lista)

	for i in range(n):
		for j in range(0, n - i - 1):
			if lista[j] > lista[j + 1]: 
				lista[j + 1], lista[j] = lista[j], lista[j + 1]

				# O(n) * O(n) = O(n * n) = O(n^2)

	return lista
		


if __name__ == '__main__':
	tamano = int(input('Tamaño de la lista: '))

	lista = [random.randint(0, 100) for i in range(tamano)]

	print('Lista desordenada', lista)

	ordenado = bubble_sort(lista)

	print('Lista ordenada', ordenado)