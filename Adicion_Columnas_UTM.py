"""El siguiente SCRIPT lee el archivo especificado, el cual contiene coordenadas angulares y las transforma luego
en coordenadas UTM. Ademas de agregar una columna al PUNREF (PUnto de REFerencia)."""


####################################################################################################
# LIBRERIAS
####################################################################################################
# Para el calculo de distancias
from pyproj import Geod

# Para el calculo de UTMS
from pyproj import Proj

####################################################################################################
# FUNCION EXTRACTORA DE CAMPOS
####################################################################################################
def extractor_de_campo( linea = 'columna01,columna02,columna03' , numero_de_campo = 1 , separador = "," , tipo = "str"):
	"""La siguiente funcion lee caracter por caracter el String, identificando el inicio y fin de un campo, en base a un separados.
		Luego la funcion devuelve el campo."""


	# Numero de campo en que se parte
	num_campo_iteracion = 1

	# El campo que se busca
	campo = ""

	# Luego se realiza un recorrido de los caracteres
	for num_caracter in range(len(linea)):

		# Se se esta viendo un caracter en el numero de campo correspondiente
		if (num_campo_iteracion == numero_de_campo) and (linea[num_caracter] != separador):

			# Se agrega el caracter
			campo+=linea[num_caracter]

		# Si se identifica un caracter separador, este se cuenta
		if (linea[num_caracter] == separador):

			# Se adiciona 1 campo
			num_campo_iteracion+=1

	# Se da el formato seleccionado		
	if tipo == "float": campo = float(campo)

	# Se da el formato seleccionado		
	if tipo == "int": campo = int(campo)
	
	return campo

####################################################################################################
# SCRIPT PRINCIPAL
####################################################################################################
# Designacion de camino de origen y destino
ubicacion_original = '/media/discoExternoRAID/raul/listadoAntenas.csv'
ubicacion_destino = '/media/discoExternoRAID/raul/listadoAntenas_Final.csv'

leer = open(ubicacion_original, 'r')
# Abre el archivo a escribir
escribir = open(ubicacion_destino, 'w')

# Lee 'la' linea
linea = str(leer.readline())

# Se crea la instancia que calculara las distancias
g = Geod(ellps='WGS84')

# Se crea la instancia para el calculo de los UTM
p = Proj(proj='utm',zone=19,ellps='WGS84')

# Se lee el resto de las lineas
while 1:
	# Se lee la linea siguiente
	linea=str(leer.readline())
	# Si no hay mas lineas se termina todo
	if not linea: break

	# Si la linea corresponde a una antena en la RM
	if linea[1:3] == '13':

		# Extraccion de datos relevantes
		region = extractor_de_campo( linea , 1 )
		BTS = extractor_de_campo( linea , 2 )
		torre = extractor_de_campo( linea , 3 )
		longitud = extractor_de_campo( linea , 4, tipo = "float" )
		latitud = extractor_de_campo( linea , 5 , tipo = "float" )
		campo_06 = extractor_de_campo( linea , 6 )
		campo_07 = extractor_de_campo( linea , 7 )
		campo_08 = extractor_de_campo( linea , 8 , tipo = "int")

		# Calculo de la distancia
		az12,az21, distancia = g.inv( longitud , latitud , -70.650459 , -33.437911 )

		# Calculo de las proyecciones
		x , y = p( longitud, latitud )

		# Creacion de la nueva linea
		linea= region +','+BTS+','+torre+','+str(longitud)+','+str(latitud)+','+campo_06+','+campo_07+','+str(campo_08)+','+str(x)+','+str(y)+','+str(distancia)+'\n'
		escribir.write(linea)

	else:

		# Extraccion de datos relevantes
		region = extractor_de_campo( linea , 1 )
		BTS = extractor_de_campo( linea , 2 )
		torre = extractor_de_campo( linea , 3 )
		longitud = extractor_de_campo( linea , 4, tipo = "float" )
		latitud = extractor_de_campo( linea , 5 , tipo = "float" )
		campo_06 = extractor_de_campo( linea , 6 )
		campo_07 = extractor_de_campo( linea , 7 )
		campo_08 = extractor_de_campo( linea , 8, tipo = "int" )

		# Si no pasa nada solo se agrega una coma
		linea=region +','+BTS+','+torre+','+str(longitud)+','+str(latitud)+','+campo_06+','+campo_07+','+str(campo_08)+','+''+','+''+','+''+'\n'
		escribir.write(linea)
	


leer.close()	
escribir.close()