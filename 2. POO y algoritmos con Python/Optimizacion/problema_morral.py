""" El problema del morral nos plantea que tenemos un morral en donde
debemos meter todos los objetos posibles sin pasar la capacidad del morral
generando el máximo valor posible dentro """

# Primero definimos nuestra función
def morral(morral_tam, pesos, valores, n):
	# Ahora comprobamos que no se nos hayan acabado los objetos o el tamaño del morral
	if n == 0 or morral_tam == 0:
		return 0

	# Aquí paramos si el peso excede el tamaño del morral 
	if pesos[n - 1] > morral_tam:
		return morral(morral_tam, pesos, valores, n - 1)

	# Tomamos una decision, si lo metemos agarramos la suma de los valores y se ejecuta la recursividad
	# Si no lo escogemos se pasa al siguiente objeto
	return max(valores[n - 1] + morral(morral_tam - pesos[n - 1], pesos, valores, n - 1),
			   morral(morral_tam, pesos, valores, n - 1))




if __name__ == '__main__':
	# Definimos el tamaño y asignamos los valores por un input para el usuario
	tam_valores = int(input('Ingrese el número de valores que va a introducir: '))
	print('El peso máximo que puede ocupar el morral es de 50\n')
	valores = []
	pesos = []
	morral_tam = 50

	for i in range(tam_valores):
		valores.append(int(input(f'Ingrese el valor del objeto {i + 1}: ')))
		pesos.append(int(input(f'Ingrese el peso del objeto {i + 1}: ')))
		print('\n')

	n = len(valores)

	# Llamamos y mostramos el resultado
	resultado = morral(morral_tam, pesos, valores, n)
	print('El valor máximo es de', resultado)