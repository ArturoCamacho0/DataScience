# Diccionarios: Son como las listas, pero se accede a traves de llaves, no tienen un orden interno y pueden iterarse
my_dict = {
	'Arturo': 21,
	'Josef': 16,
	'Juan': 18
}

print(my_dict)

# Acceder a traves de la llave
print(my_dict['Arturo'])

# Si no existe la llave en el diccionario, podemos utilizar la función get en el que el segundo parametro devolverá un valor por defecto
print(my_dict.get('Eli', 30))

# Agregar una nueva llave en el diccionario
my_dict['Jorge'] = 50
print(my_dict)

# Borrar una llave del diccionario
del my_dict['Josef']
print(my_dict)

# Iterar el diccionario por llaves
for llave in my_dict.keys():
	print(llave)

# Iterar el diccionario por valores
for valor in my_dict.values():
	print(valor)

# Iterar el diccionario por ambos
for llave, valor in my_dict.items():
	print(llave, valor)

# Saber si existe un valor en el diccionario
print('David' in my_dict)