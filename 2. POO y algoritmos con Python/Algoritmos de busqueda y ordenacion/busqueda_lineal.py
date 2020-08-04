import random

# BUSQUEDA LINEAL
""" La busqueda lineal nos permíte buscar un elemento pasando de uno en uno hasta encontrarlo,
la cosa mala es que el elemento puede encontrarse en el último punto de donde lo buscamos """
def busqueda_lineal(lista, objetivo):
	match = False

	for elemento in lista: # O(n)
		if elemento == objetivo:
			match = True
			break

	return match


if __name__ == '__main__':
	tamano = int(input('Tamaño de la lista: '))
	objetivo = int(input('Número que se quiere encontrar: '))

	lista = [random.randint(0, 100) for i in range(tamano)]

	print(lista)

	encontrado = busqueda_lineal(lista, objetivo)

	print(f'El elemento {objetivo} {"si existe" if encontrado else "no existe"} en la lista')