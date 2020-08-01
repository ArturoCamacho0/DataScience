class CasillaDeVotacion:
	def __init__(self, identificador, pais):
		self._identificador = identificador
		self._pais = pais
		self._region = None

	@property
	def region(self):
		return self._region

	@region.setter
	def region(self, region):
		if region in self._pais:
			self._region = region
		else:
			raise ValueError(f'La region {region} no es valida en {self._pais}')


casilla = CasillaDeVotacion(1999, ['México', 'Estado de México'])
casilla.region = 'Puebla'
print(casilla.region)