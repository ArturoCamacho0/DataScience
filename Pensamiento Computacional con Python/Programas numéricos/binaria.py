objetivo = int(input('Ingresa un número: '))
epsilon = 0.001
limite_inf = 0.0
limite_sup = max(1.0, objetivo)
respuesta = (limite_sup + limite_inf) / 2

while abs(respuesta**2 - objetivo) >= epsilon:
	print(f'Bajo = {limite_inf}, Alto = {limite_sup},  Respuesta = {respuesta}')

	if respuesta**2 < objetivo:
		limite_inf = respuesta
	else:
		limite_sup = respuesta

	respuesta = (limite_sup + limite_inf) / 2

print(f'La raíz cuadrada de {objetivo} es {respuesta}')