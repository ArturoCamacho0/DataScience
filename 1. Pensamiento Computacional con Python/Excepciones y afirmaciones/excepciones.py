def divide_elementos_de_lista(litsa, divisor):
	# Intentamos hacer una acción
	try:
		return [i / divisor for i in lista]
	# Tomamos la excepcion en caso de que falle
	except ZeroDivisionError as e:
		return lista

lista = list(range(10))
divisor = 2

print(divide_elementos_de_lista(lista, divisor))