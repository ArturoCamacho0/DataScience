# Pruebas de caja de cristal
""" Se basan en el flujo del programa
Prueba todos los caminos posibles de una función. Ramificaciones, bucles y recursion
Regression testing o mocks
Se realizan cuando el código ya se conoce """

import unittest

def es_mayor_de_edad(edad):
	if edad >= 18:
		return True
	else:
		return False

class CristalTest(unittest.TestCase):
	# Función para testear la primera posibilidad
	def test_es_mayor_de_edad(self):
		edad = 20

		resultado = es_mayor_de_edad(edad)

		self.assertEqual(resultado, True)

		# Función para testear función con la segunda posibilidad
		def test_es_menor_de_edad(self):
			edad = 15

			resultado = es_menor_de_edad(edad)

			self.assertEqual(resultado, False)

# Comparar si se cumplió el test
if __name__ == '__main__':
	unittest.main()