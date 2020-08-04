import random

# MERGE SORT
"""
Este algoritmo crea sublistas hasta llegar a una lista con un sólo elemento,
esas sublistas se compararán entre sí de menos a más hasta combinar todas
ya ordenadamente
"""
def merge_sort(lista):
	if len(lista) > 1:
		medio = len(lista) // 2
		izquierda = lista[:medio]
		derecha = lista[medio:]
		
		#llamada recursiva
		izquierda = merge_sort(izquierda)
		derecha = merge_sort(derecha)
		
		#iteradores para recorrer las dos sublistas
		i = 0
		j = 0
		#Iterador para la lista principal
		k = 0
		
		while i< len(izquierda) and j < len(derecha): #mientras podamos seguir comparando
			if izquierda[i] < derecha[j]:
			    lista[k] = izquierda[i]
			    i += 1
			else:
			    lista[k] = derecha[j]
			    j += 1
			k+= 1
		#copiar los pedazos de las listas que quedaron
		while i < len(izquierda):
			lista[k] = izquierda[i]
			i+=1
			k += 1
		while j < len(derecha):
			lista[k] = derecha[j]
			j += 1
			k += 1
		print(f'izquierda  {izquierda}. derecha  {derecha}')
		print(lista)
		print('--' * 30)

	return lista

if __name__ == '__main__':
	tamano = int(input('Tamaño de la lista: '))

	lista = [random.randint(0, 100) for i in range(tamano)]

	print(lista)
	print('-' * 20)

	ordenado = merge_sort(lista)

	print('Lista ordenada', ordenado)