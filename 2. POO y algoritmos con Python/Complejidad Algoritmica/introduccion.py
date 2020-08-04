import time
""" Para optimizar de mejor manera nuestros programas, medir el tiempo de ejecución
de los algoritmos es una muy buena práctica que nos ayudará a saber cuál de todos
se ajusta mejor a lo que queremos realizar, y así ahorrarnos mucho tiempo de ejecución. """

# Implementamos una función para sacar el factorial de un número con un ciclo
def factorial(n):
	respuesta = 1

	while n > 1:
		respuesta *= n
		n -= 1

	return respuesta


# Implementamos la función para sacar un factorial de forma recursiva
def factorial_recursivo(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n - 1)


if __name__ == '__main__':
	n = 1000

	# Medimos el tiempo de ejecucion del ciclo
	comienzo = time.time()
	factorial(n)
	final = time.time()

	print('El ciclo tardó', final - comienzo)

	# Medimos el tiempo de ejecución de recursividad
	comienzo2 = time.time()
	factorial_recursivo(n)
	final2 = time.time()

	print('La recursividad tardó',final2 - comienzo2)

# El tiempo es una medida muy inestable, puede variar la respuesta