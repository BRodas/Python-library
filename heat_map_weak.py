#!/usr/bin/python2.7

"""
####################################################################################################
DESCRIPCION
####################################################################################################

	En este Script se extrae informacion agregada de las celdas de Voronoi.
"""

####################################################################################################
# LIBRERIAS
####################################################################################################

# Trabajar MySQL
import MySQLdb

# para el uso de opciones en la linea de comando
import argparse

# Para la creacion de mapas de calor
import heatmap

# Se importa una libreria para crear facilmente archivos KML
import simplekml

# Se importa la libreria que permite tratamiento de fechas
from datetime import date,timedelta,datetime


####################################################################################################
# EL SIGUIENTE BLOQUE ESTA ORIENTADO PARA LA INTERACCION CON EL TERMINAL
####################################################################################################
# Se crea la instancia
parser = argparse.ArgumentParser(description = "Foursquare", epilog = '13 de Junio 2013')


# Graficar los locales FOURSQUARE
parser.add_argument("-g","--graficarKML", help="Se grafican todos los locales de Foursquare" , action ="store_true" )

# Graficar los locales FOURSQUARE
parser.add_argument("-e","--escribirTXT", help="Se crawlean los datos de Foursquare" , action ="store_true" )


args = parser.parse_args()


####################################################################################################
# GRAFICO DE LOS DATOS EN UN MAPA DE CALOR (TOTALMENTE OPCIONAL)
####################################################################################################

# En esta parte se una una funcion para no usar mucha memoria
def mapa_de_calor(ObjetosAnalisis_01, nombre_mapa_calor,maximo,minimo):
	"""A esta funcion se le entrega un listado de tuplas, talque el orden es:
		(longitud,latitud,frecuencia)"""

	# Creacion de la instancia
	hm = heatmap.Heatmap()

	# Creacion de la lista
	pts = []

	for tupla in ObjetosAnalisis_01:
		if tupla[2]<= minimo: minimo = tupla[2]
		if tupla[2]>= maximo: maximo = tupla[2]

	# Creacion de la lista con los puntos
	for tupla in ObjetosAnalisis_01:

		# Normalizacion para el mapa de calor
		norm = int(  10/float(maximo-minimo)*(tupla[2]-minimo) ) + 1  
		for i in range(norm):
			# Se invierte a: Primero longitudes y luego latitudes
			pts.append(( tupla[1],tupla[0]  ))

	# Inclusion de los puntos
	hm.heatmap(pts, scheme = 'classic', opacity = 120, dotsize = 80)
	# Creacion del archivo con el mapa de calor
	hm.saveKML(nombre_mapa_calor+".kml")

	return maximo,minimo

####################################################################################################
# FUNCION QUE AYUDA A ORDENAR MAS LA CONSULTA
####################################################################################################

def consulta(indice_dia,hora):

	consulta = 'SELECT TABLA02.LATITUD, TABLA02.LONGITUD, COUNT(TABLA02.NUM_VORONOI), TABLA02.NUM_VORONOI \
	FROM ( SELECT Antenas_Limpio.LONGITUD, Antenas_Limpio.LATITUD , Antenas_Limpio.NUM_VORONOI \
		FROM Antenas_Limpio,( SELECT BTS_ID, TIME_START_CHARG , DATE_START_CHARG \
			FROM CDR_One_Limpio WHERE HOUR(TIME_START_CHARG) = '+str(hora)+' AND DAYOFWEEK(DATE_START_CHARG) = '+str(indice_dia)+' ) AS Tabla \
WHERE (Antenas_Limpio.BTS_ID = Tabla.BTS_ID AND Antenas_Limpio.REGION=13) ) AS TABLA02 GROUP BY TABLA02.NUM_VORONOI;'

	return consulta


####################################################################################################
# FUNCION PARA ESCRIBIR LAS LISTAS
####################################################################################################

# Esta funcion escribe propiamente tal
def escribir(listado,ubicacion,modo,indice_dia,hora):

	lista_encabezado=[]
	lista_frecuencias=[]

	# Si se esta partiendo el archivo:
	if modo =='w':
		# Se crea la instancia
		instancia_escribir = open(ubicacion, modo)
		# Se escribe primero el encabezado
		for elemento in listado:
			# Se va escribiendo el elemento
			# Se escribe el indice del dia (Domingo es 1), la hora, la frecuencia de llamados, y el numero de voronoi
			instancia_escribir.write( str(indice_dia)+','+str(hora)+','+str(elemento[2])+','+str(elemento[3])+ '\n')

	# Si no:
	elif modo =='a':
		# Se crea la instancia
		instancia_escribir = open(ubicacion, modo)
		# Se escribe primero el encabezado
		for elemento in listado:
			# Se va escribiendo el elemento
			# Se escribe el indice del dia (Domingo es 1), la hora, la frecuencia de llamados, y el numero de voronoi
			instancia_escribir.write( str(indice_dia)+','+str(hora)+','+str(elemento[2])+','+str(elemento[3])+ '\n')

	# Se cierra la instancia
	instancia_escribir.close()


# Esta funcion chequea si el archivo ya existe
def escribir_informe(listado, ubicacion,indice_dia,hora):
	# Si el archivo existe, se empieza a escribir al final, si no se crea uno nuevo
	try:
		with open(ubicacion): escribir(listado,ubicacion,'a',indice_dia,hora)
	except IOError:
		escribir(listado,ubicacion,'w',indice_dia,hora)



####################################################################################################
# SCRIPT PRINCIPAL
####################################################################################################

# TIMESTAMP
now=datetime.now()
print('\n')
print('Tiempo de inicio')
print(now)

# Se abre la coneccion a la base de datos
db=MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "eadh5148", db = "mobility", port=5029 )
#db=MySQLdb.connect(host = "192.168.1.103", user = "root", passwd = "eadh5148", db = "mobility", port=5029 )
#db=MySQLdb.connect(host = "localhost", user = "root", passwd = "eadh5148", db = "mobility", port=5029 )


# Se crea el cursos	
c = db.cursor() 

# Los maximos y minimos estimados
maximo_general = 40912
minimo_general = 1


for indice_dia in range(1,8):
	for hora in range(0,24):

		# Se ejecuta una consulta
		c.execute( consulta(indice_dia,hora) )

		# se pasa la consuta a un listado entendible
		listado_BaseDatos = c.fetchall()

		# Si se escogio como opcion el escribir un TXT
		if args.escribirTXT:
			# Se escribe el listado en un archivo
			ubicacion = '/media/discoExternoRAID/raul/Python/Resultados_Santiago_Semana_tipo.csv'
			escribir_informe(sorted(listado_BaseDatos, key=lambda listado_BaseDatos: listado_BaseDatos[3]), ubicacion , indice_dia , hora)

		# Si se escogio como opcion el crear archivos KML
		if args.graficarKML:
			# declaracion del nombre
			nombre_mapa_calor = 'dia'+str(indice_dia)+'hora'+str(hora)
			# se crea el mapa de calor
			maximo, minimo= mapa_de_calor(listado_BaseDatos, nombre_mapa_calor, maximo_general, minimo_general)

		# Si hay nuevos valores
		if minimo <= minimo_general: minimo_general = minimo
		if maximo >= maximo_general: maximo_general = maximo


	# Punto de control externo
	print("")
	print("Dia: "+str(indice_dia)+" terminado")
	# TIMESTAMP
	now=datetime.now()
	print('\n')
	print('Tiempo de inicio')
	print(now)


print("")
print("maximo_general")
print(maximo_general)

print("")
print("minimo_general")
print(minimo_general)

# TIMESTAMP
now=datetime.now()
print('\n')
print('Tiempo de inicio')
print(now)
