# Pruebas de caja negra

""" Se basan en la especificacion de la función o el programa
Prueba inputs y valida outputs
Unit Testing o Integration Testing"""

# Importamos la libreria de unittest para hacer pruebas unitarias
import unittest

# Función para hacer la suma
def suma(num1, num2):
	return num1 + num2

# Creamos la clase para hacer el test
class CajaNegraTest(unittest.TestCase):
	# Creamos la función para testear la función de suma
	def test_suma_dos_positivos(self):
		num1 = 10
		num2 = 5

		resultado = suma(num1, num2)

		# Asegurar el resultado
		self.assertEqual(resultado, 15)

	# Creamos la función para testear la función de suma de negativos
	def test_suma_dos_negativos(self):
		num1 = -10
		num2 = -7

		# Asegurar el resultado
		resultado = suma(num1, num2)

		# Asegurar el resultado
		self.assertEqual(resultado, -17)

# Corremos el main
if __name__ == '__main__':
	unittest.main()