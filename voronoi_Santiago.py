#!/usr/bin/python2.7


####################################################################################################
# HISTORIAL Y MODIFICACIONES
####################################################################################################
"""El siguiente codigo crea un mapa de Voronoi para santiago

mar ago  6 17:48:33 CLT 2013
-Se incluye la creacion de un KML con los numeros de Voronoi

mie jul  3 16:32:33 CLT 2013
-	Se re realiza el codigo pero para TODO chile,
-	Se ponen cotas para el grafico KML
-	Se tiene cuidado con el re procesamiento de lineas ya dibujadas

13Jun2013	
-	Se cambia el color de la linea a verde y se especifica el ancho en 3.
-	Se usan las latitudes y longitudes
-	Se aplica a TODO Chile

"""



####################################################################################################
# LIBRERIAS QUE SE IMPORTAN
####################################################################################################

# funcion que verifica si un punto esta dentro de un poligono convexo
from lib_python import punto_en_poligono

# Se importa la libreria que permite tratamiento de fechas
from datetime import date,timedelta,datetime

# Trabajar MySQL/Infobright
import MySQLdb

# Para trabajar con la linea de comando. Envia comandos a la "linea de comandos"
import subprocess

# Personal para el tratamiento de las consultas. En una tabla hay varias filas, una fila es un "Objeto"
from lib_python import Objetos

# Para la fragmentacion de Voronoi
#from pyhull.voronoi import VoronoiTess

# Se importa la libreria que el uso de decimales
from decimal import *

# Se importa una libreria para crear facilmente archivos KML
import simplekml

# Libreria que calcula las UTM
from pyproj import Proj


####################################################################################################
# TIMESTAMP
####################################################################################################
now=datetime.now()
print('\n')
print('Tiempo de inicio')
print(now)



####################################################################################################
# FUNCION LISTA A STRING
####################################################################################################

def lista_a_string(lista = [1,2,3]):

	lista_nueva = []
	for elemento in lista:
		lista_nueva.append(str(elemento))

	cadena = ','.join(lista_nueva)

	return cadena

####################################################################################################
# EL CODIGO
####################################################################################################


# Conexion MYSql
db = MySQLdb.connect(host = "127.0.0.1", user= "root", passwd = "eadh5148", db = "mobility", port = 5029)
BaseDatos = db.cursor()


####################################################################################################
# KML que muestra el numero de Voronoi correspondiente.
####################################################################################################
# La consulta
consulta = 'select LONGITUD,LATITUD,NUM_VORONOI from Antenas group by NUM_VORONOI '
BaseDatos.execute(consulta)
listado_valores = BaseDatos.fetchall()

# Se crea el KML
archivo_KML = simplekml.Kml(name="Numero de regiones de Voronoi")

# Se recorren las 3422 (aprox.)  regiones
for region_voronoi in listado_valores:
	
	longitud = region_voronoi[0]
	latitud = region_voronoi[1]
	numero = str(region_voronoi[2])	

	punto_modificable = archivo_KML.newpoint(coords = [(longitud,latitud)], name = numero )
	punto_modificable.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'

archivo_KML.save('/media/discoExternoRAID/raul/Python/Resultados/Num_Voronoi.kml')

####################################################################################################
### CALCULO DEL DIAGRAMA DE VORONOI
####################################################################################################
"""

# La consulta
consulta = 'SELECT * FROM Antenas WHERE (LONGITUD IS NOT NULL) AND (LATITUD IS NOT NULL) ;'
BaseDatos.execute(consulta)
listado_valores = BaseDatos.fetchall()

# Puntos
puntos = []

# Se crea la instancia
kml = simplekml.Kml()


# Se crea una carpeta donde se guardan los puntos de las antenas!
carpeta_antenas = kml.newfolder(name='Antenas')
style = simplekml.Style()
style.labelstyle.color = simplekml.Color.green
style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
# Re arreglo del arreglo
for antena in listado_valores:
	# Se Pasan los campor a variables
	region_punto = antena[0]
	BTS = antena[1]
	longitud = antena[3]
	latitud = antena[4]
	# Se crea un listado con los puntos en estudio, sin repeticiones
	if not ([longitud,latitud] in puntos):puntos.append([ longitud , latitud ])
	# Los puntos dentro de las coordenadas definidas se grafican
	if region_punto == '13' :
		instancia_punto = carpeta_antenas.newpoint(name = BTS)
		instancia_punto.coords = [( longitud , latitud )]
		instancia_punto.style = style


# Se crea la instancia de Voronoi
voronoi = VoronoiTess(puntos)
# voronoi.vertices es un listado de listas, con el primer valor una longitud y el segundo una latitud.
# voronoi.regions es un listado de listas con el indice del vertice correspondiente.



### CREACION DEL ARCHIVO CSV, Y KML

# donde se va a escribir el archivo
Escribir = open('/media/discoExternoRAID/raul/Python/Resultados/voronoi_resultado.csv' ,'w')

# La consulta
consulta = 'SELECT LONGITUD,LATITUD,NUM_VORONOI,REGION FROM Antenas WHERE (LATITUD IS NOT NULL) AND (LONGITUD IS NOT NULL) GROUP BY NUM_VORONOI ;'
BaseDatos.execute(consulta)
listado_valores =list(BaseDatos.fetchall())

# listado de las coordenadas de la region
coordenadas_region = []
coordenadas_kml = []

#Se crea una carpeta donde se guardan los puntos de las antenas!
carpeta_regiones = kml.newfolder(name='Regiones')


# recorrido de todas las regiones
for region in voronoi.regions:
	
	# las coordenadas de la region
	for indice_vertice in region:
		coordenadas_region.append( voronoi.vertices[indice_vertice] )
		coordenadas_kml.append( [ voronoi.vertices[indice_vertice][1], voronoi.vertices[indice_vertice][0] ] )
	
	# pregunta: que punto pertenece a la region
	for punto in listado_valores:
		longitud = punto[0]
		latitud = punto[1]
		longitud = float(longitud)
		latitud = float(latitud)
		

		if punto_en_poligono.point_in_poly(longitud, latitud, coordenadas_region):
			# Si es asi y pertenece, se escribe una linea con el vertice correspondiente
			for coordenada in coordenadas_region:
				# Se crea la linea
				longitud = coordenada[0]
				latitud = coordenada[1]
				linea = lista_a_string(punto)+','+str(longitud)+','+str(latitud)+'\n'
				# Se escribe en el archivo
				Escribir.write(linea)		


			########### PARTE GRAFICA: Solo para la region metropolitana
			#region = punto[3]
			#if region == '13':
				# Se van agregando los distintos poligonos
			#	nombre = punto[2]
			#	print('\n')
			#	print('coordenadas region')
			#	print(coordenadas_region)
			#	print('\n')
        	#	instancia_poligono = carpeta_regiones.newpolygon(name= str(nombre), outerboundaryis = [coordenadas_kml] , innerboundaryis = [coordenadas_kml])
			#	instancia_poligono.style.linestyle.color = simplekml.Color.red
        	#	instancia_poligono.style.linestyle.width = 2


			# se guarda el punto que se borrara
			borrar_punto = punto
			# Se continua con la siguiente region
			break

	# Se borra el punto del listado
	try:
		listado_valores.remove(borrar_punto)
	except ValueError:
		pass

	# Se resetea el listado para meter la proxima region
	coordenadas_kml = []
	coordenadas_region = []

# Se cierra el archivo
Escribir.close()

# Se graba el archivo
kml.save("Voronoi_diagrama.kml")
"""

# TIMESTAMP
now = datetime.now()
print('\n')
print('TIEMPO DE FIN')
print(now)

