#!/usr/bin/python2.7

# Libreria que permite hacer la consulta por HTML
from urllib2 import urlopen
# Libreria que permite trabajar con datos Json
import simplejson
# Se importa la libreria que el uso de decimales
from decimal import *
# El realizar las siguientes 3 lineas permite el uso de acentos. IMPORTANTE!!!!!!!
import sys
reload(sys)
sys.setdefaultencoding("latin1")
# Permite parsear HTML
from bs4 import BeautifulSoup
# Permite el uso de conjuntos
from sets import Set
# Libreria para eliminar acentos
import unicodedata
# Calculo de valores absolutos
from math import fabs
# Decodifica la polilinea
from decode import decode_line
# Creacion del archivo KML
import simplekml




####################################################################################################
# Invertir tuplas
####################################################################################################

def invertir(polylinea):
	"""Esta funcion invierte las tuplas.
		original 	(x,y)
		retorno		(y,x)

		OJO: Se entrega un listado de tuplas"""

	resultado = []
	for tupla in polylinea:

		tupla_invertida = (tupla[1],tupla[0])
		resultado.append(tupla_invertida)

	return resultado

####################################################################################################
# Coordenada mas cercana
####################################################################################################
def coordenada_cercana(referencia, listado_coordenadas):
	"""Esta funcion calcula la coordenada mas cercana a la referencia pero de manera sencilla, obviando la curvatura de la tierra"""

	dist = 99999999999

	# Recorrido de la lista
	for tupla in listado_coordenadas:
		dist_nueva = fabs(referencia[0]-tupla[0])+fabs(referencia[1]-tupla[1])
		if dist_nueva < dist:
			coordenada = tupla
			dist = dist_nueva

	return coordenada



####################################################################################################
# Eliminadora de tildes
####################################################################################################
def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', unicode(s)) if unicodedata.category(c) != 'Mn'))



####################################################################################################
# Transformadora de Strings
####################################################################################################
def string_json(oracion_o_palabra):
	"""Esta funcion transforma la "oracion_o_palabra" en un "string" que se pueda llegar y usar en json """

	# si son varias palabras estas se separan en un listado
	listado = oracion_o_palabra.split()

	# Se declara la variable a usar
	paraJson = listado[0]
	# Se recorre este listado
	for elemento in listado[1:]:
		# Se van concatenando palabra por palabra con un "+" adelante
		paraJson += '+'+elemento

	return paraJson



####################################################################################################
# Funcion que transforma calles en una tupla de coordenadas
####################################################################################################
def calle_coordenadas(calle):
	"""Funcion que transforma calles en una lista de tuplas de coordenadas"""

	# Definicion de parametros importantes!
	googleapi = 'http://maps.googleapis.com/maps/api/geocode/json'

	# Listado que contendra las tuplas
	listado = []
	
	# transformacion de la calle
	calle = string_json(calle)

	# La consulta que sacara el origen y destino
	url = '%s?address=%s,+Santiago+Metropolitan+Region,+Chile&sensor=false' % (googleapi, calle)

	# And go ahead and make the request
	request = urlopen(url)
	# and load the JSON
	results = simplejson.load(request)


	latitud = results['results'][0]['geometry']['bounds']['northeast']['lat']
	longitud = results['results'][0]['geometry']['bounds']['northeast']['lng']
	coordenadas = (latitud,longitud)
	listado.append(coordenadas)

	latitud = results['results'][0]['geometry']['bounds']['southwest']['lat']
	longitud = results['results'][0]['geometry']['bounds']['southwest']['lng']
	coordenadas = (latitud,longitud)
	listado.append(coordenadas)


	latitud = results['results'][0]['geometry']['location']['lat']
	longitud = results['results'][0]['geometry']['location']['lng']
	coordenadas = (latitud,longitud)
	listado.append(coordenadas)

	return listado



####################################################################################################
# Funcion que recoje las calles en el trazado
####################################################################################################
def trazado( OrigenLatitud, OrigenLongitud , DestinoLatitud , DestinoLongitud, ModoTransporte ):
	"""La siguiente funcion devuelve el listado "trazado" con las tuplas de coordenadas que deben ir siguiendose.

		trazado[0] es la tupla (OrigenLatitud, OrigenLongitud)
		trazado[-1] es la tupla (DestinoLatitud, DestinoLongitud)

		Los modos de transporte para la variable ModoTransporte son:
			driving
			walking
			bicycling
			transit
		"""


	# Conjunto de objetos que se obvian
	conj_obviar = Set(['right','left','north','south','5th','1st','2nd','3rd','4th'])

	# Conjunto de Calles
	conj_calles = Set([])

	# Conjunto de Coordenadas
	conj_coordenadas = Set([])

	# Seleccion de la referencia
	referencia = ( OrigenLatitud , OrigenLongitud )

	# "Distancia" limite
	limite = (fabs( OrigenLatitud - DestinoLatitud )+fabs( OrigenLongitud - DestinoLongitud ))

	# Transformacion a tipo "string"
	OrigenLatitud = str(OrigenLatitud)
	OrigenLongitud = str(OrigenLongitud)
	DestinoLatitud = str(DestinoLatitud)
	DestinoLongitud = str(DestinoLongitud)


	# Definicion de parametros importantes!
	googleapi = 'http://maps.googleapis.com/maps/api/directions/json'
	origin = '%s,%s' % (OrigenLatitud, OrigenLongitud)
	destination = '%s,%s' % (DestinoLatitud, DestinoLongitud)


	# La consulta que sacara el origen y destino
	url = '%s?origin=%s&destination=%s&mode=%s&sensor=false' % (googleapi, origin, destination, ModoTransporte)
	
	
	# And go ahead and make the request
	request = urlopen(url)

	# and load the JSON
	results = simplejson.load(request)
	
	polylinea = results['routes'][0]['overview_polyline']['points']

	# Se recorren TODAS las rutas
	for route in results['routes']:
	

		# Si no hay "waypoints" esto es unico
		for leg in route['legs']:


			# Los pasos uno por uno
			for step in leg['steps']:


				# Se guarda la linea HTML
				html_doc = step['html_instructions'].decode('unicode-escape')
				# Se parsea
				soup = BeautifulSoup(html_doc)
				# Se agrupan todos los valores en negritas en una lista, donde se incluyen las calles
				listado = soup.find_all('b')
				# Se recorren los elementos de la lista
				for elemento in listado:
					# Se transforma el contenido del tag en tipo string
					elemento = str(elemento.string)
					# Se chequea si el elemento esta en la lista a obviar
					if (not ( elemento in conj_obviar)) and (not ( elemento in conj_calles)):

						# Eliminador de tildes
						elemento = elimina_tildes(elemento)
						# Anade el elemento al conjunto calles
						conj_calles.add(elemento)
						# Se transforma la calle en coordenadas (una tupla con latitud y longitud)
						coordenadas = calle_coordenadas(elemento)
						# Se elige el mas cercano respecto a la referencia
						posible_referencia = coordenada_cercana( referencia,coordenadas)

						posible_referencia_evaluada = fabs( referencia[0] - posible_referencia[0] )+fabs( referencia[1] - posible_referencia[1] )

						# Por si se escapa a un lado que nada que ver
						if posible_referencia_evaluada < limite:
							referencia = posible_referencia
							# Se agrega al conjunto
							conj_coordenadas.add(referencia)
							# Se extrae el contenido de las etiquetas
							

	return conj_coordenadas , conj_calles , polylinea



# INICIO PARA EL TESTEO


OrigenLatitud = -33.40171
OrigenLongitud = -70.544171
DestinoLatitud = -33.433733
DestinoLongitud = -70.558419


#driving,walking,bicycling,transit
coordenadas, calles , polylinea = trazado( OrigenLatitud, OrigenLongitud , DestinoLatitud , DestinoLongitud, 'driving' )

#Listado con tuplas (lat,lng)
polylinea = decode_line(polylinea)
print(polylinea)

# Invertir tuplas
polylinea = invertir(polylinea)
print(polylinea)


kml = simplekml.Kml()

lin = kml.newlinestring(name="Camino", description= "camino de prueba", coords= polylinea )  # lon, lat, optional height

lin.style.linestyle.color = 'ff0000ff'  # Red

lin.style.linestyle.width= 10  # 10 pixels

kml.save("borrar.kml")

print(coordenadas)
