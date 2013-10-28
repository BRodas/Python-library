"""
Thu 25 Jul 2013 05:43:29 PM CLT 
Este Script se ha creado con dos propositos:

1) Corregir un error de carga
2) Corregir los futuros TXT que lleguen de Movistar


"""

####################################################################################################
# SE IMPORTAN LAS LIBRERIAS CORRESPONDIENTES
####################################################################################################

# Se importa la libreria que permite tratamiento de fechas
from datetime import datetime

####################################################################################################
# SCRIPT
####################################################################################################
now_Inicio=datetime.now()


#Funcion "cambiaFormatoFecha"
	# cambia el formato de 03-07-2013 a 2013-07-03


# Se define el camino al archivo destino donde se escribiran los resultados
destino = '/media/discoExternoRAID/raul/borrar.csv'
leer = open(destino,'r')
destino = '/media/discoExternoRAID/raul/borrar_resultado.csv'
escribir = open(destino,'w')


#Las variables con su declaracion
i=0
j=1

#Conteo numero de lineas
while i<j:

	#Leer la linea
	fila = leer.readline()
	#Si no hay fila cancela
	if not fila: 
		i = 1
	# Si hay continua
	else:
		# Separacion en base al caracter
		fila=fila.split('|')
		# extraccion de las comillas del campo FECHA_HORA
		fila[0] = fila[0][1:-1]
		# Separacion del ano
		fila.insert(0, fila[0][0:10])
		# Dar vuelta el dia y el ano
		fila[0]=fila[0][-4:]+fila[0][2:-4]+fila[0][:2]
		# solo hora en el elemento 1
		fila[1]=fila[1][11:]
		# Escribe la linea en el archivo
		escribir.write('|'.join(fila))


# cerrar la lectura
leer.close()
escribir.close()

#los timestamp finales
print('\n')
print('Tiempo de inicio')
print(now_Inicio)
print('\n')
print('Tiempo de fin')
now_Fin=datetime.now()
print(now_Fin)
