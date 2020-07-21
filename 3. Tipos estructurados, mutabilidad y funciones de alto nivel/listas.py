a = [1, 2, 3]

b = list(a)

print(b)

# LIST COMPREHENSION: Aplicar operaciones a los valores de una secuencia
my_list = list(range(0, 100))
print(my_list)

print("\n")

double = [i * 2 for i in my_list]
print(double)

print("\n")

pares = [i for i in my_list if i%2 == 0]
print(pares)