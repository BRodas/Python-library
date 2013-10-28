# RUTINA QUE CALCULA LAS DISTATNCIAS ENTRE VARIOS PUNTOS DADOS EN LONGITUD Y LATITUD

# se importa 'LecturaArchivo'. este es una libreria de funciones orientadas a la manipulacion de texto
from lib_python import LecturaArchivo , parseador

# Para trabajar con la linea de comando
import subprocess

# Distancia entre el punto al centro y uno de sus vecinos
from pyproj import Geod

# Para trabajar con decimales
from decimal import *

############################################################################################################################################################
# NUEVA RUTINA: ESTA PREGUNTA DESDE UNA CONSULTA MYSQL


# Codigo MySQL pre hecho
codigoMysql = 'echo "select BTS_ID, LATITUD, LONGITUD , TECNOLOGIA FROM Antenas_Indra WHERE Antenas_Indra.PROV="131" ;" | mysql-ib -uroot  mobility '
# Se toma la data desde lo que entrega la linea de comando
data =  subprocess.Popen( codigoMysql , shell = True, stdout=subprocess.PIPE ).communicate()[0]
# Se parsea el "string" y se entrega a la variable consulta
consulta = parseador.general(consulta = data, cantCampos = 4)


# Se realiza una separacion en base a la tecnologia, para ello se recorre el arreglo
listado_3G = []
listado_2G = []
for antena in consulta:
	# Si la tecnologia de la antenas es 3G
	if antena[3] == "3G":
		# Se guarda
		listado_3G.append(antena)
	# Si en cambio la tecnologia es 2G
	elif antena[3] == "2G":
		# Se guarda en otra lista
		listado_2G.append(antena)

consulta= []

print(len(listado_3G))
print('\n')
print(len(listado_2G))




# Se crea la instancia que calculara los resultados
g = Geod(ellps='bessel')

# Cantidad de distancias sobre un limite
cant_exc_3G=[0,0,0,0,0,0]
cant_exc_2G=[0,0,0,0,0,0]


# Este indice indica el inicio de donde se revisara la lista
inicio = 0
# Numerador y denominador
numerador = 0
denominador = 0

# Aqui se recorre la lista en dos dimensiones
print('\n')
print("% avance 3G")
for ind_fil in range(0, len(listado_3G)):

	if ind_fil%200==0:
		print(float(ind_fil)/len(listado_3G)*100)

	inicio+=1
	distancia_min = 10000000

	# Se recorre la lista en la segunda dimencion
	for ind_col in range( inicio , len(listado_3G) ):
		# Se calcula la distancia
		az12,az21, distancia = g.inv( Decimal(listado_3G[ind_fil][2]) , Decimal(listado_3G[ind_fil][1]) , Decimal(listado_3G[ind_col][2]) , Decimal(listado_3G[ind_col][1]) )
		if distancia > 1:
			distancia_min = min(distancia_min,distancia)

	# Para armar una especie de histograma
	#if distancia_min >= 2000: 
	#	cant_exc_3G[5] =cant_exc_3G[5] +1
	#elif 1600 <= distancia_min < 2000:
	#	cant_exc_3G[4] =cant_exc_3G[4] +1
	#elif 1600 <= distancia_min < 1600:
	#	cant_exc_3G[3] =cant_exc_3G[3] +1
	#elif 800 <= distancia_min < 1200:
	#	cant_exc_3G[2] =cant_exc_3G[2] +1
	#elif 400 <= distancia_min < 800:
	#	cant_exc_3G[1] =cant_exc_3G[1] +1
	#elif distancia_min < 400:
	#	cant_exc_3G[0] =cant_exc_3G[0] +1


	# Para armar una especie de histograma
	if distancia_min >= 5000: 
		cant_exc_3G[5] =cant_exc_3G[5] +1
	elif 4000 <= distancia_min < 5000:
		cant_exc_3G[4] =cant_exc_3G[4] +1
	elif 3000 <= distancia_min < 4000:
		cant_exc_3G[3] =cant_exc_3G[3] +1
	elif 2000 <= distancia_min < 3000:
		cant_exc_3G[2] =cant_exc_3G[2] +1
	elif 1000 <= distancia_min < 2000:
		cant_exc_3G[1] =cant_exc_3G[1] +1
	elif distancia_min < 1000:
		cant_exc_3G[0] =cant_exc_3G[0] +1

	# Se suma la distancia
	if distancia_min <= 1000000:
		numerador = numerador + distancia_min
		denominador+=1

dist_prom_3G = 0
if not denominador==0: dist_prom_3G = float(numerador)/denominador





# Este indice indica el inicio de donde se revisara la lista
inicio = 0
# Numerador y denominador
numerador = 0
denominador = 0

# Aqui se recorre la lista en dos dimensiones
print('\n')
print("% avance 2G")
for ind_fil in range(0, len(listado_2G)):

	if ind_fil%200==0:
		print(float(ind_fil)/len(listado_2G)*100)

	inicio+=1
	distancia_min = 10000000
	# Se recorre la lista en la segunda dimencion
	for ind_col in range( inicio , len(listado_2G) ):
		# Se calcula la distancia
		az12,az21, distancia = g.inv( Decimal(listado_2G[ind_fil][2]) , Decimal(listado_2G[ind_fil][1]) , Decimal(listado_2G[ind_col][2]) , Decimal(listado_2G[ind_col][1]) )
		if distancia > 1 :
			distancia_min = min(distancia_min,distancia)

	# Para armar una especie de histograma
	#if distancia_min >= 2000: 
	#	cant_exc_2G[5] =cant_exc_2G[5] +1
	#elif 1600 <= distancia_min < 2000:
	#	cant_exc_2G[4] =cant_exc_2G[4] +1
	#elif 1600 <= distancia_min < 1600:
	#	cant_exc_2G[3] =cant_exc_2G[3] +1
	#elif 800 <= distancia_min < 1200:
	#	cant_exc_2G[2] =cant_exc_2G[2] +1
	#elif 400 <= distancia_min < 800:
	#	cant_exc_2G[1] =cant_exc_2G[1] +1
	#elif distancia_min < 400:
	#	cant_exc_2G[0] =cant_exc_2G[0] +1


	# Para armar una especie de histograma
	if distancia_min >= 5000: 
		cant_exc_2G[5] =cant_exc_2G[5] +1
	elif 4000 <= distancia_min < 5000:
		cant_exc_2G[4] =cant_exc_2G[4] +1
	elif 3000 <= distancia_min < 4000:
		cant_exc_2G[3] =cant_exc_2G[3] +1
	elif 2000 <= distancia_min < 3000:
		cant_exc_2G[2] =cant_exc_2G[2] +1
	elif 1000 <= distancia_min < 2000:
		cant_exc_2G[1] =cant_exc_2G[1] +1
	elif distancia_min < 1000:
		cant_exc_2G[0] =cant_exc_2G[0] +1



	# Se suma la distancia
	if distancia_min <= 10000000:
		numerador = numerador + distancia_min
		denominador+=1


dist_prom_2G = 0
if not denominador==0: dist_prom_2G = float(numerador)/denominador




print('\n')
print('3G')
print(dist_prom_3G)
print('"histograma"')
print(cant_exc_3G)

print('\n')
print('2G')
print(dist_prom_2G)
print('"histograma"')
print(cant_exc_2G)











############################################################################################################################################################
# ANTIGUA RUTINA: LA CUAL USA UNA DIRECCION O CAMINO DENTRO DEL DISCO

if False:
	# el directorio que se trabajara
	Directorio='./Resultados/AntenasTecnologia.txt'

	# Se pone el archivo en un arreglo
	Archivo = LecturaArchivo.leer(Directorio)

	# Ya que es una tabla con encabezado el archivo, este se lleva a un diccionario
	DatosOrdenado = LecturaArchivo.DicionarioTabla(Archivo)


	# Ya que la tabla que he importado de "Directorio" se que contiene numeros con 'coma' y cuales son, los voy a transformar en 'punto'
	limite = len(DatosOrdenado['LATITUD'])
	i=0
	while i<limite:
		DatosOrdenado['LATITUD'][i] = DatosOrdenado['LATITUD'][i].replace(',','.')
		DatosOrdenado['LONGITUDE'][i] = DatosOrdenado['LONGITUDE'][i].replace(',','.')
		i=i+1

	# Transformacion de 'srt' en 'float'
	i=0

	while i<limite:
		DatosOrdenado['LATITUD'][i] = float(DatosOrdenado['LATITUD'][i])
		DatosOrdenado['LONGITUDE'][i] = float(DatosOrdenado['LONGITUDE'][i])
		i=i+1



	# Calculo de distancias entre puntos (longitud y latitud)
	# libreria que calcula las distancias entre los puntos
	# OBS: de la trilogia de datos no se cuales son los dos primeros: (az12,az21,dist)
	from pyproj import Geod
	g = Geod(ellps='bessel')
	matriz=[]
	fila=''
	i=0
	j=0
	# Creacion del encabezado
	while i<limite:
		fila = fila+'\t'+str(i+1)
		i=i+1
	fila = fila+'\r\n'
	matriz.append(fila)

	# Llenado del resto
	i=0
	while i<limite:
		j=0
		fila=''
		while j<limite:
			az12,az21,dist = g.inv(DatosOrdenado['LONGITUDE'][i],DatosOrdenado['LATITUD'][i],DatosOrdenado['LONGITUDE'][j],DatosOrdenado['LATITUD'][j])
			dist= str(dist/1000)
			if i==j: dist=str('99999999')		
			fila = fila+'\t'+dist		
			j=j+1

		fila = fila+'\r\n'
		matriz.append(fila)
		i=i+1

	# Agregacion de la columna 1
	i=0
	while i<limite:
		matriz[i+1]=str(i+1)+matriz[i+1]
		i=i+1



	# Escritura de archivos
	UbicacionArchivo = '/home/bernardo/Desktop/PYT_Python/DistAntenas.INC'
	LecturaArchivo.escribir(matriz,UbicacionArchivo)

############################################################################################################################################################
