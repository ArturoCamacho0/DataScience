class Automovil:
	def __init__(self, modelo, marca, color):
		self.modelo = modelo
		self.marca = marca
		self.color = color
		self._estado = 'en reposo'
		self._motor = Motor(cilindros = 4)

	def acelerar(self, tipo = 'despacio'):
		if tipo == 'rapido':
			self._motor.inyecta_gasolina(10)
		else:
			self._motor.inyecta_gasolina(3)

		self._estado = 'en marcha'

class Motor:
	def __init__(self, cilindros, tipo = 'gasolina'):
		self.cilindros = cilindros
		self.tipo = tipo
		self._temperatura = 0

	def inyecta_gasolina(self, cantidad):
		pass

class Pasajeros:
	def __init__(self):
		self.capacidad = 5

	def cupo(self, pasajeros):
		self.pasajeros = 4
		
		if self.pasajeros >= self.capacidad:
			print('La capacidad ha llegado a su límite')
		elif self.pasajeros <= 0:
			print('No hay pasajeros')
		else:
			print('Nos vamos!')
			automovil = Automovil(2010, 'BMW', 'Negro')
			automovil._estado = 'en marcha'