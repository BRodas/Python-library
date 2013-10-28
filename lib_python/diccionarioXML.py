from datetime import date,timedelta

#############################################################################


def fBloqueDias( bloquedias = {'01_LuMaMi': [1,3],'02_Ju':[4,4] ,'03_Vi':[5,5] ,'04_Sa':[6,6] ,'05_Do': [7,7]} ):
	"""esta funcion se ocupa de manera auxiliar. Es solo para retornat los bloques de dias"""

	Bloque_Dias = bloquedias


	return Bloque_Dias


#############################################################################

# Bloque por cada 20 minutos
def funcionBloques( bloquehorario = { 'Bloque01':[timedelta(0,0	),timedelta(0,	1200	)],'Bloque02':[timedelta(0,1200	),timedelta(0,	2400	)],'Bloque03':[timedelta(0,2400	),timedelta(0,	3600	)],'Bloque04':[timedelta(0,3600	),timedelta(0,	4800	)],'Bloque05':[timedelta(0,4800	),timedelta(0,	6000	)],'Bloque06':[timedelta(0,6000	),timedelta(0,	7200	)],'Bloque07':[timedelta(0,7200	),timedelta(0,	8400	)],'Bloque08':[timedelta(0,8400	),timedelta(0,	9600	)],'Bloque09':[timedelta(0,9600	),timedelta(0,	10800	)],'Bloque10':[timedelta(0,10800	),timedelta(0,	12000	)],'Bloque11':[timedelta(0,12000	),timedelta(0,	13200	)],'Bloque12':[timedelta(0,13200	),timedelta(0,	14400	)],'Bloque13':[timedelta(0,14400	),timedelta(0,	15600	)],'Bloque14':[timedelta(0,15600	),timedelta(0,	16800	)],'Bloque15':[timedelta(0,16800	),timedelta(0,	18000	)],'Bloque16':[timedelta(0,18000	),timedelta(0,	19200	)],'Bloque17':[timedelta(0,19200	),timedelta(0,	20400	)],'Bloque18':[timedelta(0,20400	),timedelta(0,	21600	)],'Bloque19':[timedelta(0,21600	),timedelta(0,	22800	)],'Bloque20':[timedelta(0,22800	),timedelta(0,	24000	)],'Bloque21':[timedelta(0,24000	),timedelta(0,	25200	)],'Bloque22':[timedelta(0,25200	),timedelta(0,	26400	)],'Bloque23':[timedelta(0,26400	),timedelta(0,	27600	)],'Bloque24':[timedelta(0,27600	),timedelta(0,	28800	)],'Bloque25':[timedelta(0,28800	),timedelta(0,	30000	)],'Bloque26':[timedelta(0,30000	),timedelta(0,	31200	)],'Bloque27':[timedelta(0,31200	),timedelta(0,	32400	)],'Bloque28':[timedelta(0,32400	),timedelta(0,	33600	)],'Bloque29':[timedelta(0,33600	),timedelta(0,	34800	)],'Bloque30':[timedelta(0,34800	),timedelta(0,	36000	)],'Bloque31':[timedelta(0,36000	),timedelta(0,	37200	)],'Bloque32':[timedelta(0,37200	),timedelta(0,	38400	)],'Bloque33':[timedelta(0,38400	),timedelta(0,	39600	)],'Bloque34':[timedelta(0,39600	),timedelta(0,	40800	)],'Bloque35':[timedelta(0,40800	),timedelta(0,	42000	)],'Bloque36':[timedelta(0,42000	),timedelta(0,	43200	)],'Bloque37':[timedelta(0,43200	),timedelta(0,	44400	)],'Bloque38':[timedelta(0,44400	),timedelta(0,	45600	)],'Bloque39':[timedelta(0,45600	),timedelta(0,	46800	)],'Bloque40':[timedelta(0,46800	),timedelta(0,	48000	)],'Bloque41':[timedelta(0,48000	),timedelta(0,	49200	)],'Bloque42':[timedelta(0,49200	),timedelta(0,	50400	)],'Bloque43':[timedelta(0,50400	),timedelta(0,	51600	)],'Bloque44':[timedelta(0,51600	),timedelta(0,	52800	)],'Bloque45':[timedelta(0,52800	),timedelta(0,	54000	)],'Bloque46':[timedelta(0,54000	),timedelta(0,	55200	)],'Bloque47':[timedelta(0,55200	),timedelta(0,	56400	)],'Bloque48':[timedelta(0,56400	),timedelta(0,	57600	)],'Bloque49':[timedelta(0,57600	),timedelta(0,	58800	)],'Bloque50':[timedelta(0,58800	),timedelta(0,	60000	)],'Bloque51':[timedelta(0,60000	),timedelta(0,	61200	)],'Bloque52':[timedelta(0,61200	),timedelta(0,	62400	)],'Bloque53':[timedelta(0,62400	),timedelta(0,	63600	)],'Bloque54':[timedelta(0,63600	),timedelta(0,	64800	)],'Bloque55':[timedelta(0,64800	),timedelta(0,	66000	)],'Bloque56':[timedelta(0,66000	),timedelta(0,	67200	)],'Bloque57':[timedelta(0,67200	),timedelta(0,	68400	)],'Bloque58':[timedelta(0,68400	),timedelta(0,	69600	)],'Bloque59':[timedelta(0,69600	),timedelta(0,	70800	)],'Bloque60':[timedelta(0,70800	),timedelta(0,	72000	)],'Bloque61':[timedelta(0,72000	),timedelta(0,	73200	)],'Bloque62':[timedelta(0,73200	),timedelta(0,	74400	)],'Bloque63':[timedelta(0,74400	),timedelta(0,	75600	)],'Bloque64':[timedelta(0,75600	),timedelta(0,	76800	)],'Bloque65':[timedelta(0,76800	),timedelta(0,	78000	)],'Bloque66':[timedelta(0,78000	),timedelta(0,	79200	)],'Bloque67':[timedelta(0,79200	),timedelta(0,	80400	)],'Bloque68':[timedelta(0,80400	),timedelta(0,	81600	)],'Bloque69':[timedelta(0,81600	),timedelta(0,	82800	)],'Bloque70':[timedelta(0,82800	),timedelta(0,	84000	)],'Bloque71':[timedelta(0,84000	),timedelta(0,	85200	)],'Bloque72':[timedelta(0,85200	),timedelta(0,	86400	)] } ):


# Bloque de 1 dia
#def funcionBloques( bloquehorario = { 'Bloque01': [timedelta(0,1),timedelta(0, 86399 )] } ):

# Bloque por cada hora
#def funcionBloques( bloquehorario = { 'Bloque01': [timedelta(0,0), timedelta(0 , 3600)], 'Bloque02' : [timedelta(0, 3601 ), timedelta(0,7200)] ,  'Bloque03': [timedelta(0,7201),timedelta(0,10800)] , 'Bloque04':[timedelta(0,10801),timedelta(0,14400)] , 'Bloque05':[timedelta(0,14401),timedelta(0,18000)] , 'Bloque06':[timedelta(0, 18001),timedelta(0, 21600)] , 'Bloque07':[timedelta(0, 21601),timedelta(0, 25200)] , 'Bloque08':[timedelta(0, 25201),timedelta(0, 28800)], 'Bloque09':[timedelta(0, 28801 ),timedelta(0, 32400 )], 'Bloque10':[timedelta(0, 32401 ),timedelta(0, 36000 )], 'Bloque11':[timedelta(0, 36001 ),timedelta(0, 39600 )], 'Bloque12':[timedelta(0, 39601),timedelta(0, 43200 )], 'Bloque13':[timedelta(0, 43201 ),timedelta(0, 46800 )], 'Bloque14':[timedelta(0, 46801 ),timedelta(0, 50400 )], 'Bloque15':[timedelta(0, 50401 ),timedelta(0, 54000 )], 'Bloque16':[timedelta(0, 54001 ),timedelta(0, 57600 )], 'Bloque17':[timedelta(0, 57601 ),timedelta(0, 61200 )], 'Bloque18':[timedelta(0, 61201 ),timedelta(0, 64800 )], 'Bloque19':[timedelta(0, 64801 ),timedelta(0, 68400 )], 'Bloque20':[timedelta(0, 68401 ),timedelta(0, 72000 )], 'Bloque21':[timedelta(0, 72001 ),timedelta(0, 75600 )], 'Bloque22':[timedelta(0, 75601 ),timedelta(0, 79200 )], 'Bloque23':[timedelta(0, 79201 ),timedelta(0, 82800 )], 'Bloque24':[timedelta(0, 82801 ),timedelta(0, 86400 )] } ):

# Bloques definidos con Movistar
#def funcionBloques( bloquehorario = { 'Bloque06': [timedelta(0,0), timedelta(0, 21600)] , 'Bloque10':[timedelta(0, 21601), timedelta(0, 36000 )], 'Bloque13':[timedelta(0, 36001 ), timedelta(0, 46800 )], 'Bloque15':[timedelta(0, 46801 ), timedelta(0, 54000 )], 'Bloque18,5':[timedelta(0, 54001 ), timedelta(0, 66600 )], 'Bloque21,5':[timedelta(0, 66601 ), timedelta(0, 77400 )], 'Bloque24':[timedelta(0, 79201 ), timedelta(0, 86400 )] } ):
	"""esta funcion se ocupa de manera auxiliar, es solo para retornar los bloques horarios"""



	# Aqui se define el segundo nivel de orden, los bloques
	Bloques = bloquehorario

	return Bloques






#####################################################################################################################################################
# Clase OPTICS
class ClaseOptics:

	# La funcion inicializadora
	def __init__(self, listadoTuplas = [ (0,'', date(2012,11,1) , timedelta(0,0) , -33.4560600000 ,  -33.4560600000  )  , (0,'',date(2012,11,1), timedelta(0,0),  -33.4560600000,  -33.4560600000  ) ] , Distancia = 3000 ,  MinPts = 5  ):

		# Se define el atributo ".DiccionarioOptics"
		
		self.DiccionarioOptics = fOPTICS(listadoTuplas,Distancia,MinPts)


		# Recorrido del diccionario, ya que el ULTIMO ELEMENTO de la LISTA final es el CENTROIDE
		# Se define el atributo con el diccionario de centroides
		self.CentroidesOptics = {}
		# Se define un listado de tuplas que contendra SOLO los CENTROIDES
		listadoOPTICS =[]

		
		# Recorrido por los distintos niveles OPTICS, para crear "self.CentroidesOptics"
		for Niv01 , ValNiv01 in self.DiccionarioOptics.iteritems() :
			# Segundo nivel de recorrido
			for Niv02 , ValNiv02 in ValNiv01.iteritems():
				# Se recorre el tercer nivel
				for Niv03 , listado in ValNiv02.iteritems() :
					# Si no es ruido se agrega a un listado los datos del centroide
					if (not Niv03=='ruido') and (not self.DiccionarioOptics[Niv01][Niv02][Niv03][-1]==[]):
						# Si CentroidesOptics no tiene la llave, la crea
						if  not self.CentroidesOptics.has_key(Niv01) : self.CentroidesOptics[Niv01]={}
						# Si CentroidesOpticss no tiene la segunda llave, la crea
						if not self.CentroidesOptics[Niv01].has_key(Niv02) : self.CentroidesOptics[Niv01][Niv02]={}
						# Si CentroidesOpticss no tiene la tercera llave, la crea
						if not self.CentroidesOptics[Niv01][Niv02].has_key(Niv03) : self.CentroidesOptics[Niv01][Niv02][Niv03]=[]
						self.CentroidesOptics[Niv01][Niv02][Niv03].append(self.DiccionarioOptics[Niv01][Niv02][Niv03][-1])
						

						# Estas lineas se hacen pensando en el optics que se aplicara a los clusters formados
						
						# A continuacion se arma un listado con las coordenadas que arman un cluster sin repetirlas
						listadoCoordenadas=[]
						for elemento in self.DiccionarioOptics[Niv01][Niv02][Niv03][:-1]:
							coordenadas=(elemento[2],elemento[3])
							listadoCoordenadas.append(coordenadas)						
						listadoCoordenadas = list(set(listadoCoordenadas))
						
						# Aqui se entregan las coordenadas del centroide
						latitud = self.DiccionarioOptics[Niv01][Niv02][Niv03][-1][0]
						longitud = self.DiccionarioOptics[Niv01][Niv02][Niv03][-1][1]
						# listadoCoordenadas: es el LISTADO de las TUPLAS (lat,lon) SIN REPETIR que arman EL CENTROIDE 
						tupla = ('','', date(2013,01,23), timedelta(0, 0),latitud,longitud, listadoCoordenadas)
						listadoOPTICS.append(tupla)

				# Antes de continuar con el liguiente nivel corre un Optics




		# Se importa la libreria OPTICS
		import OPTICS
		# A continuacion se calcula el centroide de los centroides.

		conjuntoObjetos = OPTICS.SetOfObjects( listadoOPTICS )
		resultadoAlg = OPTICS.FOptics(conjuntoObjetos , Distancia ,  0  )

		self.Centroides_CentroidesOptics=[]
		# Si el listado no es vacio y tiene mas de dos elementos
		numeroAntenas=0
		self.histograma = [0]*100

		if not resultadoAlg == [] and len(resultadoAlg) > 1:
			i=0

			# i es un condator de la lista "listado"
			while i <= len(resultadoAlg)-1:

				# Se crea una lista vacia donde se van metiendo los clusters
				bolsa = []
				listadoAntenas=[]


				# Se agrega el primer elemento de la lista a la bolsa
				bolsa.append(resultadoAlg[i])

				coordenada01=(resultadoAlg[i][2],resultadoAlg[i][3])
			
				for elemento in listadoOPTICS:
					coordenada02 = (elemento[4],elemento[5])
					if coordenada01==coordenada02:
						# Agregar al listado de antenas
						for coordAntenas in elemento[6]:
							listadoAntenas.append(coordAntenas)


				# Se pasa al siguiente elemento
				i+=1

				# Si no se esta fuera de los elementos de la lista y la distancia del siguiente elemento es menor a la Reachability Distance
				while ( i<=len(resultadoAlg)-1 ) and ( resultadoAlg[i][4] <= Distancia ):

					coordenada01=(resultadoAlg[i][2],resultadoAlg[i][3])
					
					for elemento in listadoOPTICS:
						coordenada02 = (elemento[4],elemento[5])
						if coordenada01==coordenada02:
							# Agregar al listado de antenas
							for coordAntenas in elemento[6]:
								listadoAntenas.append(coordAntenas)

					

					# Se agrega el elemento a la bolsa
					bolsa.append(resultadoAlg[i])

					# Y se para al siguiente elemento
					i+=1

				# Si la bolsa termino con mas de 1 elemento
				if len(bolsa) > 1 :

					# Se agrega el centroide
					centroMasa = centroide(bolsa)
					self.Centroides_CentroidesOptics.append(centroMasa)


					listadoAntenas = list(set(listadoAntenas))
					numeroAntenas = len(listadoAntenas)
					self.histograma[numeroAntenas]+=1


				# Si la bolsa termino con solo 1 elemento
				else:

					centroMasa = centroide(bolsa)
					self.Centroides_CentroidesOptics.append(centroMasa)

					listadoAntenas = list(set(listadoAntenas))
					numeroAntenas = len(listadoAntenas)
					self.histograma[numeroAntenas]+=1

		print('\n'+"Histograma: numero de antenas (posicion de la lista, partiendo de 1) vs frecuencia")
		print(self.histograma[1:10])



###########################################################################################################################################################
# Mon 18 Mar 2013 02:07:02 PM CLT Funcion generadora del diccionario para OPTICS

def fOPTICS( listadoTuplas = [ (0,'', date(2012,11,1) , timedelta(0,0) , -33.4560600000 ,  -33.4560600000  )  , (0,'',date(2012,11,1), timedelta(0,0),  -33.4560600000,  -33.4560600000  ) ] , Distancia = 3000 ,  MinPts = 5  ):
	"""Esta funcion recibe el listado de las tuplas. Cada tupla es un registro."""

	# Declaracion del diccionario de dias
	Dic_Bloq_Dia = fBloqueDias( bloquedias = {'01_Lu':[1,1], '02_Ma':[2,2] , '03_Mi': [3,3],'04_Ju':[4,4] ,'05_Vi':[5,5] ,'06_Sa':[6,6] ,'07_Do': [7,7]} )

	# Declaracion del diccionario de horas
	Dic_Bloq_Hor = funcionBloques()


	# Aqui se crea el diccionario
	diccionarioOPTICS = {}
	diccionarioOPTICS_02 = {}
	# Aqui se arma el diccionario "diccionarioCentroides", pero VACIO. 
	for bloqDias , contenido01 in Dic_Bloq_Dia.iteritems():
		# Con esta linea se crean los indices correspondiente al dia
		diccionarioOPTICS[bloqDias] = {}
		diccionarioOPTICS_02[bloqDias] = {}
		# Aqui se recorren los bloques horarios
		for bloqHoras , contenido02 in Dic_Bloq_Hor.iteritems():
			# Aqui se crean los indices correspondientes al bloque horario
			diccionarioOPTICS[bloqDias][bloqHoras] = []
			diccionarioOPTICS_02[bloqDias][bloqHoras] = {}


	
	# Llenado del diccionario.
	for fila in listadoTuplas:
		fecha = fila[2]
		hora = fila[3]

		# Recorrido del diccionario, cosa de ir llenarlo. El primer nivel de recorrido son los dias.	
		for Niv01 , ValNiv01 in Dic_Bloq_Dia.iteritems():
			# El segundo nivel de recorrido son los bloques horarios.
			for Niv02, ValNiv02 in Dic_Bloq_Hor.iteritems():
				# Si en la pagina que se esta viendo del diccionario "diccionarioCentroides" los valores del registro corresponden entonces se agregan las coordenadas.
				if	( ValNiv01[0] <= fecha.isoweekday() <= ValNiv01[-1] )	and ( ValNiv02[0].seconds <= hora.seconds <= ValNiv02[-1].seconds ):

					diccionarioOPTICS[Niv01][Niv02].append(fila)		




	# Se ejecutara el algoritmo OPTICS por cada dia (Lunes, Martes, Miercoles, Jueves, Viernes, Sabado, Domingo) y por cada hora (0, 1, 2, 3,...)
	import OPTICS

	# Comienza con el recorrido del diccionario
	for Niv01 , ValNiv01 in Dic_Bloq_Dia.iteritems():
		# El segundo nivel de recorrido son los bloques horarios.
		for Niv02, ValNiv02 in Dic_Bloq_Hor.iteritems():

			# Se aplica el algoritmo OPTICS

			listadoOPTICS = diccionarioOPTICS[Niv01][Niv02]
			numeroUsuario = str(listadoTuplas[0][0])
			conjuntoObjetos = OPTICS.SetOfObjects( listadoOPTICS )
			resultadoAlg = OPTICS.FOptics(conjuntoObjetos , Distancia ,  MinPts  ) 
			diccionarioOPTICS[Niv01][Niv02] = resultadoAlg



	# Reordenacion del DICCIONARIO OPTICS
	# Se recorren los dias
	for Dia, Horas in diccionarioOPTICS.iteritems():
		# Luego se recorren los bloques horarios
		for bloques, listado in Horas.iteritems():

			# Si el listado no es vacio y tiene mas de dos elementos
			if not listado == [] and len(listado) > 1:
				i=0

				# i es un condator de la lista "listado"
				while i <= len(listado)-1:

					# Se crea una lista vacia donde se van metiendo los clusters
					bolsa = []

					# Se agrega el primer elemento de la lista a la bolsa
					bolsa.append(listado[i])

					# Se pasa al siguiente elemento
					i+=1

					# Si no se esta fuera de los elementos de la lista y la distancia del siguiente elemento es menor a la Reachability Distance
					while ( i<=len(listado)-1 ) and ( listado[i][4] <= Distancia ):

						# Se agrega el elemento a la bolsa
						bolsa.append(listado[i])

						# Y se para al siguiente elemento
						i+=1

					# Si la bolsa termino con mas de 1 elemento
					if len(bolsa) > 1 :

						# Se crea el cluster
						diccionarioOPTICS_02[Dia][bloques][str( float(len(bolsa))/len(listado)*100 )+str(i)+'%'] = bolsa

						# Se agrega el centroide
						centroMasa = centroide(bolsa)
						diccionarioOPTICS_02[Dia][bloques][str( float(len(bolsa))/len(listado)*100 )+str(i)+'%'].append(centroMasa)

					# Si la bolsa termino con solo 1 elemento
					else:

						# Se agrega a ruido, pero si ruido no existe, se crea
						if (not diccionarioOPTICS_02[Dia][bloques].has_key('ruido')): diccionarioOPTICS_02[Dia][bloques]['ruido']=[]
						diccionarioOPTICS_02[Dia][bloques]['ruido'].append(listado[i-1])

			# Se el listado no es vacio, pero tiene 1 solo elemento
			elif (not listado == []) and (len(listado) == 1):
				# Es ruido
				diccionarioOPTICS_02[Dia][bloques]['ruido'] = listado


	del diccionarioOPTICS

	#return diccionarioOPTICS
	return diccionarioOPTICS_02






#Importa la libreria para el tratamiento de Decimal('3.66')
from decimal import *

def centroide( listado = [  (date(2012, 11, 9), timedelta(0, 72757), Decimal('-33.4'), Decimal('-70.5'), 1000000, 571)  ,  (date(2012, 11, 9), timedelta(0, 73040), Decimal('-33'), Decimal('-70'), 571, 571)  ,  (date(2012, 11, 9), timedelta(0, 73320), Decimal('-33'), Decimal('-70'), 571, 571)  ,  (date(2012, 11, 9), timedelta(0, 73530), Decimal('-33'), Decimal('-70'), 571, 571)  ] ):
	"""Funcion interna de la funcion OPTICS para el calculo de centro de masa"""

	# Puesto que calcula los centroides
	# Importa la libreria de pyproj
	from pyproj import Proj

	# el transformador. de utm a lat/long, recordar agregar "inverse = 'true' "
	transformador = Proj( proj='utm', zone='19', ellps='WGS84' )	

	# Llenado del diccionario.
	sumaX = 0
	sumaY = 0

	# Recorre las tuplas del listado
	for tupla in listado:
		latitud = tupla[2]
		longitud = tupla[3]
		#Estos estan en metros
		x = transformador(longitud,latitud)[0]
		y = transformador(longitud,latitud)[1]

		# Va sumando las coordenadas UTM
		sumaX =	sumaX + x
		sumaY =	sumaY + y

	# Calcula el centro, dividiendo por la cantidad de puntos habidos en listado
	centroX = float(sumaX) / len(listado)
	centroY = float(sumaY) / len(listado)

	# Transforma de vuelta a coordenadas angulares los datos
	longitud = transformador(centroX,centroY,inverse='true')[0]
	latitud = transformador(centroX,centroY,inverse='true')[1]

	# Los mete en una tupla
	coordenadasCentro = ( latitud , longitud )

	return coordenadasCentro


###########################################################################################################################################################




def fecha_bloque(ListadoDeListas):
	""" Armado del diccionario 'fecha_bloque', el orden de cada fila es:  
		NUMBER_CELLPHONE , 
		BTS_ID , 
		DATE_START_CHARG (Indices primarios del diccionario) , 	
		TIME_START_CHARG (Indice secundario, se organizan luego en bloque), 
		LATITUD , 
		LONGITUD """


	# Este diccionario es donde se meten los datos, es el primer nivel de orden
	CDR_Fecha = {}
	
	# Aqui se define el segundo nivel de orden, los bloques, los cuales son una funcion.
	intBloques = funcionBloques()



	# Se revisa fila por fila la tabla entregada. Cada fila "row" es una lista de python
	for row in ListadoDeListas:

		# Por algo de legibilidad se realiza este paso
		fecha = str(row[2])

		# Se chequea si es que el diccionario contiene la fecha consultada
		if CDR_Fecha.has_key(fecha):

			# Se hace un recorrido por los bloques horarios definidos anteriormente en el diccionario intBloques
			for key, interv in intBloques.iteritems():
			
				# Este cambio de variable es para mejorar la legibilidad
				hora = row[3]

				# Con este "if" se verifica si la hora del CDR esta dentro del bloque
				if interv[0] <= hora and interv[1] >=hora:
			
					# Esta variable es el limite superior del bloque horario.
					bloque = key
			
					# Si no existe dentro de la "fecha" el bloque horario se crea.
					if not CDR_Fecha[fecha].has_key(bloque): 			CDR_Fecha[fecha][bloque] = []
				
					# Ya que en el diccionario existe fecha y un bloque horario se incluyen los datos correspondientes.
					registro = []
					registro.append(row[1])
					registro.append(row[3:6])
					CDR_Fecha[fecha][bloque].append(registro)
					#CDR_Fecha[fecha][bloque].append(row[1])
					#CDR_Fecha[fecha][bloque].append(row[3:6])

		# Ya que el diccionario NO contiene la fecha consultada
		else:
		
			# Se crea el diccionario en el diccionario
			CDR_Fecha[fecha]={}

			# Se recorre el diccionario
			for key, interv in intBloques.iteritems():
			
				# Este cambio de variable es para mejorar la legibilidad
				hora = row[3]

				# Si el CDR esta en el bloque
				if interv[0] <= hora and interv[1] >= hora :

					# Bloque horario
					bloque = key

					# Ya que en el diccionario existe fecha y un bloque horario se incluyen los datos correspondientes.
					CDR_Fecha[fecha][bloque] = []
					registro = []
					registro.append(row[1])
					registro.append(row[3:6])
					CDR_Fecha[fecha][bloque].append(registro)
					#CDR_Fecha[fecha][bloque].append(row[1])
					#CDR_Fecha[fecha][bloque].append(row[3:6])
					

	#Recorrido por fecha
	
	return CDR_Fecha




#############################################################################




def bloque_fecha(consulta):
	""" Armado del diccionario 'fecha_bloque', el orden de cada fila es:  
		NUMBER_CELLPHONE , 
		BTS_ID , 
		DATE_START_CHARG (Indices primarios del diccionario) , 	
		TIME_START_CHARG (Indice secundario, se organizan luego en bloque), 
		LATITUD , 
		LONGITUD """


# Aqui se define el primer nivel de orden, los bloques. Esto es modificable.
	intBloques = funcionBloques()


	# Este diccionario es donde se meten los datos, es el primer nivel de orden
	Diccionario = {}

	# Se revisa fila por fila la tabla entregada. Cada fila "row" es una lista de python

	for row in consulta:
		
		# Este cambio de variable es para mejorar la legibilidad
		hora = row[3]	
		fecha = str(row[2])

		# Se hace un recorrido por los bloques horarios definidos anteriormente en el diccionario intBloques
		for key, interv in intBloques.iteritems():
		
			# Con este "if" se verifica si la hora del CDR esta dentro del bloque
			if interv[0] <= hora and interv[1] >=hora:
			
				#bloque = str(interv[0])[0:5]+'-'+str(interv[1])[0:5]
				bloque = key

				if Diccionario.has_key(bloque):

					if Diccionario[bloque].has_key(fecha):
				
						registro=[]
						registro.append(row[1])
						registro.append(row[3:6])
						Diccionario[bloque][fecha].append(registro)

					else:
						Diccionario[bloque][fecha]=[]
						registro=[]
						registro.append(row[1])
						registro.append(row[3:6])
						Diccionario[bloque][fecha].append(registro)

				else:

					Diccionario[bloque] = {}

					if Diccionario[bloque].has_key(fecha):
						registro=[]
						registro.append(row[1])
						registro.append(row[3:6])
						Diccionario[bloque][fecha].append(registro)

					else:
						Diccionario[bloque][fecha]=[]
						registro=[]
						registro.append(row[1])
						registro.append(row[3:6])
						Diccionario[bloque][fecha].append(registro)


	return Diccionario




##################################################################################################################################################


def centroides( listadoTuplas = [ (0,'', date(2012,11,1) , timedelta(0,0) , -33.4560600000 ,  -33.4560600000  )  , (0,'',date(2012,11,1), timedelta(0,0),  -33.4560600000,  -33.4560600000  ) ]  ):
	"""Esta funcion transforma el listado de tuplas en un diccionario con los centroides por bloque y en coordenadas UTM"""

	# Importa la libreria de pyproj
	from pyproj import Proj
	import decimal

	# Aqui se importa el diccionario con los bloques horarios
	Dic_Bloq_Hor = funcionBloques()	

	# Aqui se importa el diccionario con los bloques de dias
	Dic_Bloq_Dia = fBloqueDias()

	# el transformador. de utm a lat/long, recordar agregar "inverse = 'true' "
	transformador = Proj( proj='utm', zone='19', ellps='WGS84' )

	# Aqui se crea el diccionario
	diccionarioCentroides = {}
	# Aqui se arma el diccionario "diccionarioCentroides", pero VACIO. 
	for bloqDias , contenido01 in Dic_Bloq_Dia.iteritems():
		# Con esta linea se crean los indices correspondiente al dia
		diccionarioCentroides[bloqDias] = {}
		# Aqui se recorren los bloques horarios
		for bloqHoras , contenido02 in Dic_Bloq_Hor.iteritems():
			# Aqui se crean los indices correspondientes al bloque horario
			diccionarioCentroides[bloqDias][bloqHoras] = []





	# Aqui se hace el llenado del diccionario, pero de manera ordenada. En la tupla coordenadas, el primer termino es la latitud, y luego la longitud.
	coordenadas = []


	# Llenado del diccionario.
	for fila in listadoTuplas:
		fecha = fila[2]
		hora = fila[3]
		latitud = fila[4]
		longitud = fila[5]
		#Estos estan en metros
		x = transformador(longitud,latitud)[0]
		y = transformador(longitud,latitud)[1]
		coordenadas=(x,y)		
		

		# Recorrido del diccionario, cosa de ir llenarlo. El primer nivel de recorrido son los dias.	
		for Niv01 , ValNiv01 in Dic_Bloq_Dia.iteritems():
			# El segundo nivel de recorrido son los bloques horarios.
			for Niv02, ValNiv02 in Dic_Bloq_Hor.iteritems():
				# Si en la pagina que se esta viendo del diccionario "diccionarioCentroides" los valores del registro corresponden entonces se agregan las coordenadas.
				if	( ValNiv01[0] <= fecha.isoweekday() <= ValNiv01[-1] )	and ( ValNiv02[0].seconds <= hora.seconds <= ValNiv02[-1].seconds ):	
					diccionarioCentroides[Niv01][Niv02].append(coordenadas)		

	# Hasta aqui el diccionarioCentroides esta ordenado por niveles y en su ultimo nivel tiene un listado con las coordenas en UTM. Puesto que la idea es calcular el centroide por cada bloque se realizan los siguientes pasos:
	# Se recorre el primer nivel
	for Niv01, Niv02 in diccionarioCentroides.iteritems():
		# Luego se recorre por cada primer nivel el segundo nivel
		for llave, valores in Niv02.iteritems():
			# 
			sumaX = 0
			sumaY = 0
			# Luego se recorre por cada segundo nivel el listado
			for parCoordenado in valores:
				sumaX = parCoordenado[0] + sumaX
				sumaY = parCoordenado[1] + sumaY
				
			# Si esl divisor es distinto de cero, se calcula la coordenada
			if not len(valores)==0:
				centroX = float(sumaX)/len(valores)
				centroY = float(sumaY)/len(valores)
				longitud = transformador(centroX,centroY,inverse='true')[0]
				latitud = transformador(centroX,centroY,inverse='true')[1]
				diccionarioCentroides[Niv01][llave] = [ ( longitud , latitud ) ]


	return diccionarioCentroides




