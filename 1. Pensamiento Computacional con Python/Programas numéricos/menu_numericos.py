import os

# Ennumeración exhaustiva
def enumeracion(objetivo):
	respuesta = 0

	print('ENNUMERACIÓN EXHAUSTIVA\n')

	while respuesta**2 < objetivo:
		respuesta += 1

	if respuesta**2 == objetivo:
		print(f'La raíz cuadrada de {objetivo} es {respuesta}')
	else:
		print(f'{objetivo} no tiene una raíz exacta')

# Aproximación numerica
def aproximacion(objetivo):
	epsilon = 0.01
	paso = epsilon**2
	respuesta = 0

	print('APROXIMACIÓN NUMÉRICA\n')

	while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
		respuesta += paso

	if abs(respuesta**2 - objetivo) >= epsilon:
		print(f'No se encontró la raíz cuadrada de {objetivo}')
	else:
		print(f'La raíz cuadrada de {objetivo} es {respuesta}')

# Busqueda binaria
def binaria(objetivo):
	epsilon = 0.01
	bajo = 0.0
	alto = (bajo + objetivo) / 2
	respuesta = 0

	print('BUSQUEDA BINARIA\n')

	while abs(respuesta**2 - objetivo) >= epsilon:

		if respuesta**2 < objetivo:
			bajo = respuesta
		else:
			alto = respuesta

		respuesta = (alto + bajo) / 2

	print(f'La raíz de {objetivo} es {respuesta}')

# Menú
op = 1

while op > 0 and op < 4:
	os.system('cls')

	print("""\n---------------------- MENÚ DE PROGRAMAS NUMÉRICOS ----------------------------------\n
		1. Ennumeración exhaustiva\n
		2. Aproximación numérica\n
		3. Busqueda binaria\n
		Presione cualquier otro número para salir.
	\n------------------------------------------------------------------------------------\n""")

	op = int(input('\nEscriba la opción por la cuál buscará su raíz: '))

	objetivo = int(input('\nIngrese el número del cuál desea sacar su raíz: '))
	print('\n\n')

	os.system('cls')
	if op == 1:
		enumeracion(objetivo)
		input('\n\nPresiona enter para volver al menú')
		os.system('cls')
	elif op == 2:
		aproximacion(objetivo)
		input('\n\nPresiona enter para volver al menú')
		os.system('cls')
	elif op == 3:
		binaria(objetivo)
		input('\n\nPresiona enter para volver al menú')
		os.system('cls')
	else:
		print('Saliendo...')