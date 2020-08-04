import random

def busqueda_binaria(lista, comienzo, final, objetivo):
	if comienzo > final:
		return False

	medio = (comienzo + final) // 2

	if lista[medio] == objetivo:
		return True
	elif lista[medio] < objetivo:
		return busqueda_binaria(lista, (medio + 1), final, objetivo)
	else:
		return busqueda_binaria(lista, comienzo, (medio - 1), objetivo)


if __name__ == '__main__':
	tamano = int(input('Tamaño de la lista: '))
	objetivo = int(input('Número que se quiere encontrar: '))

	lista = sorted([random.randint(0, 100) for i in range(tamano)])

	print(lista)

	encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

	print(f'El elemento {objetivo} {"si existe" if encontrado else "no existe"} en la lista')
