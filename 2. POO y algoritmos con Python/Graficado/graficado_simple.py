# Para gráficar podemos utilizar la librería Bokeh
"""
Desde bokeh en el apartado de plotting vamos a importar:
figure que nos sirve para mostrar la gráfica en la ventana
output_file para determinar el nombre del archivo del output
show para generar un servidor para mostrar el archivo html en el browser
"""
from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
	# Asignamos el nombre del archivo
	output_file('graficado_simple.html')
	# Creamos la figura
	fig = figure()

	# Damos los valores para X y Y
	valores = int(input('Ingresa cuantos valores quieres graficar: '))
	x_vals = list(range(valores))
	y_vals = []

	for x in x_vals:
		val = int(input(f'Valor de Y para el valor { x } en el eje X: '))
		y_vals.append(val)

	# Creamos las líneas para visualizarlas
	fig.line(x_vals, y_vals, line_width = 2)
	# Mostramos la gráfica
	show(fig)