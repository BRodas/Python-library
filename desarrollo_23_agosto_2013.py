# IPython log file


import numpy
import pandas


# El camino de donde se extraen la pertenencia de las regiones a los cluters
camino = '/media/discoExternoRAID/raul/Experimentos_Mobility/25_Comportamiento_Suelo/K-Means_Miguel/01_09_assignments_02.csv'
# la variable que se usa es datos_brutos_pertenencia
datos_brutos_pertenencia = pandas.read_csv( camino , index_col=False )
arreglo_pertenencia_clusters = datos_brutos_pertenencia[['voronoi_cell_id','asignaciones_iteracion_10']].values
cluster_trabajo = arreglo_pertenencia_clusters[arreglo_pertenencia_clusters[:,1]==1][:,0]
cluster_residencial = arreglo_pertenencia_clusters[arreglo_pertenencia_clusters[:,1]!=1][:,0]

