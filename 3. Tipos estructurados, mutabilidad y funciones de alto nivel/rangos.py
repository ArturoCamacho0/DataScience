# Rangos: range(inicio, fin, pasos)
my_range = range(0, 7, 2)

other_range = range(0, 8, 2)

# Igualdad de valores
if my_range == other_range:
	print("Los pasos del rango son iguales")
else:
	print("Los pasos del rango son diferentes")

# Igualdad de objetos
if my_range is other_range:
	print("Son objetos iguales")
else:
	print("Son diferentes objetos")


# Imprimir valores pares del 0 100
for i in range(0, 101, 2):
	print(i)

print("\n")

# Imprimir valores nones del 1 al 99
for i in range(0, 100):
	print(i)