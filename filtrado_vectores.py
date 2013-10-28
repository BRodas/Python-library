
#############################################
# LIBRERIAS
############################################
from lib_python import debugear
import numpy
import pandas



################ LA FUNCION QUE CALCULA LA DISTANCIA MANHATAN ENTRE DOS VECTORES
def distancia(vector_1, vector_2):
    return numpy.absolute(vector_1 - vector_2 ).sum()
###############################################################################

# El camino de donde se extraen la pertenencia de las regiones a los cluters
camino = '/media/discoExternoRAID/raul/Experimentos_Mobility/25_Comportamiento_Suelo/K-Means_Miguel/01_09_assignments_02.csv'
# la variable que se usa es datos_brutos_pertenencia
datos_brutos_pertenencia = pandas.read_csv( camino , index_col=False )
arreglo_pertenencia_clusters = datos_brutos_pertenencia[['voronoi_cell_id','asignaciones_iteracion_10']].values
cluster_trabajo = arreglo_pertenencia_clusters[arreglo_pertenencia_clusters[:,1]==1][:,0]
cluster_residencial = arreglo_pertenencia_clusters[arreglo_pertenencia_clusters[:,1]!=1][:,0]

# Ahora voy por las frecuencias de cada region
camino_frecuencias_regiones = '/media/discoExternoRAID/raul/Experimentos_Mobility/25_Comportamiento_Suelo/Frecuencias_Relativas.csv'
frecuencias_regiones_voronoi  = numpy.loadtxt(camino_frecuencias_regiones, delimiter=',')

# Se extraen los vectores tipos de cada tipo
camino_clusters_tipo = '/media/discoExternoRAID/raul/Experimentos_Mobility/25_Comportamiento_Suelo/K-Means_Miguel/01_09_meta_centroids_02.csv'
vector_tipo_cluster_residencial = numpy.loadtxt(camino_clusters_tipo, delimiter=',')[0,:]
vector_tipo_cluster_trabajo = numpy.loadtxt(camino_clusters_tipo, delimiter=',')[1,:]

# Se crea el arreglo con las distancias a los vectores tipos
distancias_residencial = numpy.array([ [distancia(vector_tipo_cluster_residencial , frecuencias_regiones_voronoi[ frecuencias_regiones_voronoi[:,0]==reg][0][1:]  ) , reg] for reg in cluster_residencial ])
distancias_trabajo = numpy.array([ [distancia(vector_tipo_cluster_trabajo , frecuencias_regiones_voronoi[ frecuencias_regiones_voronoi[:,0]==reg][0][1:]  ) , reg] for reg in cluster_trabajo ])

# Para ordenar el vector primero se mete en un DataFrame
data_frame_residencial  = pandas.DataFrame(distancias_residencial[:,0] , index = distancias_residencial[:,1] , columns = ['distancia'])
data_frame_trabajo  = pandas.DataFrame(distancias_trabajo[:,0] , index = distancias_trabajo[:,1] , columns = ['distancia'])

# Luego se ordenan los DataFrame
data_frame_residencial = data_frame_residencial.sort(columns='distancia')
data_frame_trabajo = data_frame_trabajo.sort(columns='distancia')

# Ahora lo que se busca es guardar los vectores mas alejados de los centroides
# Para ello lo primero es guardar las frecuencias en un DataFrame, ya que resulta mas facil manipular
data_frame_frecuencias = pandas.DataFrame( frecuencias_regiones_voronoi[:,1:], index= frecuencias_regiones_voronoi[:,0] )

# La concatenacion es correcta de esta manera
# Notese que crea este nuevo par de DataFrames con los indices ordenados segun el segundo DataFrame que se pasa en la concatenacion, este segundo DataFrame tiene los indices ordenados segun la distancia que hay hacia el vector tipo, por lo tando los DataFrame creados ya estan ordenados.
data_frame_residencial_vectores = pandas.concat( [data_frame_frecuencias, data_frame_residencial] , join='inner', axis=1)
data_frame_trabajo_vectores = pandas.concat( [data_frame_frecuencias, data_frame_trabajo] , join='inner', axis=1)

# De todas maneras se van a ordenar igual de nuevo.
data_frame_trabajo_vectores = data_frame_trabajo_vectores.sort(columns='distancia') 
data_frame_residencial_vectores = data_frame_residencial_vectores.sort(columns = 'distancia')
# AHORA VOY A SELECCIONAR LOS ULTIMOS
for porcentaje in [(.1 +0.05*i ) for i in range(5)]:
	
	# Seleccion de las ultimas filas del DataFrame
	residencial_guardar = data_frame_residencial_vectores.tail( int(len(data_frame_residencial_vectores)*porcentaje ) )[range(168)]
	trabajo_guardar = data_frame_trabajo_vectores.tail( int(len(data_frame_residencial_vectores)*porcentaje) )[range(168)]

	# El archivo donde se guardaran
	camino_guardar_residencial = '/media/discoExternoRAID/raul/Python/Resultados/Regiones_Voronoi/residencial_alejados_%s.csv'%(porcentaje)
	camino_guardar_trabajo = '/media/discoExternoRAID/raul/Python/Resultados/Regiones_Voronoi/trabajo_alejados_%s.csv'%(porcentaje)

	# Se guardan los archivos
	residencial_guardar.to_csv(camino_guardar_residencial, header=False)
	trabajo_guardar.to_csv(camino_guardar_trabajo, header=False)



	# Seleccion de las primeras filas del DataFrame
	residencial_guardar = data_frame_residencial_vectores.head( int(len(data_frame_residencial_vectores)*(1-porcentaje) ) )[range(168)]
	trabajo_guardar = data_frame_trabajo_vectores.head( int(len(data_frame_residencial_vectores)*(1-porcentaje)) )[range(168)]

	# El archivo donde se guardaran
	camino_guardar_residencial = '/media/discoExternoRAID/raul/Python/Resultados/Regiones_Voronoi/residencial_cercanos_%s.csv'%(1-porcentaje)
	camino_guardar_trabajo = '/media/discoExternoRAID/raul/Python/Resultados/Regiones_Voronoi/trabajo_cercanos_%s.csv'%(1-porcentaje)

	# Se guardan los archivos
	residencial_guardar.to_csv(camino_guardar_residencial, header=False)
	trabajo_guardar.to_csv(camino_guardar_trabajo, header=False)

