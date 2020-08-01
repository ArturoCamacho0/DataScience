class Trabajador:
	def __init__(self, nombre, puesto):
		self.nombre = nombre
		self.puesto = puesto

	def mostrar_trabajador(self):
		return f'El trabajador {self.nombre} tiene el puesto de {self.puesto}'


class Carpintero(Trabajador):
	def __init__(self, nombre, puesto = 'carpintero'):
		super().__init__(nombre, puesto)


class Plomero(Trabajador):
	def __init__(self, nombre, puesto = 'plomero'):
		super().__init__(nombre, puesto)


class Maestro(Trabajador):
	def __init__(self, nombre, puesto = 'maestro'):
		super().__init__(nombre, puesto)


if __name__ == '__main__':
	carpintero = Carpintero('Alan')
	print(carpintero.mostrar_trabajador())

	plomero = Plomero('Juan')
	print(plomero.mostrar_trabajador())

	maestro = Maestro('Alexis')
	print(maestro.mostrar_trabajador())