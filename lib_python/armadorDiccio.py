############################################################################
# Armador de diccionarios

class diccio:


	__init__( self , listadoTuplas = [(),(),()], *orden):
		"""Esta funcion genera diccionarios en base a los niveles que se le da. En orden van numeros enteros correspondiente al numero de posicion en la tupla. OJO: El primer elemento de la tupla es CERO 0"""

		self.listadoTuplas = listadoTuplas
		self.orden = orden

		# Primero creare el diccionario, luego lo llenare
		respuesta = {}

		# crea el diccionario
		self.diccionario = creacion( self.listadoTuplas , self.orden )

		# llena el diccionario
		self.diccionario = llenado( self.listadoTuplas , self.orden )


	def creacion(self, listadoTuplas = [(),(),()], *orden ):


	def llenado(self, listadoTuplas = [(),(),()], *orden ):


##################### REVISAR #######################################
