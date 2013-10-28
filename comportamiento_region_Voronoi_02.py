#!/usr/bin/python2.7

"""
####################################################################################################
MODIFICACIONES
####################################################################################################


mar ago  6 19:21:56 CLT 2013
-Ejecucion en paralelo
-Guarda histogramas

Wed 24 Jul 2013 07:27:35 PM CLT 
Se modifica e incluye el paquete SciPy
Se en vez de usar armar una query, usa una Vista.

dom jul  7 12:40:19 CLT 2013
Se incorpora Numpy

"""



####################################################################################################
# SE IMPORTAN LAS LIBRERIAS CORRESPONDIENTES
####################################################################################################
# Trabajar con los algoritmos de clusterizacion
import scipy

# Trabajar MySQL/Infobright
import MySQLdb

# Se importa la libreria que permite tratamiento de fechas
from datetime import date,timedelta,datetime

# Se importa numpy, para el tratamiento efectivo de datos
from numpy import *
import numpy

# Se importa SciPy
from scipy.optimize import minimize

# Se importa Matplotlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot
matplotlib.pyplot.ioff()


# Se importa la libreria de procesamiento multiple
import multiprocessing
from multiprocessing import Pool

# Libreria para utilitarios varios
import sys

# Libreria Pandas
import pandas

# Se importa la libreria que permite tratamiento de fechas
from datetime import date,timedelta,datetime

# libreria matematica
import math

import sys
############################################################################################################################################
#FUNCION PARA DEBUGEAR
def set_trace():
	from IPython.core.debugger import Pdb
	Pdb(color_scheme='Linux').set_trace(sys._getframe().f_back)
############################################################################################################################################
####################################################################################################
# FUNCIONES QUE DEVUELVEN UN VECTOR DE RESULTADOS
####################################################################################################
def vector_frecuencias_relativas(numero_region_voronoi):
	"""A esta funcion se le entrega la region de voronoi que se quiere estudiar.
	Lo que entrega de vuelta es un panda.DataFrame, con 1 index (el numero de la region de voronoi) y 168 columnas ordenadas (una por cada bloque horario)"""

	db = MySQLdb.connect( host = "127.0.0.1", user = "root", passwd = "eadh5148", db = "mobility", port = 5029 )
	#db = MySQLdb.connect( host = "146.83.5.100", user = "root", passwd = "eadh5148", db = "mobility", port = 5029 )
	BaseDatos = db.cursor()

	# Se realiza la consulta correspondiente
	consulta_frecuencia = 'SELECT Num_Dia, Num_Hora, COUNT(*) FROM CDR_One_EFECTIVO WHERE Num_Voronoi=%s GROUP BY Num_Dia,Num_Hora ORDER BY Num_Dia,Num_Hora ;'%(numero_region_voronoi)

	# Se realiza la consulta
	BaseDatos.execute(consulta_frecuencia)
	# Se extrae la informacion entregada en una matriz
	consulta_frecuencia = numpy.array(BaseDatos.fetchall())

	# Cierro la base de datos
	BaseDatos.close()

	try:
	# Se crea un indice Heriarquico
		indices = pandas.MultiIndex.from_arrays( consulta_frecuencia[:,0:2].T, names=['Dias','Horas'])
		arreglo_indices = numpy.array([sorted(range(1,8)*24, key=int ),[j%24 for j in range(0,24*7)]] )
		indices_guias = pandas.MultiIndex.from_arrays( arreglo_indices , names=['Dia','Horas'] ) 

		# La suma total de todas las frecuencias
		suma_total =  consulta_frecuencia[:,2].sum()

		# Normalizacion del vector
		vector_normalizado = numpy.around(numpy.true_divide(consulta_frecuencia[:,2], suma_total ) , decimals=10)

		# Creacion del vector con las frecuencias
		frecuencias_relativas = pandas.DataFrame( vector_normalizado , index = indices, columns= [str(numero_region_voronoi)])
		data_frame_guia = pandas.DataFrame( numpy.zeros( (1,168) ).T , index = indices_guias,  columns= [str(numero_region_voronoi)])
		frecuencias_relativas = frecuencias_relativas + data_frame_guia

		# Relleno los valores vacios por zeros
		frecuencias_relativas = frecuencias_relativas.fillna(value=0)

		# Ordenacion de dicho vector y cambio de 1 COLUMNA a 1 FILA
		frecuencias_relativas = frecuencias_relativas.sortlevel(0).T

		# Se guarda el archivo correspondiente a esta frecuencia
		frecuencias_relativas.to_csv('/media/discoExternoRAID/raul/Python/Resultados/Regiones_Voronoi/Frecuencias_Relativas.csv', header = False, mode = 'a' )

	except IndexError:
		print "IndexError"

	print('.... Numero: %s	Fin: %s'%(numero_region_voronoi , datetime.now()))
	# Devuelve un diccionario
	#return frecuencias_relativas.to_dict()



def vector_frecuencias_absolutas(numero_region_voronoi):
	"""a esta funcion se le entrega la region de voronoi que se quiere estudiar. lo que entrega de vuelta es un diccionario con 168 llaves y cada una de estas con la frecuencia absoluta correspondiente"""

	db = MySQLdb.connect( host = "127.0.0.1", user = "root", passwd = "eadh5148", db = "mobility", port = 5029 )
	#db = MySQLdb.connect( host = "146.83.5.100", user = "root", passwd = "eadh5148", db = "mobility", port = 5029 )
	BaseDatos = db.cursor()

	# Se declara el diccionario donde ira a parar la info
	diccionario_frecuencias_absolutas = {}
	diccionario_frecuencias_absolutas['numero_region_voronoi'] = numero_region_voronoi

	# Se realiza la consulta correspondiente
	consulta_frecuencia = 'SELECT Num_Dia, Num_Hora, COUNT(*) FROM CDR_One_EFECTIVO WHERE Num_Voronoi=%s GROUP BY Num_Dia,Num_Hora ;'%(numero_region_voronoi)

	# Se realiza la consulta
	BaseDatos.execute(consulta_frecuencia)
	# Se extrae la informacion entregada en una matriz
	consulta_frecuencia = numpy.array(BaseDatos.fetchall())

	try:
		# Se ordena en un diccionario
		for tupla_frecuencia in consulta_frecuencia:
			# Se ordena la info
			llave = '%s %s'%(tupla_frecuencia[0],tupla_frecuencia[1])
			frecuencia = tupla_frecuencia[2]
			# Luego se incorpora en el diccionario
			diccionario_frecuencias_absolutas.setdefault(llave,frecuencia)

	except IndexError:
		pass

	return diccionario_frecuencias_absolutas



####################################################################################################
# FUNCION DE PROBABILIDADES
####################################################################################################
def proba_pertenencia(x):
	"""Probabilidaddes de pertenencia, dado parametros LAMBDAS"""
	return array([divide(exp(x[0]),exp(x[0])+exp(x[1])+1) ,divide(exp(x[1]),exp(x[0])+exp(x[1])+1),divide(1,exp(x[0])+exp(x[1])+1) ])




####################################################################################################
# ANALISIS POR REGION DE VORONOI
####################################################################################################

def verosimilitud(consulta_regiones_voronoi):
	"""jue ago  8 15:46:56 CLT 2013 Las regiones ingresadas son Huerfanos (Oficina), La Reina (Residencial) y Bellavista (Carrete).

		Lo que hace esta funcion es revisar las regiones de Voronoi del listado con que porcentaje se parecen mas a una de las regiones pre ingresadas.
		consulta_regiones_voronoi, corresponde a un listado con regiones de Voronoi
	 """

	# En este arreglo de numpy se guardaran las probabilidades
	lista_resultados= empty((0,4))


	# Este "i" es de testeo, es borrable
	i=0

	# Se realiza la consulta de la cantidad de llamadas, region por region.
	for region_voronoi in consulta_regiones_voronoi:

		# La region de voronoi
		numero_region = str(region_voronoi[0])

		# Se realiza la consulta, en base a los parametros: Region de Voronoi (Dia, Hora , Frecuencia).
		consulta_frecuencia = 'SELECT DIA,HORA , COUNT(*)  FROM (select DAYOFWEEK(Fecha) AS DIA,  HOUR(Hora) AS HORA , NUM_VORONOI FROM CDR_One_BRUTO_02, Antenas WHERE CDR_One_BRUTO_02.BTS_ID = Antenas.BTS_ID AND NUM_VORONOI = %s ) AS TABLA GROUP BY DIA,HORA ;'%(numero_region)
		#consulta_frecuencia = 'SELECT DIA,HORA , COUNT(*) , NUM_VORONOI FROM (select DAYOFWEEK(Fecha) AS DIA,  HOUR(Hora) AS HORA , NUM_VORONOI FROM CDR_One_BRUTO_02, Antenas WHERE CDR_One_BRUTO_02.BTS_ID = Antenas.BTS_ID AND NUM_VORONOI = +'str(numero_region)'+) AS TABLA GROUP BY DIA,HORA ;'

		# Se realiza la consulta
		BaseDatos.execute(consulta_frecuencia)
		# Se extrae la informacion entregada en una matriz
		consulta_frecuencia = BaseDatos.fetchall()

		# Interrumpo a proposito para ver que pasa 
		#raise NameError('probando')

		try:

			# Creacion del arreglo, de dimension: anos vistos, semanas vistas, 7 dias y 24 horas
			#probabilidad_region_voronoi = numpy.zeros( ( 7, 24 )  )
			frecuencias_region_voronoi = numpy.zeros((7,24))

			# Se recorre el listado guardando la info ordenada
			for fila in consulta_frecuencia:

				# se le da sentido a los valores
				dia = int(fila[0])-1
				hora = int(fila[1])
				frecuencia = int(fila[2])
					# Se guarda el valor en el arreglo
				frecuencias_region_voronoi[dia][hora] = frecuencia
				# Normalizacion del vector
			#probabilidad_region_voronoi = frecuencias_region_voronoi / frecuencias_region_voronoi.sum()
		except IndexError:
			# celda vacia
			print "celda vacia "+str(numero_region)
			# Creacion del arreglo, de dimension: anos vistos, semanas vistas, 7 dias y 24 horas
			probabilidad_region_voronoi = numpy.zeros((1, 1, 7, 24 )  )
			# verosimilitud
		def verosimilitud_negativa(lambdas):
			"""Verosimilitud"""
			f_huerfanos_2283=array([0.00009,0.00004,0.00006,0.00002,0.00002,0.00002,0.00001,0.00003,0.00007,0.00018,0.00042,0.00092,0.00126,0.00146,0.00156,0.00148,0.00159,0.00176,0.00167,0.00110,0.00070,0.00037,0.00022,0.00012,0.00007,0.00001,0.00000,0.00000,0.00000,0.00001,0.00007,0.00035,0.00240,0.01009,0.01578,0.01854,0.01899,0.01450,0.01344,0.01638,0.01701,0.01682,0.01424,0.00753,0.00316,0.00138,0.00059,0.00021,0.00009,0.00003,0.00002,0.00001,0.00001,0.00001,0.00006,0.00032,0.00217,0.00834,0.01313,0.01722,0.01886,0.01689,0.01416,0.01598,0.01644,0.01636,0.01426,0.00708,0.00281,0.00121,0.00065,0.00030,0.00016,0.00006,0.00002,0.00002,0.00004,0.00004,0.00014,0.00051,0.00239,0.00853,0.01320,0.01774,0.01966,0.01967,0.01729,0.01695,0.01851,0.01964,0.01567,0.00776,0.00333,0.00142,0.00063,0.00022,0.00009,0.00005,0.00002,0.00001,0.00001,0.00002,0.00007,0.00040,0.00224,0.00961,0.01456,0.01843,0.02389,0.02371,0.02024,0.02056,0.02087,0.02067,0.01752,0.00880,0.00394,0.00164,0.00073,0.00029,0.00012,0.00004,0.00002,0.00001,0.00002,0.00001,0.00006,0.00041,0.00249,0.01054,0.01691,0.02002,0.02363,0.02123,0.02201,0.02196,0.02271,0.02123,0.01183,0.00654,0.00359,0.00155,0.00076,0.00032,0.00019,0.00012,0.00006,0.00004,0.00004,0.00003,0.00005,0.00009,0.00032,0.00212,0.00362,0.00502,0.00639,0.00651,0.00444,0.00346,0.00315,0.00289,0.00300,0.00231,0.00159,0.00079,0.00046,0.00024])
			f_huerfanos_2283 = f_huerfanos_2283.reshape(7,24)

			f_reina_2855=array([0.0028657774,0.0018236765,0.001745519,0.000651313,0.0001823677,0.0001302626,0.000052105,2.60525218841184E-005,0.0006773656,0.0028136724,0.0045852439,0.0075552313,0.0101604835,0.0100562734,0.0076594414,0.0058878699,0.0060962901,0.008284702,0.0080762818,0.0102125886,0.0099781159,0.0074249687,0.0056012922,0.0024489371,0.0006773656,7.81575656523551E-005,0.000052105,0,0,0,0.0001823677,0.0029699875,0.0041162985,0.0087015423,0.0094570654,0.0080762818,0.0067215506,0.005392872,0.0068518133,0.0090402251,0.0096654856,0.0115412672,0.0124531055,0.0138599416,0.010733639,0.0092486453,0.0056794498,0.0026834098,0.0006252605,0.000052105,0.000052105,0,0,2.60525218841184E-005,0.0002865777,0.0028918299,0.004142351,0.006591288,0.0077115465,0.0074510213,0.0070341809,0.0073207586,0.0081023343,0.007789704,0.011280742,0.0110983743,0.0138599416,0.0134431013,0.0138859942,0.0089881201,0.0072165486,0.0026313047,0.0015110463,0.0002605252,0.0001823677,0.0002084202,0.000052105,2.60525218841184E-005,0.0001302626,0.0030741976,0.0040120884,0.0069299708,0.0075552313,0.0084670696,0.0085973322,0.0096133806,0.0096654856,0.0090923301,0.0126354731,0.0131825761,0.0125052105,0.0147457274,0.0129741559,0.0091183827,0.0059660275,0.0027615673,0.0008076282,7.81575656523551E-005,0.000052105,2.60525218841184E-005,0.0003386828,0.0002865777,0.0007555231,0.0026052522,0.0040120884,0.0068778658,0.0082586494,0.0081023343,0.0099260108,0.0084670696,0.0107596915,0.0087536474,0.0106033764,0.0137557316,0.0138599416,0.0164912464,0.0131044185,0.0123488954,0.0060962901,0.0032826178,0.0013807837,0.0003126303,0.000052105,2.60525218841184E-005,2.60525218841184E-005,0.000052105,0.0005731555,0.0039078783,0.0050802418,0.0063828679,0.0095091705,0.0075552313,0.0096394331,0.0092225927,0.0098218008,0.0113588995,0.0121404752,0.0158138808,0.0108378491,0.0106554815,0.0097957482,0.0082325969,0.0061744477,0.0032565652,0.0036734056,0.0010160484,0.0021623593,0.0002865777,0.0002605252,0.0001042101,7.81575656523551E-005,0.0009378908,0.0023186744,0.0042205085,0.0059139225,0.0091965402,0.0106033764,0.0098478533,0.0104731138,0.0084149646,0.0085973322,0.0083107545,0.0113067945,0.0105773239,0.0111244268,0.0096133806,0.0052626094,0.0053147145])
			f_reina_2855 = f_reina_2855.reshape(7,24)

			f_bellavista_2410=array([0.0189224934,0.0125568619,0.011554057,0.0032845495,0.0028921476,0.0004796024,0.0002034677,2.90668100629296E-005,0.0001162672,0.0003052015,0.0005668028,0.0013806735,0.0031828157,0.0030229482,0.0032118825,0.0038949525,0.0037786853,0.0038658857,0.0038658857,0.0051012252,0.0056534946,0.0043309547,0.003589751,0.0028049472,0.0008574709,0.0001162672,0.0001308006,0.000072667,1.45334050314648E-005,1.45334050314648E-005,5.81336201258593E-005,0.0003342683,0.0006976034,0.0012644062,0.0022672112,0.0024706789,0.002223611,0.0033281498,0.0041565538,0.0050140247,0.0054936271,0.0056244277,0.0073248361,0.0077317715,0.0090979115,0.0078189719,0.0083131077,0.0062057639,0.0021654773,0.0003342683,0.0006249364,8.72004301887889E-005,8.72004301887889E-005,1.45334050314648E-005,4.36002150943945E-005,0.0003052015,0.0007557371,0.0011045388,0.0023108114,0.0030374817,0.0030229482,0.0051157586,0.0063946982,0.0070777683,0.0077753717,0.0085311088,0.0081968404,0.0118301917,0.0132689988,0.0160012789,0.0155798102,0.0128329966,0.00810964,0.0040257532,0.0033281498,0.0023980118,0.0013080065,0.0003924019,1.45334050314648E-005,0.0004505356,0.0008865377,0.0015986746,0.0017004084,0.0026596131,0.002906681,0.006351098,0.0073248361,0.0067725667,0.007034168,0.008574709,0.0101443167,0.0100280495,0.0100425829,0.0097809816,0.0086037758,0.0057116282,0.0032700161,0.0005668028,0.0004069353,0.0003924019,0.0001162672,4.36002150943945E-005,8.72004301887889E-005,0.0004214687,0.0008574709,0.0013516067,0.0021364105,0.0038368189,0.0036042844,0.0074411034,0.0089235107,0.007964306,0.0079933728,0.0108855204,0.0116993911,0.0135742003,0.0146932725,0.0183556906,0.0153182089,0.0112197887,0.0066417661,0.0018166756,0.0007412037,0.0003924019,0.0002325345,1.45334050314648E-005,1.45334050314648E-005,0.0004796024,0.0006976034,0.0012644062,0.0020056099,0.0021364105,0.003589751,0.0072812359,0.0091269784,0.0108564536,0.0108855204,0.0138939352,0.013239932,0.0177016873,0.0246777217,0.0269013327,0.0300986818,0.0308689523,0.0323513596,0.0199398317,0.0195764966,0.0082259072,0.00473789,0.0008865377,0.0001308006,0.0002906681,0.0003052015,0.0009156045,0.0015405409,0.0024706789,0.0024270786,0.004127487,0.0053337596,0.0053773599,0.0058569622,0.0069469676,0.0096356475,0.0088944439,0.0129492639,0.0175272865,0.0205357013,0.022425044])
			f_bellavista_2410 = f_bellavista_2410.reshape(7,24)
		
			return -sum(frecuencias_region_voronoi*log( f_huerfanos_2283*divide(exp(lambdas[0]),exp(lambdas[0])+exp(lambdas[1])+1) +f_reina_2855*divide(exp(lambdas[1]),exp(lambdas[0])+exp(lambdas[1])+1) +f_bellavista_2410*divide(1,exp(lambdas[0])+exp(lambdas[1])+1)  ))

		# CALCULO DE VEROSIMILITUDES
		parametro = numpy.array([3, 3])
		resultado = minimize(verosimilitud_negativa, parametro, method='nelder-mead', options={'xtol': 1e-8, 'disp': False})

		# Se van agregando elementos a la lista
		fila = numpy.insert(proba_pertenencia(resultado.x),0, int(numero_region) )
		lista_resultados= numpy.append(lista_resultados, [fila] ,axis=0 )

		#Interrumpo el ciclo a proposito para ver resultados
		i+=1
		print(str(i) + " de " + str(len(consulta_regiones_voronoi))+" "+str(datetime.now())  )
		#	if i ==3: break



	# finalizado el ciclo "for" se guarda el arreglo
	numpy.savetxt('/media/discoExternoRAID/raul/Python/Resultados/Regiones_Voronoi/porcentajes_voronoi.csv', lista_resultados, fmt='%4f', delimiter=',', newline='\n')




####################################################################################################
# FUNCION HISTOGRAMA
####################################################################################################
def histograma( lista_regiones_voronoi = [(1,),(2,),(3,) ] ):
	"""Esta funcion genera los histogramas de las zonas de Voronoi.
		lista: Es un listado con los numeros de las zonas de Voronoi que viene de la base de datos con el formato mostrado."""

	def graficar(valores_histograma= range(100) , titulo='' , camino='' , normalizado = False):

		etiqueta_x = []
		for dia in ['Do','Lu','Ma','Mi','Ju','Vi','Sa']:
			for hora in range(24):
				if hora==0:
					etiqueta_x.append(dia)
				else:
					etiqueta_x.append('')

		# Creacion del grafico
		num_conteiners = 168
		matplotlib.pyplot.hist(valores_histograma , bins = num_conteiners, color = 'green', normed=normalizado, hold = False)
		matplotlib.pyplot.xticks(numpy.arange(168),etiqueta_x )
		matplotlib.pyplot.xlabel('Dia y Hora')
		matplotlib.pyplot.ylabel('Frecuencia')
		matplotlib.pyplot.title(titulo )
		matplotlib.pyplot.savefig( camino )

	####################################################################################################
	# DECLARACION DE TABLAS DE LA BASE DE DATOS Y CONECCION CON LA BASE DE DATOS
	####################################################################################################

	# Coneccion con la base de datos
	db = MySQLdb.connect( host = "127.0.0.1", user = "root", passwd = "eadh5148", db = "mobility", port = 5029 )
	#db = MySQLdb.connect( host = "146.83.5.100", user = "root", passwd = "eadh5148", db = "mobility", port = 5029 )
	BaseDatos = db.cursor()

	numero_graficados = 0			

	# Se realiza la consulta de la cantidad de llamadas, region por region.
	for region_voronoi in lista_regiones_voronoi:

		# La region de voronoi
		numero_region = str(region_voronoi[0])

		# Frecuencia acumulada
		suma_acumulada=0
		valores_histograma =  numpy.array([])

		# Se realiza la consulta, en base a los parametros: Region de Voronoi (Dia, Hora , Frecuencia).
		consulta_frecuencia = 'SELECT DAYOFWEEK(Fecha) as DIA, HOUR(Hora) as HORA FROM CDR_One_EFECTIVO WHERE NUM_VORONOI='+numero_region+';'

		#print "consulta region "+str(numero_region)
		# Se realiza la consulta
		BaseDatos.execute(consulta_frecuencia)
		#print "consulta terminada"

		# Se extrae la informacion entregada en una matriz
		consulta_frecuencia = numpy.array(BaseDatos.fetchall())


		try:

			# Calculo de los valores del histograma
			valores_histograma = 24*(consulta_frecuencia[:,0]-1) + consulta_frecuencia[:,1]

			#Graficos
			graficar(valores_histograma = valores_histograma  ,titulo = 'Num. region: '+str(numero_region), camino =  '/media/discoExternoRAID/raul/Python/Resultados/Regiones_Voronoi/histograma.'+str(numero_region)+'.png')
			graficar(valores_histograma = valores_histograma  ,titulo = 'Num. region (normalizado): '+str(numero_region), camino =  '/media/discoExternoRAID/raul/Python/Resultados/Regiones_Voronoi/histograma.normalizado.'+str(numero_region)+'.png', normalizado=True)

			# Contador
			numero_graficados+=1
			print "Numero de regiones ya graficadas "+str(numero_graficados)

		except IndexError:
			# celda vacia
			print "celda vacia "+str(numero_region)

		#raise NameError('alto')

	####################################################################################################
	# TIMESTAMP FIN Y PRINTEO
	####################################################################################################

	now_Fin=datetime.now()
	print('Tiempo de fin')
	print(now_Fin)
	print('\n')


####################################################################################################
# FUNCION HISTOGRAMA
####################################################################################################
def Matriz_Comportamiento_General( listado_vectores= [(1,),(2,),(3,) ] ):
	"""INCOMPLETA, NO FUNCIONA. Esta funcion lo que hace es aplicar una clasterizacion a traves de K_medias"""

	# Se declara el vector 
	data = numpy.array([])

	# Listado de antenas
	listado_antenas = numpy.unique(listado_vectores[:,0])

	# Se reordena la data, para ello se recorre el listado de antenas
	for vector in listado_antenas:

		# Se chequea si hay 168 bloques horarios
		cant_bloques_horarios = len( listado_vectores[ listado_vectores[:,0] == vector ] )
		#if cant_bloques_horarios == 168:		



		# Se agrega el vector ordenado
		data = numpy.append(data, vector_arreglado)		

	# Se realiza la clusterizacion
	k = 4
	centroides,pertenencia = scipy.cluster.vq.kmeans2(data, k, iter=100, thresh=1e-05, minit='random')	

	# Imprime el resultado
	print pertenencia

	raise NameError('alto')

####################################################################################################
# EJECUCION Y PARALELIZACION
####################################################################################################

# Si se ejecuta desde la consola
if __name__=='__main__':
	"""Lo que se busca es ejecutar este codigo. Y  que paraleliza en algunos casos"""

	clusterizacion = False
	histogramas = False
	resumen_frecuencias = True
	verosimilitud = False

	# Si lo que se busca es realizar un CSV con el resumen de frecuencias absolutas y relativas, este es la opcion
	if resumen_frecuencias:

		# Coneccion con la base de datos
		db = MySQLdb.connect( host = "127.0.0.1", user = "root", passwd = "eadh5148", db = "mobility", port = 5029 )
		#db = MySQLdb.connect( host = "146.83.5.100", user = "root", passwd = "eadh5148", db = "mobility", port = 5029 )
		BaseDatos = db.cursor()

		# CONSULTA LAS REGIONES DE VORONOI 
		consulta_regiones_voronoi = 'SELECT DISTINCT NUM_VORONOI FROM Antenas WHERE REGION = 13 ;'
		consulta_regiones_voronoi = str(consulta_regiones_voronoi)

		# Se realiza la consulta
		BaseDatos.execute(consulta_regiones_voronoi)
		# Se extrae la informacion entregada en una matriz
		consulta_regiones_voronoi = pandas.DataFrame(numpy.array(BaseDatos.fetchall()))

		BaseDatos.close()

		################# ABSOLUTO ###########################
		# Corre en paralelo
		#resultados_absolutas = piscina.map_async(vector_frecuencias_absolutas,consulta_regiones_voronoi[0]).get()
		#resultados_absolutos = vector_frecuencias_absolutas(consulta_regiones_voronoi[0][0])
		# Lo traspaso a Pandas
		#resultados_absolutas = pandas.DataFrame(resultados_absolutas)
		# Paso a un archivo CSV
		#resultados_absolutas.to_csv('/media/discoExternoRAID/raul/Python/Resultados/Regiones_Voronoi/Frecuencias_Absolutas.csv')

		################# RELATIVO ###########################
		# TESTEO
		#resultados_relativas = vector_frecuencias_relativas(consulta_regiones_voronoi[0][0])
		#resultados_relativas = map(vector_frecuencias_relativas, consulta_regiones_voronoi[0][28:] )

		# CORRE EN PARALELO
		# Se indica el numero de procesos que se desea


		piscina = Pool(processes = 6)
		piscina.map(vector_frecuencias_relativas, consulta_regiones_voronoi[0], chunksize=10 )
		piscina.close()

		#larg_lista = len(consulta_regiones_voronoi[0])/10
		#limite_inf=0
		#for limite_sup in [10*i for i in range(1,larg_lista+1)]:
		#	piscina = Pool(processes = 6)
		#	piscina.map(vector_frecuencias_relativas, consulta_regiones_voronoi[0][limite_inf:limite_sup], chunksize=6 )
		#	piscina.close()
		#	limite_inf = limite_sup


	# Si lo que se busca es el calculo de verosimilitud
	if verosimilitud:


		# Coneccion con la base de datos
		db = MySQLdb.connect( host = "127.0.0.1", user = "root", passwd = "eadh5148", db = "mobility", port = 5029 )
		#db = MySQLdb.connect( host = "146.83.5.100", user = "root", passwd = "eadh5148", db = "mobility", port = 5029 )
		BaseDatos = db.cursor()

		# CONSULTA LAS REGIONES DE VORONOI 
		consulta_regiones_voronoi = 'SELECT DISTINCT NUM_VORONOI FROM Antenas WHERE REGION = 13 ;'
		consulta_regiones_voronoi = str(consulta_regiones_voronoi)

		print "termino consulta sobre el listado de antenas"
		# Se realiza la consulta
		BaseDatos.execute(consulta_regiones_voronoi)
		# Se extrae la informacion entregada en una matriz
		consulta_regiones_voronoi = BaseDatos.fetchall()

		# Se entrega los datos a la funcion de verosimilitud
		verosimilitud(consulta_regiones_voronoi) 



	# Si lo que se busca es realizar un K_medias sobre todos los vectores
	if clusterizacion:

		# Coneccion con la base de datos
		db = MySQLdb.connect( host = "127.0.0.1", user = "root", passwd = "eadh5148", db = "mobility", port = 5029 )
		#db = MySQLdb.connect( host = "146.83.5.100", user = "root", passwd = "eadh5148", db = "mobility", port = 5029 )
		BaseDatos = db.cursor()

		# CONSULTA LAS REGIONES DE VORONOI 
		consulta_regiones_voronoi = 'SELECT *, COUNT(*) FROM (SELECT NUM_VORONOI,DAYOFWEEK(Fecha) AS Dia,HOUR(Hora) AS Hora FROM CDR_One_EFECTIVO ) AS Tabla GROUP BY NUM_VORONOI , Dia , Hora ORDER BY NUM_VORONOI,Dia,Hora;'
		consulta_regiones_voronoi = str(consulta_regiones_voronoi)

		# Se realiza la consulta
		BaseDatos.execute(consulta_regiones_voronoi)
		# Se extrae la informacion entregada en una matriz
		consulta_regiones_voronoi = numpy.array(BaseDatos.fetchall())
		print "termino consulta sobre el listado de antenas"

		# Se envia la consulta a la funcion
		Matriz_Comportamiento_General(consulta_regiones_voronoi)



	# Si lo que se busca es realizar graficos de histogramas, de TODAS las regiones
	if histogramas:
		jobs=[]

		# Coneccion con la base de datos
		db = MySQLdb.connect( host = "127.0.0.1", user = "root", passwd = "eadh5148", db = "mobility", port = 5029 )
		#db = MySQLdb.connect( host = "146.83.5.100", user = "root", passwd = "eadh5148", db = "mobility", port = 5029 )
		BaseDatos = db.cursor()

		# CONSULTA LAS REGIONES DE VORONOI 
		consulta_regiones_voronoi = 'SELECT DISTINCT NUM_VORONOI FROM Antenas WHERE REGION = 13 ;'
		consulta_regiones_voronoi = str(consulta_regiones_voronoi)

		print "termino consulta sobre el listado de antenas"
		# Se realiza la consulta
		BaseDatos.execute(consulta_regiones_voronoi)
		# Se extrae la informacion entregada en una matriz
		consulta_regiones_voronoi = BaseDatos.fetchall()

		# Creacion de la lista que albergara las listas
		Listado_de_Listas = []

		# Particion de la lista
		# Declaracion de las variables iniciales
		inicio = 0
		termino = len(consulta_regiones_voronoi)/8
		largo_intervalo = termino
		for indice in range(9):

			Listado_de_Listas.append(consulta_regiones_voronoi[inicio:termino])
			inicio += largo_intervalo
			termino += largo_intervalo

		# Corre en paralelo
		print "inicio multiprocesamiento"
		for lista in Listado_de_Listas:
			#histograma(lista)
			proceso = multiprocessing.Process(target = histograma, args=(lista,))
			jobs.append(proceso)
			proceso.start()


