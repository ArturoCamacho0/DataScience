def fibonacci(n):
	if n == 0 or n ==1:
		return 1

	return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('Ingresa un número: '))

print(f'La recursividad del número {n} es {fibonacci(n)}')