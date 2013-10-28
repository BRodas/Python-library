# Importacion de librerias
from datetime import date,timedelta
from decimal import *




##########################################################################
# OrderSeeds

# Le entrega instancias a esta funcion. El primer atributo corresponde a un LISTADO de instancias, y el segundo corresponde a LA 

# Funcion de actualizacion
def update(OrderSeeds, neighbors , CenterObject , indice):


	# Distancia nucleo del objeto en el centro
	c_dist = CenterObject.core_distance


	# Recorrido de los objetos al rededor
	for Object in neighbors:



		# Si alguno de los puntos no ha sido procesado
		if not Object.Processed:

			# Distancia entre el punto al centro y uno de sus vecinos
			from pyproj import Geod
			g = Geod(ellps='WGS84')
			az12,az21, distancia = g.inv( Object.longitud , Object.latitud , CenterObject.longitud , CenterObject.latitud )

			# Se elige la mayor distancia
			new_r_dist = max( c_dist , distancia)


			# Si la distancia de alcance es indefinida
			if Object.reachability_distance == 1000000:

				# Se agrega una distancia
				Object.reachability_distance = new_r_dist

				

				# Se inserta el objeto en la lista, pero de manera ordenada
				OrderSeeds.append(Object)


			# Si ya hay una distancia
			else:

				# Pero esta es mayor al new_r_dist
				if new_r_dist < Object.reachability_distance:

					# Se modifica
					Object.reachability_distance = new_r_dist

	
	# Ordenamiento del listado de instancias en base a la distancia
	import operator
	OrderSeeds = sorted(OrderSeeds , key=operator.attrgetter('reachability_distance') )
				

	# ALGORITMO BUBLE SORT
	# Recorre el listado de vecinos desordenados, para ordenarlos. Se ocupara un algoritmo de Bubble. El algoritmo fue extraido de http://stackoverflow.com/questions/895371/bubble-sort-homework
	# Asumimos que las distancias estan desordenadas
	#/\sortede = False

	# Mientras no este ordenada
	#/\while not sortede:

		# Asumimos a primera que si lo esta
		#/\sortede = True

		

		# Se recorre el listado
		#/\for i in range(0, len(OrderSeeds)-1):

			# Si resulta que el "primer" elemento es mayor que el "segundo"
			#/\if OrderSeeds[i].reachability_distance > OrderSeeds[i+1].reachability_distance:

				# La lista en verdad esta desordenada
				#/\sortede = False

				# Se retiene el valor "segundo"
				#/\hold_01 = OrderSeeds[i+1]

				# Se hace la vuelta
				#/\OrderSeeds[i+1] = OrderSeeds[i]

				# Se vuelve a poner el segundo elemento
				#/\OrderSeeds[i] = hold_01


	#if CenterObject in OrderSeeds: OrderSeeds.remove(CenterObject)

	

	return OrderSeeds





##########################################################################################################################################################
# Analisis en profundidad del punto

# SetOfObjects es una clase que tiene como atributo el listado de de instancias, donde cada instancia es un Object. Object es una de las muchas instancias pertenecientes a SetOfObjects.
def ExpandClusterOrder(SetOfObjects , Object , epsi = 10000 , MinPts = 2 , listadoTuplas = [(),()] ):

	# Listado de instancias de vecinos [instancia01, instancia02, instancia03, ..., instanciaNN]
	neighbors = SetOfObjects.neighbors(Object, epsi)


	# Se marca como chequeado el objeto/punto
	Object.Processed = True

	# Se define con que se puede alcanzar el objeto
	Object.reachability_distance = 1000000

	# Se calcula la "distancia al centro" del punto en estudio
	Object.setCoreDistance(neighbors , epsi , MinPts)


	# En las siguientes dos lineas se escribe el punto en estudio
	listadoTuplas.append( ( Object.numero, Object.nombre ,Object.fecha , Object.hora , Object.latitud , Object.longitud,Object.azimut , Object.ancho , Object.alcance, Object.reachability_distance , Object.core_distance, Object.voronoi ))



	#if EscribirArchivo == True: Escribir.write(linea)

	# Lista vacia que se llenara con instancias y su indice
	OrderSeeds = []
	indice = 0

	# Si el elemento tiene una "core_distance". Si tiene una "core_distance", se procede a recolectar objetos/puntos que son "directly density-reachable"
	if Object.core_distance != 1000000:

		# Le entrega instancias a esta funcion. El primer atributo corresponde a un LISTADO de instancias, y el segundo corresponde a LA instancia. OrderSeeds, lo que hace entonces es generar un LISTADO con los objetos que estan "DIRECTLY DENSITY-REACHABLE" respecto al "Object", ordenados segun "REACHABILITY DISTANCE".
		OrderSeeds = update( OrderSeeds , neighbors , Object , indice)

		# Mientras hallan puntos en la cola
		#while indice < len(OrderSeeds):
		while OrderSeeds != []:
		
			# La siguiente linea si bien la define el paper esta intrincicamente
			# currentObject = OrderSeeds.next()

			# indice
			currentObject = OrderSeeds[0]

			# los nuevos vecinos
			neighbors = SetOfObjects.neighbors(currentObject , epsi)

			# Se declara como procesado
			currentObject.Processed = True

			# Se calcula la distancia al nucleo
			currentObject.setCoreDistance(neighbors , epsi , MinPts)

			
			# En las siguientes dos lineas se escribe el punto en estudio
			listadoTuplas.append(( currentObject.numero ,currentObject.nombre ,currentObject.fecha , currentObject.hora , currentObject.latitud , currentObject.longitud , currentObject.azimut , currentObject.ancho , currentObject.alcance , currentObject.reachability_distance , currentObject.core_distance,currentObject.voronoi ))
			

			# Si el elemento tiene una "core_distance"
			if currentObject.core_distance != 1000000:

				# Actualiza el orden de la cola

				OrderSeeds = update( OrderSeeds , neighbors , currentObject, indice)
				indice = -1
			
			# Remueve el elemento ya revisado
			if currentObject in OrderSeeds: OrderSeeds.remove(currentObject)

			# Se pasa al siguiente elemento de la lista OrderSeeds
			indice +=1




	return listadoTuplas




###########################################################################################################################################################
# Algoritmo OPTICS

# SetOfObjects es una clase, que debe tener como atributo un listado de instancias, pero tambien los vecinos. epsi es un radio, y debe ser en metros. MinPts es un numero natural. Destino, corresponde a un directorio donde se escribe el archivo.
def FOptics( SetOfObjects , epsi , MinPts ):

	
	listadoTuplas = []

	# Recorre el conjunto de objetos
	for Object in SetOfObjects.listadoInstancias:

		
		# Si la instancia NO ha sido procesado
		if not Object.Processed:

			# Si no se ha revisado, lo revisa en profundidad
			listadoTuplas = ExpandClusterOrder(SetOfObjects , Object , epsi , MinPts , listadoTuplas)

			# Se continua con los vecinos del punto anterior
			neighbors = SetOfObjects.neighbors(Object, epsi)
			if not neighbors == []:
				for El_neighbor in neighbors:

					
					if not El_neighbor.Processed: listadoTuplas = ExpandClusterOrder(SetOfObjects , El_neighbor , epsi , MinPts , listadoTuplas)


	# Cierra el archivo que se esta escribiendo
	#Escribir.close()

	return listadoTuplas




###########################################################################
# Clase creadora de SetOfObjects

# La clase creadora de una Instancia con un conjunto de instancias
class SetOfObjects:

	# Inicialisacion de la clase
	def __init__(self, listadoTuplas = [(),(),()]):

		# Se hace propia el listado de las tuplas
		self.listadoTuplas = listadoTuplas

		# En esta lista se meteran las mismas tuplas, pero transformadas en instancias		
		self.listadoInstancias = []

		# Estas se recorren una por una
		for tupla in self.listadoTuplas:
			
			# Se crea una instancia con la tupla
			instancia = Object( numero=tupla[0] , nombre = tupla[1] , fecha = tupla[2] , hora = tupla[3] , latitud = tupla[4] , longitud = tupla[5], azimut=tupla[6], ancho=tupla[7],alcance=tupla[8], voronoi = tupla[9] )
		
			# La instancia recien creada de anade al listado de instancias
			self.listadoInstancias.append(instancia)



	# En esta funcion se genera un listado de las instancias vecinas a la instancia "Object"
	def neighbors(self, Object , epsi):


		# Cero sera el vecino mas cercano en cuanto a distancia
		vecinosDesordenados = []

		# Distancias ordenadas
		distanciasDesordenadas = []

		# Diccionario de vecinos ordenados
		vecinosDesordenadosDiccionario = {}

		# Recorre el listado de instancias de puntos evaluados
		for instancia in self.listadoInstancias:


			# Para que el objeto no se compare consigo mismo
			if not (instancia == Object):

				# Calculo de la distancia entre los puntos
				from pyproj import Geod
				g = Geod(ellps='WGS84')
				az12,az21, distancia = g.inv( instancia.longitud , instancia.latitud , Object.longitud , Object.latitud )
				# Si la distancia con el punto en vista es menor a epsi
				if distancia <= epsi:

					# Se le agrega un atributo a la instancia
					instancia.distancia = distancia

					# Se agrega la instancia evaluada al listado de instancias. TODAVIA NO ESTAN ORDENADOS
					vecinosDesordenados.append(instancia)

					#2013-04-16 OMISION 1
					#Listado con las distancias al punto en estudio. TODAVIA NO ESTAN ORDENADOS
					#distanciasDesordenadas.append(distancia)


		# Ordenamiento del listado de instancias en base a la distancia
		import operator
		vecinosOrdenados = sorted(vecinosDesordenados , key=operator.attrgetter('distancia') )


		#2013-04-16 OMISION 1 (INICIO)
		# Recorre el listado de vecinos desordenados, para ordenarlos. Se ocupara un algoritmo de Bubble. El algoritmo fue extraido de http://stackoverflow.com/questions/895371/bubble-sort-homework
		# Asumimos que las distancias estan desordenadas
		#/\sortede = False

		# Mientras no este ordenada
		#/\while not sortede:

			# Asumimos a primera que si lo esta
			#/\sortede = True

			# Se recorre el listado
			#/\for i in range(0, len(distanciasOrdenadas)-1):

				# Si resulta que el "primer" elemento es mayor que el "segundo"
				#/\if distanciasOrdenadas[i] > distanciasOrdenadas[i+1]:

					# La lista en verdad esta desordenada
					#/\sortede = False

					# Se retiene el valor "segundo"
					#/\hold_01 = distanciasOrdenadas[i+1]
					#/\hold_02 = vecinosOrdenados[i+1]

					# Se hace la vuelta
					#/\distanciasOrdenadas[i+1] = distanciasOrdenadas[i]
					#/\vecinosOrdenados[i+1] = vecinosOrdenados[i]

					# Se vuelve a poner el segundo elemento
					#/\distanciasOrdenadas[i] = hold_01
					#/\vecinosOrdenados[i] = hold_02
		#2013-04-16 OMISION 1 (FIN)




		# Se debuelve el listado de vecinos
		return vecinosOrdenados		



###########################################################################
# Clase creadora de instancias Objects

class Object:

	# Se entregan los parametros que crean un objeto
	def __init__(self, numero = 0 ,nombre="" , fecha = date(2013,01,01) , hora = timedelta( 0, 1000) , latitud = Decimal('-33.00'), longitud = Decimal('-70.00') , azimut=0 , ancho=0 , alcance=0, voronoi = 0):

		self.numero = numero
		self.nombre = nombre
		self.fecha = fecha
		self.hora = hora
		self.latitud = latitud
		self.longitud = longitud
		self.azimut = azimut
		self.ancho = ancho
		self.alcance = alcance
		self.voronoi = voronoi
		self.distancia = 0
		self.Processed = False
		self.reachability_distance = 1000000
		self.core_distance = 1000000

	# Funcion que calcula la "core distance". neighbors es el listado de instancias correspondientes a puntos vecinos al principal. 
	# neighbors VIENE ORDENADO POR DISTANCIAS, EL CERO ES EL VECINO MAS CERCANO.
	def setCoreDistance(self , neighbors , epsi , MinPts):


		# Si hay puntos suficientes
		if (len(neighbors)>=MinPts) and (not neighbors==[]):

			# Se mete al vecino en la variable
			if not ( (MinPts-1)<0 ) :
				vecino = neighbors[MinPts-1]
			else:
				vecino = neighbors[0]

			# Se calcula la distancia
			from pyproj import Geod
			g = Geod(ellps='WGS84')
			az12,az21, distancia = g.inv( vecino.longitud , vecino.latitud , self.longitud , self.latitud )

			# Se calcula la core_distance, en metros
			self.core_distance = distancia

