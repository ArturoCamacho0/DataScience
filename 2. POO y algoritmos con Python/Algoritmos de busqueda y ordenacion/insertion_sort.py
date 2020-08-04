import random

# INSERTION SORT
"""
El método por inserción de ordenamiento nos ayuda a ordenar una lista al igual que el bubble,
solo que en este método se crea una sublista donde va guardando los elementos actuales, si el
elemento es menor al valor guardado en la sublista se agrega en el primer indice 
"""
def insertion_sort(lista):
	for indice in range(1, len(lista)):
		valor_actual = lista[indice]
		posicion_actual = indice

		while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
			lista[posicion_actual] = lista[posicion_actual - 1]
			posicion_actual -= 1

		lista[posicion_actual] = valor_actual

	return lista


if __name__ == '__main__':
	tamano = int(input('Tamaño de la lista: '))

	lista = [random.randint(0, 100) for i in range(tamano)]

	print('Lista desordenada', lista)

	ordenado = insertion_sort(lista)

	print('Lista ordenada', ordenado)