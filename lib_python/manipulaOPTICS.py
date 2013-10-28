# Libreria de systema
import sys
# Libreria para la manipulacion de datos
import pandas
# Libreria para la manipulacion de numeros mas rapido
import numpy
# Libreria para exportar a KML
import simplekml
# Libreria para el tratamiento de fechas y horas
from datetime import date,timedelta
#Importa la libreria para el tratamiento de Decimal('3.66')
from decimal import *
# Puesto que calcula los centroides
# Importa la libreria de pyproj
from pyproj import Proj, Geod
# Se importa la libreria de OPTICS para aplicar el algoritmo,
# y la de Malla para el achuramiento de zonas 
import OPTICS, Malla
# Se importa la libreria matematica
import math
# Tratamiento de conjuntos
from sets import Set


############################################################################################################################################
#FUNCION PARA DEBUGEAR
def set_trace():
	from IPython.core.debugger import Pdb
	Pdb(color_scheme='Linux').set_trace(sys._getframe().f_back)
############################################################################################################################################
#FUNCION QUE GENERA UN LISTADO SIN REPETICIONES
def unicos(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]
#####################################################################################################################################################
# Clase OPTICS
class ClaseOptics:
	"""Los atributos mas importantes de esta clase son:
			self.diccionarioOPTICS
			self.centroidesOPTICS
			self.antenasOPTICS
			self.numCoordOPTICS (Diccionario)
			self.MinPts (Diccionario)
			self.totPts_totCord (Diccionario)
			self.traslapeOPTICS (Diccionario)
			self.DataFrame_Optics"""

	# La funcion inicializadora
	def __init__(self, listadoTuplas = [ (0,'', date(2012,11,1) , timedelta(0,0) , -33.4560600000 ,  -33.4560600000 ,0,0,0 )  , (0,'',date(2012,11,1), timedelta(0,0),  -33.4560600000,  -33.4560600000 ,0,0,0 ) ] , Distancia = 3000 ,  MinPts = -1 , tipo = 'general' ):
		"""listadoTuplas es la clasica tupla de : (numero,BTS_ID,fecha,hora,latitud,londitud, azimut,ancho,distancia)"""

		# Aqui se crea el diccionario
		self.numeroUsuario = listadoTuplas[0][0]
		diccionarioOPTICS = {}
		diccionarioOPTICS_02 = {}
		self.centroidesOPTICS = {}
		self.centroCorr = {}
		self.antenasOPTICS = {}
		self.MinPts = {}
		self.total_Pts = {}
		self.total_Coord_distintas={}
		self.numCoordOPTICS = {}
		self.traslapeOPTICS = {}
		self.conjunto_Mayores_Intensidades = {}

		# Declaracion de la instancia para graficar
		self.Documento_Principal_KML = simplekml.Kml(name =str(listadoTuplas[0][0]))

		# Los resultados
		columns = ['numero','nombre','fecha' ,'hora' ,'latitud','longitud','azimut','ancho','alcance', 'reachability_distance' ,'core_distance','voronoi']
		self.resultado_Optics = pandas.DataFrame(columns = columns )


		# Si resulta ser el analisis ESPECIFICO
		if tipo=='especifico' or tipo=='Especifico':

			##### Llenado de los diccionarios
			for fila in listadoTuplas:
				fecha = fila[2].isoweekday()
				hora =int(fila[3].seconds/3600)

				diccionarioOPTICS.setdefault(str(fecha),{})
				diccionarioOPTICS[str(fecha)].setdefault(str(hora) ,[])
				diccionarioOPTICS[str(fecha)][str(hora)].append(list(fila))

		# Si lo que se busca es un diccionario invertido
		if tipo=='inverso' or tipo=='Inverso' or tipo=='invertido' or tipo=='Invertido':

			##### Llenado de los diccionarios
			for fila in listadoTuplas:
				fecha = fila[2].isoweekday()
				hora =int(fila[3].seconds/3600)

				diccionarioOPTICS.setdefault(str(hora),{})
				diccionarioOPTICS[str(hora)].setdefault(str(fecha) ,[])
				diccionarioOPTICS[str(hora)][str(fecha)].append(list(fila))

		# Si el analisis es GENERAL
		elif tipo=='general' or tipo=='General':

				diccionarioOPTICS.setdefault('1',{})
				diccionarioOPTICS['1'].setdefault('1',list(listadoTuplas))


		##### Se calcula el OPTICS para los intervalos especificados

		for Niv01 , ValNiv01 in diccionarioOPTICS.iteritems():
			# El segundo nivel de recorrido son los bloques horarios.
			for Niv02, ValNiv02 in ValNiv01.iteritems():

				#### AQUI COMIENZA LA APLICACION ALGORITMO OPTICS
				##################################################
				####################
				# Inicio calculo MinPts: el cual es un parametro del algoritmo OPTICS.
				listadoOPTICS = diccionarioOPTICS[Niv01][Niv02]
				# Calculo de numero minimo de puntos
				listado = []
				for elemento in listadoOPTICS:
					listado.append(str(elemento[4])+str(elemento[5]))
				totalCoordenadas = len(unicos(listado))

				# Si no se ha indicado el numero de puntos para formar el cluster este se arma de manera dinamica.
				try:
					if (MinPts == -1) : MinPts = len(listadoOPTICS)/totalCoordenadas
				# Si resulta que se esta dividiendo por zero, el parametro se deja en 0.
				except ZeroDivisionError:
					MinPts=0

				# Fin calculo MinPts
				####################

				# Atributo con uno de los parametros para OPTICS.Crea las llaves en la medida en que no existan.
				self.MinPts.setdefault(Niv01, {})
				self.MinPts[Niv01].setdefault(Niv02, MinPts )
				# Atributo con total de llamadas
				self.total_Pts.setdefault(Niv01, {})
				self.total_Pts[Niv01].setdefault(Niv02, len(listadoOPTICS) )
				# Atributo con total coordenadas diferentes
				self.total_Coord_distintas.setdefault(Niv01, {})
				self.total_Coord_distintas[Niv01].setdefault(Niv02,totalCoordenadas )

				# Numero del usuario
				numeroUsuario = str(listadoTuplas[0][0])
				#Listado del conjunto de objetos
				conjuntoObjetos = OPTICS.SetOfObjects( listadoOPTICS )
				# Entrega de parametros para el calculo de clusters
				resultadoAlg = OPTICS.FOptics(conjuntoObjetos , Distancia ,  MinPts  )

				# Resultado del algoritmo 
				diccionarioOPTICS[Niv01][Niv02] = resultadoAlg
				self.resultado_Optics = self.resultado_Optics.append(pandas.DataFrame(resultadoAlg, columns=columns), ignore_index=True)

		# Ordenacion de los rsultados obtenidos en DataFrames
		self.Datos_Generales = pandas.Panel({'MinPts':pandas.DataFrame(self.MinPts),'total_Pts':pandas.DataFrame(self.total_Pts),'total_Coord_distintas':pandas.DataFrame(self.total_Coord_distintas)})

		##### Reordenacion del diccionario OPTICS y CALCULO DE LOS CENTROIDES
		# Se recorren los dias
		for Dia, Horas in diccionarioOPTICS.iteritems():
			# Luego se recorren los bloques horarios
			for bloques, listado in Horas.iteritems():
				num_cluster=0
				# Si el listado no es vacio y tiene mas de dos elementos
				if (not listado == []) and len(listado) > 1:
					i=0
					# i es un condator de la lista "listado"
					while i <= len(listado)-1:

						# Se crea una lista vacia donde se van metiendo los clusters
						bolsa = []
						bolsaAntenas = []

						# Se agrega el primer elemento de la lista a la bolsa
						bolsa.append(listado[i])
						bolsaAntenas.append( ( listado[i][1] , listado[i][4] , listado[i][5] ) )

						# Se pasa al siguiente elemento
						i+=1

						# Si no se esta fuera de los elementos de la lista y la distancia del siguiente elemento es menor a la Reachability Distance
						while ( i<=len(listado)-1 ) and ( listado[i][9] <= Distancia ):

							# Se agrega el elemento a la bolsa
							bolsa.append(listado[i])
							bolsaAntenas.append( ( listado[i][1] , listado[i][4] , listado[i][5] ) )

							# Y se para al siguiente elemento
							i+=1

						# Si la bolsa termino con mas de 1 elemento
						if len(bolsa) > 1 :
							num_cluster +=1
							nombreCluster = str(num_cluster)+' '+ str( round(float(len(bolsa))/len(listado), 5 ))
							#nombreCluster = 'cluster_'+str(i)  
							# Se crea el cluster
							diccionarioOPTICS_02.setdefault(Dia ,{})
							diccionarioOPTICS_02[Dia].setdefault( bloques ,{})
							diccionarioOPTICS_02[Dia][bloques].setdefault(nombreCluster,bolsa)
							diccionarioOPTICS_02[Dia][bloques][nombreCluster] = bolsa

							##### CREACION DEL DICCIONARIO CON EL LISTADO DE LAS ANTENAS
							self.antenasOPTICS.setdefault(Dia,{})
							self.antenasOPTICS[Dia].setdefault(bloques,{})
							self.antenasOPTICS[Dia][bloques].setdefault(nombreCluster,bolsaAntenas)


							##### LLENADO DEL DICCIONARIO self.numCoordOPTICS.
							# Creacion de las llaves y llenado
							numero = len(unicos(bolsaAntenas))
							self.numCoordOPTICS.setdefault(Dia,{})
							self.numCoordOPTICS[Dia].setdefault(bloques,{})
							self.numCoordOPTICS[Dia][bloques].setdefault(nombreCluster,numero)

							##### CREACION DEL DICCIONARIO DEL CENTRO DE MASAS
							centroMasa = centroide(bolsa)
							#  Si no existen las llaves se crean
							self.centroidesOPTICS.setdefault(Dia,{})
							self.centroidesOPTICS[Dia].setdefault(bloques,{})
							self.centroidesOPTICS[Dia][bloques].setdefault(nombreCluster,( 0,'BTS', date(2013, 1, 1), timedelta(0, 0), centroMasa[0],centroMasa[1]))

						# Si la bolsa termino con solo 1 elemento
						else:

							# Se agrega a ruido, pero si ruido no existe, se crea
							diccionarioOPTICS_02.setdefault(Dia ,{})
							diccionarioOPTICS_02[Dia].setdefault( bloques ,{})
							diccionarioOPTICS_02[Dia][bloques].setdefault('ruido',[])
							diccionarioOPTICS_02[Dia][bloques]['ruido'].append(listado[i-1])

				# Se el listado no es vacio, pero tiene 1 solo elemento
				elif (not listado == []) and (len(listado) == 1):
					# Es ruido
					diccionarioOPTICS_02.setdefault(Dia ,{})
					diccionarioOPTICS_02[Dia].setdefault( bloques ,{})
					diccionarioOPTICS_02[Dia][bloques].setdefault('ruido',listado)

				if diccionarioOPTICS_02[Dia][bloques]=={}: del diccionarioOPTICS_02[Dia][bloques]


		self.diccionarioOPTICS = diccionarioOPTICS_02
		del diccionarioOPTICS,diccionarioOPTICS_02


	########## METODO PARA GUARDAR LOS RESULTADOS EN UN KML
	def guardar_kml( self, niveles = 3, diccionario = {'a':{'c':[]},'b':{'d':[]}} , nombre_carpeta='por defecto', centroide = False ):
		"""Este metodo toma el diccionario entregado agrega su contenido a una instancia que representa un archivo KML, el nombre de la instancia es 
				self.Documento_Principal_KML

			niveles: 3 niveles implica un diccionario de tres llaves que termina en un listado de listas o tuplas
					2 niveles implica un diccionario de dos llaves que termina en un listado de listas o tuplas [[],[],[]]

			diccionario: el diccionario que se quiere usar, las tuplas pertenecientes al listado de tuplas deben tener el siguiente formato, [ ]

			nombre_carpeta: es el nombre que se le quiere dar a la carpeta

			centroide: es verdadero si se trata de un diccionario de centroides, puesto que las tuplas son mas cortas.
			"""

		# se crea una carpeta para el tipo de grafico que se quiere hacer
		Carpeta_Tipo_Resultado = self.Documento_Principal_KML.newfolder(name = nombre_carpeta)		
		colores = ['fffff8f0','ffd7ebfa','ffffff00','ffd4ff7f','fffffff0','ffdcf5f5','ffc4e4ff','ff000000','ffcdebff','ffff0000','ffe22b8a','ff2a2aa5','ff87b8de','ffa09e5f']
		color_pocision = 0

		# Si el diccionario tiene 3 niveles
		if niveles ==3:	
				# Recorrido por los diferentes niveles del diccionario:
				for Dia, Dic_Hora in sorted(diccionario.iteritems()):
					# Se crea la instancia dentro del documento principal, segun el dia.
					Carpeta_Dia_KML = Carpeta_Tipo_Resultado.newfolder(name = Dia) 

					# Sigue recorriendo por Hora
					for Hora , Dic_Cluster in sorted(Dic_Hora.iteritems()):
						# Se crea una instancia dentro de la carpeta del dia con una carpeta de la hora
						Carpeta_Hora_KML = Carpeta_Dia_KML.newfolder( name = Hora )
						# Recorre por Clusters ahora
						for Cluster, listado in sorted(Dic_Cluster.iteritems()):
							# Aqui se filtra, y no se escribe lo correspondiente a ruido.
							if not Cluster == 'ruido':
								# Se crea la instancia dentro de la carpeta de la hora, con los clusters
								Carpeta_Cluster_KML = Carpeta_Hora_KML.newfolder(name = Cluster )

								# Se arregla la lista
								if centroide:
									listado_arreglado=[listado]
								else:
									listado_arreglado=listado

								# Recorrido del listado de puntos
								for Punto in listado_arreglado:
	
									try:
										# Se acomodan los datos
										latitud=Punto[4]
										longitud=Punto[5]
										nombre = '%s %s'%(Punto[2],Punto[3])
										# Se agrega el punto
										punto_para_modificar = Carpeta_Cluster_KML.newpoint(coords = [(longitud,latitud)], name=nombre )
										# Las siguientes lineas modifican el estilo del icono.
										punto_para_modificar.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
										punto_para_modificar.style.iconstyle.color = colores[color_pocision]
										color_pocision = (color_pocision+1)%14

									# Si se quiere rastrear un error
									except TypeError:
										pass


								#raise NameError('Desarrollo')

								

	########## METODO PARA GUARDAR LOS RESULTADOS EN UN TXT
	def guardar_csv( self, niveles = 3, diccionario = {'a':{'c':[]},'b':{'d':[]}} , ubicacion='/media/discoExternoRAID/raul/Python/Resultados/resultado_OPTICS.csv' , modo = 'w', centroide = False):
		"""Este metodo toma el diccionario entregado y lo guarda en un csv.
		
			niveles: 3 niveles implica un diccionario de tres llaves que termina en un listado de listas o tuplas,
					2 niveles implica un diccionario de dos llaves que termina en un listado de listas o tuplas,

					las tuplas si son normales son de la forma  
					[[numero1,nombre1,fecha,hora,latitud,longitud,azimut,ancho,alcance,reachability_distance,core_distance,voronoi], ... ]

					si son de un centroides son de la forma
					[[numero1,nombre1,fecha,hora,latitud,longitud], ... ]


			diccionario: el diccionario que se quiere usar, las tuplas pertenecientes al listado de tuplas deben tener el siguiente formato, [ ]
		
			ubicacion: el camino con el nombre del archivo incluido donde se quiere guardar el archivo.
		
			modo: los mismo de python concermientes a la escritura.
		
			centroide: bolean, si es verdadero se corta la tupla, ya que viene con menos datos.	
			"""

		# definicion de las columnas
		columns = ['numero','nombre','fecha' ,'hora' ,'latitud','longitud','azimut','ancho','alcance', 'reachability_distance' ,'core_distance','voronoi','']

		guardar_csv = pandas.DataFrame( columns=columns)

		# Si el diccionario tiene 3 niveles 
		if niveles ==3:	
				# Recorrido por los diferentes niveles del diccionario:
				for Dia, Dic_Hora in diccionario.iteritems():
					for Hora , Dic_Cluster in Dic_Hora.iteritems():
						for Cluster, listado in Dic_Cluster.iteritems():
							# Aqui se filtra, y no se escribe lo correspondiente a ruido.
							if not Cluster == 'ruido':

								num_cluster = int(Cluster.split()[0])
								porc_cluster = float(Cluster.split()[1])

								# Se ajusta el tamano de la tupla
								if centroide:
									restar_columnas = -len(columns)+len(listado)
									numero_filas=len([listado])
									columns_01 = pandas.DataFrame([listado],columns=columns[:restar_columnas])
									# La siguiente linea modifica el numero, de cero al verdadero numero del usuario
									columns_01['numero']=self.numeroUsuario
									# Ademas se incluye el numero de la region de voronoi
									distancia_Min = 100000000000000
									for registro in self.diccionarioOPTICS[Dia][Hora][Cluster]:
										# Distancia mas cercana
										lat = registro[4]
										lon = registro[5]
										distancia = abs(float(lat)-columns_01['latitud'])+abs(float(lon)-columns_01['longitud'])
										# Se chequea si es realmente menor
										if distancia<=distancia_Min :
											distancia_Min = distancia
											# Se asigna la region de voronoir
											columns_01['nombre'] = registro[-1]


								else:
									numero_filas=len(listado)
									restar_columnas = -len(columns)+len(listado[0])
									columns_01 = pandas.DataFrame(listado,columns=columns[:restar_columnas])

								# Se rearma el DataFrame
								columns_02 = pandas.DataFrame([int(Dia)]*numero_filas,columns=['Dia'] )
								columns_03 = pandas.DataFrame([int(Hora)]*numero_filas,columns=['Hora'] )
								columns_04 = pandas.DataFrame([num_cluster]*numero_filas,columns=['Num_Cluster'] )
								columns_05 = pandas.DataFrame([porc_cluster]*numero_filas,columns=['Porcentaje_Cluster'] )

								# Dataframe Final
								ordenado=pandas.concat( [columns_01,columns_02,columns_03,columns_04, columns_05 ], axis = 1, ignore_index = True )
								ordenado.columns=columns[:restar_columnas]+['Dia']+['Hora']+['Num_Cluster']+['Porcentaje_Cluster']
								guardar_csv = guardar_csv.append( ordenado , ignore_index=True)

							# Aqui se incluiria un un if que agregaria ruido a otro TXT

		# se chequea que el DataFrame no este vacio
		try:
			if centroide:
				# Salvado en el archivo
				guardar_csv[['numero','nombre','latitud','longitud','Dia','Hora','Num_Cluster','Porcentaje_Cluster']].to_csv( ubicacion , mode = modo, index=False )
			else:
				# Salvado en el archivo
				guardar_csv[['numero','nombre','latitud','longitud','Dia','Hora','Num_Cluster','Porcentaje_Cluster','voronoi']].to_csv( ubicacion , mode = modo, index=False )


		except KeyError:
			print "Todo era ruido"
		#self.resultado_OPTICS.to_csv( )


	######### AQUI VA EL METODO QUE CALCULA EL TRASLAPE DE LOS CLUSTERS
	def traslaparOPTICS(self):

		# Se recorre el diccionario de centroides, 
		# ya que es un valor medio y buen punto de referencia
		for Dia, Dic_Bloq_Dia in self.centroidesOPTICS.iteritems():
			for bloque, Dic_Bloq_Hor in Dic_Bloq_Dia.iteritems():
				# En este "for" se revisan los puntos de los clusters
				for cluster, listado in Dic_Bloq_Hor.iteritems():
					
					# Se crea una MALLA para este cluster, donde iran las intersecciones
					# El unico parametro es el LADO del cuadrado en METROS
					malla = Malla.malla(ladoCuadradoMetros=50)

					# La idea es que no revise el contenido del ruido
					try:
						for registro in self.diccionarioOPTICS[Dia][bloque][cluster]:
							#El punto en observacion se agrega a la malla
							malla.achurar( identificador=registro[1], latitud=registro[4] ,longitud=registro[5] , azimut_grados=registro[6], ancho_grados=registro[7], alcance=registro[8] )
							#Se actualiza la zona de traslape con el punto en Observacion de coordenadas (x,y)
							#self.traslapeOPTICS[Dia][bloque][cluster] = malla.absolutos

						# Una vez generada la malla para un cluster el resultado de esta se pasa a un atributo
						# Aqui se guarda la malla en un diccionario
						self.traslapeOPTICS.setdefault(Dia,{})
						self.traslapeOPTICS[Dia].setdefault(bloque,{})
						self.traslapeOPTICS[Dia][bloque].setdefault(cluster,{})
						self.traslapeOPTICS[Dia][bloque][cluster] = malla.diccioMalla

						# Aqui se guardan el conjunto de los puntos mas intensos en un diccionario
						self.conjunto_Mayores_Intensidades.setdefault(Dia,{})
						self.conjunto_Mayores_Intensidades[Dia].setdefault(bloque,{})
						self.conjunto_Mayores_Intensidades[Dia][bloque].setdefault(cluster,malla.conjunto_Mayores_Intensidades)
					except KeyError:
						pass

			

					


	###### CON ESTA FUNCION SE CORRIGEN LOS CENTROIDES
	def centroidesCorregidos(self):

		# Para el calculo de distancias entre coordenadas angulares
		g = Geod(ellps='bessel')

		# Se recorre el diccionario de mayores intensidades, 
		for Dia, Dic_Bloq_Dia in self.conjunto_Mayores_Intensidades.iteritems():
			for Bloque, Dic_Bloq_Hor in Dic_Bloq_Dia.iteritems():
				for cluster, conjunto in Dic_Bloq_Hor.iteritems():
				
					distMinima = 10000
					for coordenadas in conjunto:

						# Se calcula la distancia entre el centroide y los puntos de mayor intensidad
						latitud=coordenadas[0]
						longitud=coordenadas[1]
						latitudCentroide = self.centroidesOPTICS[Dia][Bloque][cluster][4]
						longitudCentroide = self.centroidesOPTICS[Dia][Bloque][cluster][5]
						az12,az21, distancia = g.inv( longitud , latitud , longitudCentroide , latitudCentroide )

						# Si la distancia calculada es menor a la distancia minima
						if distancia < distMinima:
							# Se actualiza el valo
							distMinima = distancia
							# Se asigna un nuevo centroide
							centroCorregido = self.centroidesOPTICS[Dia][Bloque][cluster]
							centroCorregido = list(centroCorregido)
							centroCorregido[4] = latitud
							centroCorregido[5] = longitud
							centroCorregido = tuple(centroCorregido)
							self.centroCorr.setdefault(Dia,{})
							self.centroCorr[Dia].setdefault(Bloque,{})
							# y se guarda en el diccionario
							self.centroCorr[Dia][Bloque].setdefault(cluster,centroCorregido)
							self.centroCorr[Dia][Bloque][cluster]=centroCorregido




	###### AQUI SE ESCRIBE EL METODO QUE CREA EL ARCHIVO KML CON EL AREA DE COBERTURA OPTICS
	def ArchivoMalla(self, ubicacion = '/media/discoExternoRAID/raul/Python/Resultados/' , nombreArchivo = 'archivoSinNombre', nombreGoogleEarth = 'KML sin nombre'):
		"""Esta funcion crea el archivo KML con el detalle del resultado de la malla"""
		
		# Voy a usar el atributo self.traslapeOPTICS
		# Se importa la libreria
		import EnsambleXML

		# el transformador. de utm a lat/long, recordar agregar "inverse = 'true' "
		transformador = Proj( proj='utm', zone='19', ellps='WGS84' )	

		# Creacion del archivo con el detalle
		# Creacion de las etiquetas de documento
		docuMento = EnsambleXML.EnsXML( 'Document' , nombreGoogleEarth )

		# Este es el contador que va haciendo cambiar el color de los pinches
		i = 0

		# Se parte recorriendo los dias del diccionario
		for Dias , Diccio_Bloques in iter( sorted(self.traslapeOPTICS.iteritems() ) ):
			# Se crea una carpeta correspondiente al dia, en la que se van agregando al final los bloques horarios
			CarpetaDia = EnsambleXML.EnsXML( 'Folder' , Dias ) 

			# Se recorren los bloques
			for Bloque , Diccio_Clusters in iter( sorted( Diccio_Bloques.iteritems() ) ):

				# Se crea un carpeta por los bloques horarios
				CarpetaBloques = EnsambleXML.EnsXML( 'Folder' , Bloque )

				# Se recorren los cluster que son parte del bloque horario
				for clusters, Diccio_Coord_x in iter( sorted( Diccio_Clusters.iteritems() ) ):
					
					# Se crea una carpeta para cada cluster
					CarpetaCluster = EnsambleXML.EnsXML( 'Folder' , clusters )


					# Recorrido de las coordenadas
					for Coord_x, Diccio_Coord_y in iter( sorted( Diccio_Coord_x.iteritems() ) ):
					
						for Coord_y, frecuencia in iter( sorted( Diccio_Coord_y.iteritems() ) ):

							# El cambio de color es por cluster
							color = frecuencia%9

							# Transforma de vuelta a coordenadas angulares los datos
							print "%s %s" % (Decimal(Coord_x),Decimal(Coord_y))
							longitud = transformador(Decimal(Coord_x),Decimal(Coord_y),inverse='true')[0]
							latitud = transformador(Decimal(Coord_x),Decimal(Coord_y),inverse='true')[1]

							coord = [(longitud,latitud)]
							Placemark = EnsambleXML.EnsXML( 'Placemark' , str(frecuencia) , coord , color )

							# Se agrega tal punto a la carpeta de clusters
							CarpetaCluster.agregar(Placemark.cuerpo)

					
					# La carpeta cluster que se reviso recien se agrega al bloque horario
					CarpetaBloques.agregar(CarpetaCluster.cuerpo)

				# El bloque horario revisado recien se agrega a la carpeta del dia
				CarpetaDia.agregar(CarpetaBloques.cuerpo)

			# El dia revisado se agrega al documento
			docuMento.agregar(CarpetaDia.cuerpo)


		# El docuMento crea un consolidado de si mismo que se encuentra en el atributo "docuMento.consolidado"
		docuMento.consolidar( docuMento.cuerpo )
		ElScript = docuMento.consolidado

		# Se define el destino del archivo
		ubicacion = ubicacion+nombreArchivo

		# Se abre el archivo a escribit
		archivoXML = open( ubicacion, 'w')

		# Fin del Document
		archivoXML.write( ElScript )

		archivoXML.close()


	###### AQUI SE ESCRIBE EL METODO QUE CREA EL ARCHIVO KML CON EL DETALLE DEL OPTICS
	def ArchivoDetalle(self , ubicacion = '/media/discoExternoRAID/raul/Python/Resultados/' , nombreArchivo = 'archivoSinNombre', nombreGoogleEarth = 'KML sin nombre'):
		"""Esta funcion crea el archivo KML con el detalle del resultado OPTICS"""

		# Voy a usar el atributo self.diccionarioOPTICS que termina con un LISTADO DE TUPLAS. La diferencia con "self.ArchivoCentroides" es que este ultimo termina con solo una TUPLA.
		# Se importa la libreria
		import EnsambleXML

		# Creacion del archivo con el detalle
		# Creacion de las etiquetas de documento
		docuMento = EnsambleXML.EnsXML( 'Document' , nombreGoogleEarth )

		# Este es el contador que va haciendo cambiar el color de los pinches
		i = 0

		# Se parte recorriendo los dias del diccionario
		for Dias , valoresDias in iter( sorted(self.diccionarioOPTICS.iteritems() ) ):

			# Se crea una carpeta correspondiente al dia, en la que se van agregando al final los bloques horarios
			CarpetaDia = EnsambleXML.EnsXML( 'Folder' , Dias ) 

			# Se recorren los bloques
			for bloques , valoresBloques in iter( sorted( valoresDias.iteritems() ) ):

				# Se crea un carpeta por los bloques horarios
				CarpetaBloques = EnsambleXML.EnsXML( 'Folder' , bloques )

				# Se recorren los cluster que son parte del bloque horario
				for clusters, valoresClusters in iter( sorted( valoresBloques.iteritems() ) ):


					# Se crea una carpeta para cada cluster
					CarpetaCluster = EnsambleXML.EnsXML( 'Folder' , clusters )

					# El cambio de color es por cluster
					color = i%9

					# Si el cluster es el ruido, se recorre entero
					if clusters == 'ruido':

						# Aqui se recorre cada tupla del cluster ruido
						for tupla in valoresClusters:
							longitud = tupla[5]
							latitud = tupla[4]
							coord = [(longitud,latitud)]
							Placemark =  EnsambleXML.EnsXML( 'Placemark' , str(tupla[1]) , coord , color )

							CarpetaCluster.agregar(Placemark.cuerpo)

					# Si el cluster NO es de ruido
					else:

						# Se recorre todo menos el ultimo elemento que es el centroide
						for tupla in valoresClusters:
							longitud = tupla[5]
							latitud = tupla[4]
							coord = [(longitud,latitud)]
							Placemark = EnsambleXML.EnsXML( 'Placemark' , str(tupla[3]) , coord , color )

							# Se agrega tal punto a la carpeta de clusters
							CarpetaCluster.agregar(Placemark.cuerpo)


					# Se cambia el color
					i+=1
					
					# La carpeta cluster que se reviso recien se agrega al bloque horario
					CarpetaBloques.agregar(CarpetaCluster.cuerpo)

				# El bloque horario revisado recien se agrega a la carpeta del dia
				CarpetaDia.agregar(CarpetaBloques.cuerpo)

			# El dia revisado se agrega al documento
			docuMento.agregar(CarpetaDia.cuerpo)


		# El docuMento crea un consolidado de si mismo que se encuentra en el atributo "docuMento.consolidado"
		docuMento.consolidar( docuMento.cuerpo )
		ElScript = docuMento.consolidado

		# Se define el destino del archivo
		ubicacion = ubicacion+nombreArchivo

		# Se abre el archivo a escribit
		archivoXML = open( ubicacion, 'w')

		# Fin del Document
		archivoXML.write( ElScript )

		archivoXML.close()



	###### AQUI SE ESCRIBE EL METODO QUE CREA EL ARCHIVO KML CON LOS CENTROIDES DEL OPTICS
	def ArchivoCentroides(self , ubicacion = '/media/discoExternoRAID/raul/Python/Resultados' , nombreArchivo = 'archivoSinNombre', nombreGoogleEarth = 'KML sin nombre', correccion = False ):
		"""Esta funcion crea el archivo KML con los centroides del resultado OPTICS"""

		# Voy a usar el atributo self.ArchivoCentroides que termina con UNA TUPLA. La diferencia con "self.diccionarioOPTICS" es que este ultimo termina con un LISTADO de TUPLAS
		# Se importa la libreria
		import EnsambleXML

		# Creacion de las etiquetas de documento
		docuMento = EnsambleXML.EnsXML( 'Document' , nombreGoogleEarth )

		if correccion == True:
			Diccionario = self.centroCorr
		else:
			Diccionario = self.centroidesOPTICS

		# Este es el contador que va haciendo cambiar el color de los pinches
		i = 0

		# Se parte recorriendo los dias del diccionario
		for Dias , valoresDias in iter( sorted( Diccionario.iteritems() ) ):

			# Se crea una carpeta correspondiente al dia, en la que se van agregando al final los bloques horarios
			CarpetaDia = EnsambleXML.EnsXML( 'Folder' , Dias ) 

			# Se recorren los bloques
			for bloques , valoresBloques in iter( sorted( valoresDias.iteritems() ) ):

				# Se crea un carpeta por los bloques horarios
				CarpetaBloques = EnsambleXML.EnsXML( 'Folder' , bloques )

				# Se recorren los cluster que son parte del bloque horario
				for clusters, valoresClusters in iter( sorted( valoresBloques.iteritems() ) ):

					# valoresClusters es LA TUPLA
					# Se crea una carpeta para cada cluster
					#CarpetaCluster = EnsambleXML.EnsXML( 'Folder' , clusters )

					# El cambio de color es por cluster
					color = i%9

					# Se cambia el color
					i+=1

					# Se agrega el centroide, que es el ultimo elemento de la lista
					longitud = valoresClusters[5]
					latitud = valoresClusters[4]
					coord = [(longitud,latitud)]
					Placemark = EnsambleXML.EnsXML( 'Placemark' , clusters , coord , color )
					CarpetaBloques.agregar(Placemark.cuerpo)
					#CarpetaCluster.agregar(Placemark.cuerpo)

					# Se cambia el color
					i+=1
					
					# La carpeta cluster que se reviso recien se agrega al bloque horario
					#CarpetaBloques.agregar(CarpetaCluster.cuerpo)

				# El bloque horario revisado recien se agrega a la carpeta del dia
				CarpetaDia.agregar(CarpetaBloques.cuerpo)

			# El dia revisado se agrega al documento
			docuMento.agregar(CarpetaDia.cuerpo)

		# El docuMento crea un consolidado de si mismo que se encuentra en el atributo "docuMento.consolidado"
		docuMento.consolidar( docuMento.cuerpo )
		ElScript = docuMento.consolidado

		ubicacion = ubicacion + nombreArchivo
		# Se abre el archivo a escribit
		archivoXML = open( ubicacion, 'w')

		# Fin del Document
		archivoXML.write( ElScript )

		archivoXML.close()



#####################################################################################################################################################
# Funcion que calcula CENTROIDES
def centroide( listado = [  ( 0, '', date(2012, 11, 9), timedelta(0, 72757), Decimal('-33.4'), Decimal('-70.5'), 1000000, 571)  ,  (date(2012, 11, 9), timedelta(0, 73040), Decimal('-33'), Decimal('-70'), 571, 571)  ,  (date(2012, 11, 9), timedelta(0, 73320), Decimal('-33'), Decimal('-70'), 571, 571)  ,  (date(2012, 11, 9), timedelta(0, 73530), Decimal('-33'), Decimal('-70'), 571, 571)  ] ):
	"""Funcion interna de la funcion OPTICS para el calculo de centro de masa"""


	# el transformador. de utm a lat/long, recordar agregar "inverse = 'true' "
	transformador = Proj( proj='utm', zone='19', ellps='WGS84' )	

	# Llenado del diccionario.
	sumaX = 0
	sumaY = 0

	# Recorre las tuplas del listado
	for tupla in listado:
		try:
			latitud = tupla[4]
			longitud = tupla[5]
		except TypeError:
			pass
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
