class Coordenada:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def distancia(self, otra_coordenada):
		x_diff = (self.x - otra_coordenada.x)**2
		y_diff = (self.y - otra_coordenada.y)**2

		return (x_diff - y_diff)**0.5

if __name__ == '__main__':
	coord_1 = Coordenada(2, 15)
	coord_2 = Coordenada(5, 20)

	distancia = coord_1.distancia(coord_2)

	print(f"La distancia entre ({coord_1.x}, {coord_1.y}) y ({coord_2.x}, {coord_2.y}) es {abs(distancia)}")
	