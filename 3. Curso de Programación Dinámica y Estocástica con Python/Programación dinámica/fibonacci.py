import sys

# Función de fibonacci de manera recursiva
def fibonacci_recursivo(n):
	if n == 0 or n == 1 or n == 2:
		return 1

	return fibonacci(n - 1) + fibonacci(n - 2)

# Función de fibonacci de manera dinámica
def fibonacci_dinamico(n, memo = {}):
	if n == 0 or n == 1 or n == 2:
		return 1

	# Evaluamos memo para ver si existe en el diccionario el valor
	try:
		return memo[n]

	# Si no se captura el error y seguímos con el programa
	except KeyError:
		# Utilizamos recursividad, pero ahora estámos guardando en un diccionario los resultados
		resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
		memo[n] = resultado

		# Devolvemos el resultado
		return resultado

if __name__ == '__main__':
	# Así podemos asignar el límite de recursiones que se pueden hacer
	sys.setRecursionlimit(10002)

	n = int(input('Ingresa un número: '))

	fibonacci = fibonacci_dinamico(n)

	print(f'El resultado fibonacci de {n} es {fibonacci}')