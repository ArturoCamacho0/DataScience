# Afirmaciones
""" Programación defensiva
Pueden utilizarse para verificar que los tipos sean correctos en una función
También sirve para debuggear 
assert es una expresión booleana"""

# assert <condición>, <mensaje>

def primera_letra(lista_de_palabras):
	primeras_letras = []

	for palabra in lista_de_palabras:
		try:
			assert type(palabra) == str, f'{palabra} no es str'
			assert len(palabra) > 0, 'No se permiten str vacíos'

			primeras_letras.append(palabra[0])
		except AssertionError as e:
			print(e)

	return primeras_letras

lista = ["Hola", 4, "Adios", False, ""]

print('Las primeras letras validas son: ', primera_letra(lista))