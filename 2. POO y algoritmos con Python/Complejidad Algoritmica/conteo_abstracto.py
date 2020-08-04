# Una mejor forma de contar el tiempo es por medio de una ecuación matemática
"""

En este caso tenemos un trinomio al cuadrado:
f(x) = 2x^2 + x + 1000

"""

# Aquí definimos la función f(x)
def f(x):
	respuesta = 0

	# Tenemos una constante que es igual a 1000
	for i in range(1000):
		respuesta += 1

	# Después tenemos una variable x simple
	for i in range(x):
		respuesta += x

	""" Y por último al estar dentro de dos ciclos es una variable eleveada al cuadrado, 
		también se está sumando dos veces uno, por lo que surge un producto 2x^2"""
	for i in range(x):
		for j in range(x):
			respuesta += 1
			respuesta += 1

	return respuesta