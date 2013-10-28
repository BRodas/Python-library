####################################################################################################
# LIBRERIAS
####################################################################################################

# Trabajar MySQL
import MySQLdb

# Se importa la libreria que permite tratamiento de fechas
from datetime import date,timedelta,datetime

# chequeador de punto interior
from lib_python import punto_en_poligono





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
# CODIGO
####################################################################################################

# Se abre la coneccion a la base de datos
db=MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "eadh5148", db = "mobility", port=5029 )
BaseDatos = db.cursor()

# Consultas
consulta_locales = "SELECT * FROM FOURSQUARE;"
consulta_ubicaciones_Santiago = 'SELECT NUM_VORONOI FROM Antenas WHERE REGION = 13 GROUP BY NUM_VORONOI';

# Extraccion de la info
BaseDatos.execute(consulta_locales)
listado_locales = list(BaseDatos.fetchall())

BaseDatos.execute(consulta_ubicaciones_Santiago)
listado_voronoi_santiago = list( BaseDatos.fetchall())
listado_voronoi_santiago_ordenado = []
# Ordenamiento del listado
for numero_region_voronoi in listado_voronoi_santiago:
	listado_voronoi_santiago_ordenado.append(numero_region_voronoi[0])
# Se ordena la lista
listado_voronoi_santiago_ordenado = sorted(listado_voronoi_santiago_ordenado)

# Se abre el archivo donde se escribira
Escribir = open('/media/discoExternoRAID/raul/Python/Resultados/foursquare.csv', 'w')

print(" Cantidad de regiones de Voronoi")
print(len(listado_voronoi_santiago))
print("\n")
print("inicio")
print(listado_voronoi_santiago_ordenado[0])
print("fin")
print(listado_voronoi_santiago_ordenado[-1])
print("\n")


# Recorrido por las regiones voronoi de Santiago
for numero_region_voronoi in listado_voronoi_santiago_ordenado:

	print "numero region de voronoi"
	print listado_voronoi_santiago_ordenado.index(numero_region_voronoi)
	print "\n"

	# Se extraen los vertices de la region voronoi
	consulta_voronoi_Vertices = 'SELECT * FROM VORONOI WHERE NUM_VORONOI = '+str(numero_region_voronoi)+' ;'
	BaseDatos.execute(consulta_voronoi_Vertices)
	listado_voronoi_vertices = list(BaseDatos.fetchall())

	# Se reordenan las coordenadas de los vertices en un listado, para su proxima evaluacion
	listado_vertices = []
	for vertice in listado_voronoi_vertices:
		listado_vertices.append([vertice[4], vertice[5] ])


	# Se hace un loop, en la medida que hallan locales para revisar
	revisar = True

	print "Numero listado locales"	
	print len(listado_locales)
	print '\n'

	while revisar:

		
		# Se asume que no se encontrara ningun local dentro de la region de Voronoi
		revisar = False

		# Se recorren los locales foursquare evaluando cuales estan dentro de la region
		for local_foursquare in listado_locales:

			# A lo mejor hay un listado_vertices vacio
			try:
				# Se evalua si el local esta dentro del listado de vertices
				if punto_en_poligono.point_in_poly( local_foursquare[3] ,local_foursquare[2] , listado_vertices ):
					

					# Se encontro un local, por lo que se sigue revisando
					revisar = True

					# De ser asi se escribe la linea en el csv
					linea = lista_a_string(local_foursquare)+','+str(numero_region_voronoi)+'\n'
					Escribir.write(linea)
					# Este local se borra del listado
					borrar_local_de_lista = local_foursquare
					# Se rompe el "for" para borrar el local del listado
					break

			except IndexError:
				pass

		# Por si no llegase a existir la variable borrar_local_de_lista
		try:
			# Por si no esta el elemento en la lista
			try:
				# se borra el local del listado
				listado_locales.remove(borrar_local_de_lista)

			except ValueError:
				pass

		except NameError:
			pass
# Se cierra el archivo para escribir
Escribir.close()

