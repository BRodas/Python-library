""" Este archivo lo que hace es agarrar el archivo entrante y crear varios archivos listos para aplicar un LDA"""


# Se define la ubicacion del archivo a abrir
ubicacion_archivo_origen = '/home/bernardo/Experimentos_Mobility/26_Comparacion_Comportamiento_individual/Muestra10000/general/todos.general.csv'
ubicacion_destino = '/home/bernardo/Experimentos_Mobility/27_Comportamiento_Grupal/documentos_general_LDA/'

# Declaracion de variables iniciales
numero_estudio = 'inicio'
bolsa_numeros_voronoi = []

with open(ubicacion_archivo_origen) as archivo:
	# Lee linea por linea el archivo
	for line in archivo:

		# Se extrae el numero telefonico y la region de voronoi de interes
		numero = line.split(',')[0]
		num_voronoi = int(line.split(',')[-1])

		# Si el numero en estudio es el mismo
		if numero_estudio == numero:
			# Se agrega el numero a la bolsa
			bolsa_numeros_voronoi.append(str(num_voronoi))

		else:
			# Escribe el archivo
			if not (numero_estudio == 'inicio'):
				escribir = open(ubicacion_destino+numero+'.csv','w')
				bolsa_numeros_voronoi[-1] = bolsa_numeros_voronoi[-1]+'\r\n'
				escribir.write(','.join(bolsa_numeros_voronoi))
				escribir.close()
				# Vacia la bolsa
				bolsa_numeros_voronoi = []

			# Reemplaza el numero en estudio
			numero_estudio = numero
			bolsa_numeros_voronoi.append(str(num_voronoi))

