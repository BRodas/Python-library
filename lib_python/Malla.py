# ARCHIVO ORIENTADO PARA EL TRATAMIENTO DE MALLAS

# Importa la libreria de pyproj
from pyproj import Proj
# Importacion de librerias para matematicas
import math
# Para el tratamiento de conjuntos
from sets import Set


#####################################################################################################################################

def pertenece(x_pintado , y_pintado , ladoCuadradoMetros):
	"""Funcion que indica a que cuadrado pertenecen las coordenadas entregadas"""

	x_cuadricula = int(ladoCuadradoMetros * int(x_pintado/ladoCuadradoMetros))
	y_cuadricula = int(-1*ladoCuadradoMetros * int((-1*y_pintado)/ladoCuadradoMetros))

	return x_cuadricula , y_cuadricula


#####################################################################################################################################
def frange(start, end=None, inc=None):
    "A range function, that does accept float increments..."
    if end == None:
        end = start + 0.0
        start = 0.0
    if inc == None:
        inc = 1.0
    L = []
    while 1:
        next = start + len(L) * inc
        if inc > 0 and next >= end:
            break
        elif inc < 0 and next <= end:
            break
        L.append(next)    
    return L


#####################################################################################################################################
class malla():
	"""Clase orientada al tratamiento de mallas, por ejemplo achuramiento"""

	def __init__(self, ladoCuadradoMetros=20):
		"""Aqui se inicializa la clase"""
		# Esto define lo grande o pequena que es la malla
		self.ladoCuadradoMetros = ladoCuadradoMetros
		# Este es el diccionario que guarda que antenas YA se han revisado
		self.conteo_Identificador = {}
		# Este diccionario guarda el enrejado
		self.diccioMalla = {}
		# Cantidad total de puntos revisados
		self.denominador = 0
		# Mayor intensidad del enmallado
		self.mayor_Intensidad = 0
		# Conjunto que agrupara las coordenadas con mayo intensidad
		self.conjunto_Mayores_Intensidades = Set()


	def achurar(self, **parametros ):
		"""En esta funcion se trata de usar todos los angulos en radianes. """

		self.latitud = False
		self.longitud = False

		self.x = False
		self.y = False

		self.azimut_grados = False
		self.azimut_radianes = False

		self.ancho_grados = False
		self.ancho_radianes = False
		
		self.alcance = False

		

		# Se llenan los valores
		for nombreParametro, valor in parametros.iteritems():
			# Se asigna el atributo
			setattr(self, nombreParametro, valor)

		# Si no hay coordenadas "x" e "y"
		if self.x == False or self.y == False:
			# Se crea la clase "transformador que cambia de angulares a transversaler
			transformador = Proj( proj='utm', zone='19', ellps='WGS84' )

			# El primer valor es "x" y el segundo es "y"
			self.x = transformador(self.longitud,self.latitud)[0]
			self.y = transformador(self.longitud,self.latitud)[1]

		# Si el ancho de cobertura esta en grados, se transforma a radianes
		#if (self.ancho_radianes == False) and (not type(self.ancho_grados) == str ):
		try:
			self.ancho_radianes = math.pi * self.ancho_grados/180
		# Si el azimut esta en grados, se transforma a radianes
		#if (self.azimut_radianes == False) and (not type(self.azimut_grados) == str ):
			self.azimut_radianes = math.pi * self.azimut_grados/180
		except TypeError:
			pass



		# Si hay valores distintos a un entero o los valores son equivalentes a cero, no se realizar ningun achurado
		#La primera condicion es por si alguno de los valores clave es cero
		#La segunda condicion es por si alguno de los valores no tiene sentido
		condicion_uno = not (self.ancho_radianes==0 or self.alcance==0)
		condicion_dos = not (type(self.azimut_radianes)==str or type(self.ancho_radianes)==str or type(self.alcance)==str)



		if not self.conteo_Identificador.has_key(self.identificador): 
			self.conteo_Identificador.setdefault(self.identificador, 1)
			
		else:
			self.conteo_Identificador[self.identificador] +=1

		# Si cumple que NO tiene valores cero, NO tiene valores STRING, y NO se ha revisado antes el valor.
		if condicion_uno and condicion_dos:
			# Se continua con el algoritmo.
			# Primero se crea el recorrido en que se movera el radio
			self.salto_radio = self.ladoCuadradoMetros*0.9
			borde_inf = self.salto_radio
			borde_sup = self.alcance
			recorrido_radio = frange( borde_inf, borde_sup + self.salto_radio , self.salto_radio )
			# Seguno se crean los intervalos en que se movera el angulo
			borde_inf = self.azimut_radianes-self.ancho_radianes/2
			borde_sup = self.azimut_radianes+self.ancho_radianes/2

			# Se va recorriendo el radio
			coord_revisadas = Set()

			for radio in recorrido_radio:

				# El salto en que se mueve el recorrido angular es dependiente del radio que corresonde
				recorrido_angular = frange( borde_inf , borde_sup , self.salto_radio/radio )
				# Se va recorriendo el angulo
				for angulo_rad in recorrido_angular:
	
					# Puesto que puede tocar que hallan angulos negativos aqui se normalizan, 
					# para dejarlos siempre positivos entre 0 y 2pi
					angulo_rad= angulo_rad%(2*math.pi)

					# Se calculan los delta a sumar a las coordenadas
					x_delta = math.sin(angulo_rad)*radio
					y_delta = math.cos(angulo_rad)*radio

					# Se marca la zona como que pertenece
					x_pintado = x_delta + self.x
					y_pintado = y_delta + self.y

					# Devuelve los valores a los que pertenece
					x_cuadricula, y_cuadricula = pertenece(x_pintado,y_pintado,self.ladoCuadradoMetros)

					# Cuando se revisa UNA antena especifica, toca que se repiten los ajustes,
					# esto es para que no sean incluidos
					if not (x_cuadricula, y_cuadricula) in coord_revisadas:

						coord_revisadas.add((x_cuadricula, y_cuadricula))

						self.diccioMalla.setdefault( str(x_cuadricula),{})
						self.diccioMalla[ str(x_cuadricula)].setdefault( str(y_cuadricula) , 0 )

						self.diccioMalla[str(x_cuadricula)][str(y_cuadricula)] += 1
				
						# A continuacion se agrupan los pinches con MAYOR INTENSIDAD!!!!
						if self.diccioMalla[str(x_cuadricula)][str(y_cuadricula)] >= self.mayor_Intensidad:

							if self.diccioMalla[str(x_cuadricula)][str(y_cuadricula)] > self.mayor_Intensidad:
								# Se actualiza el valor
								self.mayor_Intensidad=self.diccioMalla[str(x_cuadricula)][str(y_cuadricula)]
								# Se rehace el conjunto vacio
								self.conjunto_Mayores_Intensidades=Set()


							# Transforma de vuelta a coordenadas angulares los datos
							longitud = transformador( x_cuadricula , y_cuadricula ,inverse='true')[0]
							latitud = transformador(  x_cuadricula , y_cuadricula ,inverse='true')[1]

							# El conjunto que los agrupa
							self.conjunto_Mayores_Intensidades.add(( latitud , longitud ))



						self.denominador +=1

		
	#################################################################################################
	def normalizar(self):
		"""Esta funcion simplemente agarra la malla y la normaliza"""

		# Se recorre el diccionario
		for coord_x , diccio_coord_y in self.diccioMalla.iteritems():
			for coord_y, frecuencia in diccio_coord_y.iteritems():

				# Si no existe la llave se crea
				self.diccioMalla_norm.setdefault(coord_x,{})
				self.diccioMalla_norm[coord_x].setdefault(coord_y,0)
				# Se normaliza el diccionario
				self.diccioMalla_norm[coord_x][coord_y] = self.diccioMalla[coord_x][coord_y]/self.denominador

		return self.diccioMalla_norm
