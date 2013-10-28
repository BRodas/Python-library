
##########################################################################################################################################################
# FUNCION EXTRACTORA DE CARACTERES.

def extractorContenido(cadenaMAYOR = "hola mundo" ,indice = 0, caracterFIN = " "):
	"""Esta funcion extrae una palabra o "cadena de caracteres" MENOR de una cadena MAYOR. Para ello se le debe entregar el indice de inicio, o sea en que caracter comenzar a extraer, y el caracter pone fin a la extraccion"""

	# Se declara vacia la variable que contendra el String de retorno 
	cadenaMENOR= ""
	# Se recorre el String
	for caracter in cadenaMAYOR[indice:]:
		# Si no se ha llegado al caracter de termino se continua
		if (not caracter == caracterFIN): cadenaMENOR = cadenaMENOR + caracter
		# Se se llego al caracter de termino se finaliza todo
		elif caracter == caracterFIN: break
	# Se retorna la respuesta
	return cadenaMENOR



###########################################################################################################################################################
# EL SCRIPT MISMO

from bs4 import BeautifulSoup


# Se define el camino al archivo destino donde se escribiran los resultados
destino = '/media/discoExternoRAID/raul/Python/Resultados/AntenasTecnologia.txt'
escribir = open(destino,'w')


# Se crea una instancia de BeautifulSoup
soup = BeautifulSoup(open( "/media/discoExternoRAID/raul/Python/XML/Antenas_Orientadas.kml"), "xml")


# Se adquiere el STRING  de interes.
contenidoDescription = soup.Document.Folder.Placemark.description.string


# Se recorren los elementos hijos,
for child in soup.Document.Folder.children:

	# Si el hijo no es vacio,
	if not child == '\n':

		# Verifica que sea un placemark
		if child.name == 'Placemark':

			# Se adquiere el STRING  de interes.
			contenidoDescription = child.description.string

			# Se ve si es 3G la tecnologia de la antena,
			indice = contenidoDescription.find("3G")
			# si la tegnologia es realmente 3G,
			if (not indice == -1):
				# se especifica en la variable,
				Tecnologia = "3G"
			# si no lo es,
			else:
				# se comprueba que la tecnologia es 2G, 
				indice = contenidoDescription.find("2G")
				if (not indice == -1):
					Tecnologia = "2G"
				# si tampoco es 2G,
				else:
					# se declara como indefinido.
					Tecnologia = "Indefinido"


			# Se busca el indice correspondiente al inicio del caracter de "CELLBTS",
			indiceNombreBTS = contenidoDescription.find("CELLBTS")
			# a este indice se le suma 17 correspondiente al inicio del nombre,
			Nuevo_indiceNombreBTS = indiceNombreBTS + 17
			# con esto se entregan los parametros a la formula
			nombreBTS = extractorContenido( cadenaMAYOR = contenidoDescription , indice = Nuevo_indiceNombreBTS , caracterFIN = "<")


			# Se busca la region,
			indiceRegion = contenidoDescription.find("COD_REG")
			# a este indice se le suma 17 correspondiente al inicio del nombre,
			Nuevo_indiceRegion = indiceRegion + 17
			# con esto se entregan los parametros a la formula
			Region = extractorContenido( cadenaMAYOR = contenidoDescription , indice = Nuevo_indiceRegion , caracterFIN = "<")


			# Se busca la latitud,
			indiceLat = contenidoDescription.find("th>LAT</th>")
			# a este indice se le suma 17 correspondiente al inicio del nombre,
			Nuevo_indiceLat = indiceLat + 16
			# con esto se entregan los parametros a la formula
			Latitud = extractorContenido( cadenaMAYOR = contenidoDescription , indice = Nuevo_indiceLat , caracterFIN = "<")


			# Se busca la longitud,
			indiceLon = contenidoDescription.find("th>LON</th>")
			# a este indice se le suma 17 correspondiente al inicio del nombre,
			Nuevo_indiceLon = indiceLon + 16
			# con esto se entregan los parametros a la formula
			Longitud = extractorContenido( cadenaMAYOR = contenidoDescription , indice = Nuevo_indiceLon , caracterFIN = "<")


			# Se busca el azimut,
			indiceAzi = contenidoDescription.find("AZIMUTH")
			# a este indice se le suma 17 correspondiente al inicio del nombre,
			Nuevo_indiceAzi = indiceAzi + 17
			# con esto se entregan los parametros a la formula
			Azimut = extractorContenido( cadenaMAYOR = contenidoDescription , indice = Nuevo_indiceAzi , caracterFIN = "<")


			# Se busca el angulo de cobertura,
			indiceAng = contenidoDescription.find("SECTORWIDTH")
			# a este indice se le suma 17 correspondiente al inicio del nombre,
			Nuevo_indiceAng = indiceAng + 21
			# con esto se entregan los parametros a la formula
			CoberturaAng = extractorContenido( cadenaMAYOR = contenidoDescription , indice = Nuevo_indiceAng , caracterFIN = "<")


			# Se busca el alcance,
			indiceDist = contenidoDescription.find("DISTANCIA")
			# a este indice se le suma 17 correspondiente al inicio del nombre,
			Nuevo_indiceDist = indiceDist + 19
			# con esto se entregan los parametros a la formula
			Alcance = extractorContenido( cadenaMAYOR = contenidoDescription , indice = Nuevo_indiceDist , caracterFIN = "<")

			# Se busca la provincia,
			indiceProv = contenidoDescription.find("COD_PROV</th>")
			# a este indice se le suma 17 correspondiente al inicio del nombre,
			Nuevo_indiceProv = indiceProv + 18
			# con esto se entregan los parametros a la formula
			Provincia = extractorContenido( cadenaMAYOR = contenidoDescription , indice = Nuevo_indiceProv , caracterFIN = "<")


			escribir.write( nombreBTS+','+Tecnologia+','+Region+','+Provincia+','+Latitud+','+Longitud+','+Azimut+','+CoberturaAng+','+Alcance+'\n' )

