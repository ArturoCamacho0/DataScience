# Ley de la suma
"""
O(x) + O(x) = O(x + x) = O(2x) = O(x)
Esta función crece de manera lineal dependiendo del valor de x
"""
def suma_f(x):
	for i in range(x):
		print(i)

	for i in range(x):
		print(i)


# Ley de la multiplicación
"""
O(x) * O(x) = O(x * x) = 0(x^2)
Esta función crece de manera cuadrática
"""
def multiplicacion_f(x):
	for i in range(x):
		for j in range(x):
			print(i, j)


# Recursividad multiple
# Algorítmo de Fibonacci
"""
O(2^x)
Aquí tenemos un crecimiento exponencial
"""
def fibonacci(x):
	if x == 0 or x == 1:
		return 1

	return fibonacci(x - 1) + fibonacci(x - 2)