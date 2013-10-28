#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-

"""
####################################################################################################
MODIFICACIONES
####################################################################################################
jue jun 13 17:57:07 CLT 2013
- Se agregan las distintas opciones desde terminal

"""

####################################################################################################
# LIBRERIAS
####################################################################################################

# Trabajar MySQL
import MySQLdb

# para el uso de opciones en la linea de comando
import argparse

# Para trabajar con la linea de comando. Envia comandos a la "linea de comandos"
import subprocess

# Libreria personal para el tratamiento de las consultas. En una tabla hay varias filas, una fila es un "Objeto"
from lib_python import Objetos

# Extraccion de la info de foursquare
from lib_python import fsq

# Para la creacion de mapas de calor
import heatmap

# Calculo de distancias
from pyproj import Geod

# Eliminar acentos
import unicodedata

# Se importa la libreria que permite tratamiento de fechas
from datetime import date,timedelta,datetime

# Se importa una libreria para crear facilmente archivos KML
import simplekml



####################################################################################################
# EL SIGUIENTE BLOQUE ESTA ORIENTADO PARA LA INTERACCION CON EL TERMINAL
####################################################################################################
# Se crea la instancia
parser = argparse.ArgumentParser(description = "Foursquare", epilog = '13 de Junio 2013')


# Graficar los locales FOURSQUARE
parser.add_argument("-g","--graficar_locales", help="Se grafican todos los locales de Foursquare" , action ="store_true" )

# Graficar los locales FOURSQUARE
parser.add_argument("-c","--crawleo_datos", help="Se crawlean los datos de Foursquare" , action ="store_true" )


args = parser.parse_args()



####################################################################################################
# ELIMINADORA DE TILDES
####################################################################################################
def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', unicode(s)) if unicodedata.category(c) != 'Mn'))


####################################################################################################
# GRAFICAR LOCALES FOURSQUARE
####################################################################################################
if args.graficar_locales:

	# Se crea la instancia
	kml = simplekml.Kml()


	# Se abre la coneccion a la base de datos
	db=MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "eadh5148", db = "mobility", port=5029 )


	# Se crea el cursos
	c = db.cursor() 

	# Se ejecuta una consulta
	c.execute("select NOMBRE_LOCAL, LATITUD, LONGITUD, CATEGORIA from FOURSQUARE ; " )

	# se pasa la consuta a un listado entendible
	listado_BaseDatos = c.fetchall()

	# El estilo de los pinches
	style = simplekml.Style()
	style.labelstyle.color = simplekml.Color.green
	style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'

	# Recorrido de los locales
	for tienda in listado_BaseDatos:

		longitud = tienda[2]
		latitud = tienda[1]

		if (latitud <= -20) and (longitud <= -50 ):
			#Graficando el local
			tienda_graficada = kml.newpoint(name= tienda[0] )
			tienda_graficada.description = str(tienda[3]) 
			tienda_graficada.coords = [ ( longitud , latitud ) ]  
			tienda_graficada.style = style

	# Se graba el archivo
	kml.save("Locales_Foursquare.kml")


####################################################################################################
# CRAWLEO DE DATOS
####################################################################################################
elif args.crawleo_datos:

	####################################################################################################
	# CONSULTA DE LAS 499 COORDENADAS MAS FRECUENTES
	####################################################################################################
	# La consulta
	consulta01 = 'SELECT coord, count(coord) as frecuencia FROM (select concat(LATITUD,\',\',LONGITUD) AS coord \
		FROM CDR_Mediacion_Limpio , Antenas_Limpio_Nov12Ene13 \
		WHERE CDR_Mediacion_Limpio.BTS_ID = Antenas_Limpio_Nov12Ene13.BTS_ID AND Antenas_Limpio_Nov12Ene13.REGION = "13" ) AS tabla \
		GROUP BY coord \
		ORDER BY frecuencia DESC \
		LIMIT 400;'


	consulta01 = str(consulta01)

	# TIMESTAMP
	now=datetime.now()
	print('\n')
	print('INICIO: Ejecucion consulta')
	print(now)


	codigoMysql = 'echo "'+consulta01+'" | mysql-ib -uroot -peadh5148 mobility'


	# TIMESTAMP
	now=datetime.now()
	print('\n')
	print('FIN: Ejecucion consulta')
	print(now)


	# Se toma la data desde lo que entrega la linea de comando
	data =  subprocess.Popen( codigoMysql , shell = True, stdout=subprocess.PIPE ).communicate()[0]

	# Se crea la clase "consulta", donde se especifica que la String que se tira tiene 2 columnas
	ObjetosAnalisis = Objetos.ListadoObjetos(data,2)

	# Se entregan encabezados a las columnas, que se transforman en el nombre de los atributos de la clase "consulta"
	ObjetosAnalisis.DarEncabezados( 'coordenadas','frecuencia')
	# Se le entrega un formato a cada columna, o atributo.
	ObjetosAnalisis.DarFormatos( frecuencia='entero')
	# Se crea una lista con valores, en vez de instancias
	ObjetosAnalisis.ListarValores()

	# Creacion de la lista donde se meteran los valores
	ObjetosAnalisis_01 = []
	# Se recorre la lista
	total_frec=0
	# El minimo
	minimo = 100000
	maximo = 0


	########## Preparacion de parametros para escribir los datos ##########
	# Nombre del archivo
	nombreArchivo = 'Antenas_DB_Histograma.txt'
	# Ubicacion donde se grabara el archivo
	ubicacion = '/media/discoExternoRAID/raul/Python/Resultados/'+nombreArchivo
	# Se crea la instancia que lo hace
	Escribir = open( ubicacion, 'w')

	for tupla in ObjetosAnalisis.listaValores:	
		latitud = float(tupla[0][0:10])
		longitud = float(tupla[0][15:25])
		frecuencia = tupla[1]
		total_frec += frecuencia
		minimo = min(minimo,frecuencia)
		maximo = max(maximo,frecuencia)
		ObjetosAnalisis_01.append(( latitud, longitud , frecuencia ))
		Escribir.write(str( latitud )+','+str( longitud )+','+str( frecuencia)+'\n')

	# Se cierra el archivo
	Escribir.close()



	####################################################################################################
	# GRAFICO DE LOS DATOS EN UN MAPA DE CALOR (TOTALMENTE OPCIONAL)
	####################################################################################################

	# En esta parte se una una funcion para no usar mucha memoria
	def mapa_de_calor(ObjetosAnalisis_01):
		# Creacion de la instancia
		hm = heatmap.Heatmap()

		# Creacion de la lista
		pts = []
		# Creacion de la lista con los puntos
		for tupla in ObjetosAnalisis_01:

			# Normalizacion para el mapa de calor
			norm = int(  4/float(maximo-minimo)*(tupla[2]-minimo) ) + 1  
			for i in range(norm):
				# Se invierte a: Primero longitudes y luego latitudes
				pts.append(( tupla[1],tupla[0]  ))

		# Inclusion de los puntos
		hm.heatmap(pts, scheme = 'classic', opacity = 160, dotsize = 150)
		# Creacion del archivo con el mapa de calor
		hm.saveKML("Antenas_Mas_Usadas.kml")

	# Aqui se usa la funcion recien creada
	mapa_de_calor(ObjetosAnalisis_01)



	####################################################################################################
	# EXTRACCION DE INFO A LOS ALREDEDORES Y ESCRITURA EN UN TXT
	####################################################################################################

	########## Preparacion de la instancia que extraera la info de Foursquare ##########
	# Creacion de la instancia
	info_Foursquare = fsq.fsq()


	########## Preparacion de parametros para el calculo de la distancia al centro ##########
	# Declaracion de la instancia que ayudara a calcular la distancia al centro de santiago
	g = Geod(ellps='bessel')
	# Calculo al centro de santiago
	centro_Lat = -33.437911
	centro_Lng = -70.650459


	########## Preparacion de parametros para escribir los datos ##########
	# Nombre del archivo
	nombreArchivo = 'Foursquare_DB_Borrar.txt'
	# Ubicacion donde se grabara el archivo
	ubicacion = '/media/discoExternoRAID/raul/Python/Resultados/'+nombreArchivo
	# Se crea la instancia que lo hace
	Escribir = open( ubicacion, 'w')


	# Recorrido de la lista
	for tupla in ObjetosAnalisis_01:

		# Se extraen las tiendas alrededor de aquella coordenada, y se ponen en una LISTA de tiendas
		venues = info_Foursquare.buscar( tupla[0] , tupla[1] , 500 , 50)

		# Se recorre la lista de tiendas
		for venue in venues:

			# Calculo de la distancia al centro de santiago
			az12,az21, dist_Centro_Sntg = g.inv( centro_Lng , centro_Lat , venue.location.lng , venue.location.lat )

			# Se incluyen SOLO los locales que tienen categoria
			if not (venue.categories == [] ):

				# Para el tratamiento de caracteres raros
				try:
					# Escritura de la linea
					# print( str( elimina_tildes(venue.name) )+','+str(venue.id)+','+str(venue.location.lat)+','+str(venue.location.lng)+','+str(venue.categories[0])+','+str(dist_Centro_Sntg)+'\n')
					Escribir.write(str( elimina_tildes(venue.name) )+','+str(venue.id)+','+str(venue.location.lat)+','+str(venue.location.lng)+','+str(venue.categories[0])+','+str(dist_Centro_Sntg)+'\n')

				# Si hay algun error solo continua
				except UnicodeEncodeError:
					print("Advertencia: Nombre no codificable. NO se escribio la linea")

	# Se cierra el archivo
	Escribir.close()
