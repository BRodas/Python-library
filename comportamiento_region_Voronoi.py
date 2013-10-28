#!/usr/bin/python2.7

"""
####################################################################################################
MODIFICACIONES
####################################################################################################

Wed 24 Jul 2013 07:27:35 PM CLT 
Se modifica e incluye el paquete SciPy
Se en vez de usar armar una query, usa una Vista.

dom jul  7 12:40:19 CLT 2013
Se incorpora Numpy

"""



####################################################################################################
# SE IMPORTAN LAS LIBRERIAS CORRESPONDIENTES
####################################################################################################
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
#import matplotlib.pyplot as plot



####################################################################################################
# FUNCION DE PROBABILIDADES
####################################################################################################
def proba_pertenencia(x):
	"""Probabilidaddes de pertenencia, dado parametros LAMBDAS"""
	return array([divide(exp(x[0]),exp(x[0])+exp(x[1])+1) ,divide(exp(x[1]),exp(x[0])+exp(x[1])+1),divide(1,exp(x[0])+exp(x[1])+1) ])


####################################################################################################
# DECLARACION DE TABLAS DE LA BASE DE DATOS Y CONECCION CON LA BASE DE DATOS
####################################################################################################
#Antenas = 'Antenas_Limpio_Nov12Ene13'
#Antenas = 'Antenas'
#Interacciones = 'CDR_Limpio_General'
#Interacciones = 'CDR_One_Limpio'
#Interacciones = 'CDR_One_BRUTO'

# Coneccion con la base de datos
db = MySQLdb.connect( host = "127.0.0.1", user = "root", passwd = "eadh5148", db = "mobility", port = 5029 )
#db = MySQLdb.connect( host = "146.83.5.100", user = "root", passwd = "eadh5148", db = "mobility", port = 5029 )
BaseDatos = db.cursor()


####################################################################################################
# ANALISIS POR REGION DE VORONOI
####################################################################################################

# CONSULTA LAS REGIONES DE VORONOI 
consulta_regiones_voronoi = 'SELECT DISTINCT NUM_VORONOI FROM Antenas WHERE REGION = 13 ;'
consulta_regiones_voronoi = str(consulta_regiones_voronoi)
# Se realiza la consulta
BaseDatos.execute(consulta_regiones_voronoi)
# Se extrae la informacion entregada en una matriz
consulta_regiones_voronoi = BaseDatos.fetchall()

# En este arreglo de numpy se guardaran las probabilidades
lista_resultados= empty((0,4))


# Este "i" es de testeo, es borrable
i=0

# Se realiza la consulta de la cantidad de llamadas, region por region.
for region_voronoi in consulta_regiones_voronoi:

	# La region de voronoi
	numero_region = str(region_voronoi[0])

	# Se realiza la consulta, en base a los parametros: Region de Voronoi (Dia, Hora , Frecuencia).
	consulta_frecuencia = 'SELECT DIA,HORA , COUNT(*)  FROM (select DAYOFWEEK(Fecha) AS DIA,  HOUR(Hora) AS HORA , NUM_VORONOI FROM CDR_One_BRUTO_02, Antenas WHERE CDR_One_BRUTO_02.BTS_ID = Antenas.BTS_ID AND NUM_VORONOI = '+numero_region+') AS TABLA GROUP BY DIA,HORA ;'
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
# GUARDADO DE LOS ARCHIVOS CON ESTADISTICAS BASICAS
####################################################################################################

#	plot.plot( arange( 1, 168, 1 ) ,probabilidad_region_voronoi, 'ro')
#	plot.savefig('/media/discoExternoRAID/raul/Python/Resultados/Regiones_Voronoi/'+str(numero_region)+'densidad.png')

	####### GUARDADO CON NIVEL DE DETALLE
	# Se guarda el resultado
#	nombre_archivo ='/media/discoExternoRAID/raul/Python/Resultados/Regiones_Voronoi/'+str(numero_region)+'.frecuencias.csv'
#	numpy.savetxt(nombre_archivo, frecuencias_region_voronoi , delimiter=',', fmt='%.2f')

	###### GUARDADO RESUMIDO, MEDIAS
#	nombre_archivo ='/media/discoExternoRAID/raul/Python/Resultados/Regiones_Voronoi/'+str(numero_region)+'.media.csv'
#	numpy.savetxt(nombre_archivo, numpy.mean(frecuencias_region_voronoi[0], axis = 0) , delimiter=',', fmt='%.2f')

	##### GUARDADO RESUMIDO, DESVIACIONES ESTANDARES
#	nombre_archivo ='/media/discoExternoRAID/raul/Python/Resultados/Regiones_Voronoi/'+str(numero_region)+'.desvEst.csv'
#	numpy.savetxt(nombre_archivo, numpy.std(frecuencias_region_voronoi[0], axis = 0) , delimiter=',', fmt='%.2f')

	##### GUARDADO RESUMIDO, mediana
#	nombre_archivo ='/media/discoExternoRAID/raul/Python/Resultados/Regiones_Voronoi/'+str(numero_region)+'.mediana.csv'
#	numpy.savetxt(nombre_archivo, numpy.median(frecuencias_region_voronoi[0], axis = 0) , delimiter=',', fmt='%.2f')


	##### GUARDADO RESUMIDO,minimo 
#	nombre_archivo ='/media/discoExternoRAID/raul/Python/Resultados/Regiones_Voronoi/'+str(numero_region)+'.minimo.csv'
#	numpy.savetxt(nombre_archivo, numpy.amin(frecuencias_region_voronoi[0], axis = 0) , delimiter=',', fmt='%.2f')


	##### GUARDADO RESUMIDO,maximo 
#	nombre_archivo ='/media/discoExternoRAID/raul/Python/Resultados/Regiones_Voronoi/'+str(numero_region)+'.maximo.csv'
#	numpy.savetxt(nombre_archivo, numpy.amax(frecuencias_region_voronoi[0], axis = 0) , delimiter=',', fmt='%.2f')


####################################################################################################
# TIMESTAMP FIN Y PRINTEO
####################################################################################################

now_Fin=datetime.now()
print('Tiempo de fin')
print(now_Fin)
print('\n')
