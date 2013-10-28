from datetime import date,timedelta
from decimal import *

############################################################################
"""Parseador de consultar MySQL. Se debe entregar la cantidad de campos"""

# Se entrega la consulta correspondiente
def general(consulta = "", cantCampos = 1):

	# Se lleva el string de respuesta a un listados de consulta.
	listado = consulta.split()
	# tupla
	fila = []
	# el listado respuesta
	listResp = []
	# Recorrido de la lista
	recorrido = range(len(listado)/cantCampos)
	for i in recorrido:
		# Si se lleva a la ultima linea se rompe el for	
		if i==recorrido[-1]:break
		# Esta es la lista que va agrupando las filas
		fila = []
		# Se recorre la fila elemento por elemento		
		for j in range(cantCampos):
			a_agregar = listado[i*cantCampos+ j + cantCampos ]
			fila.append(a_agregar)
		# Esta es la lista final
		listResp.append(fila)
	# se devuelde el listado de tuplas
	return listResp






############################################################################
# PARSEADOR DE CONSULTAS SQL
# Se entrega la consulta correspondiente
def sql01(consulta):

	# Se lleva el string de respuesta a un listados de consulta.
	listado = consulta.split()
	# tupla
	tupla = ()
	# el listado respuesta
	listResp = []
	# Recorrido de la lista
	recorrido = range(len(listado)/6)
	for i in recorrido:

		# Si se lleva a la ultima linea se rompe el for	
		if i==recorrido[-1]:break

		# Se transforman el tipo de datos
		numero = long(listado[i*6+6])
		BTS = str(listado[i*6+7])
		fecha = date( int(listado[i*6+8][0:4]) , int(listado[i*6+8][5:7]), int(listado[i*6+8][8:10]))
		hora = timedelta( seconds = int(listado[i*6+9][6:8]) , minutes= int(listado[i*6+9][3:5]) , hours=int(listado[i*6+9][0:2])  )
		latitud = Decimal(listado[i*6+10])
		longitud = Decimal(listado[i*6+11])
		tupla = (numero,BTS,fecha,hora,latitud,longitud)
		listResp.append(tupla)

	# se devuelde el listado de tuplas
	return listResp








############################################################################
# PARSEADOR DE CONSULTAS SQL
# Se entrega la consulta correspondiente
def sql02(consulta):

	# Se lleva el string de respuesta a un listados de consulta.
	listado = consulta.split()
	# tupla
	tupla = ()
	# el listado respuesta
	listResp = []

	# Recorrido de la lista
	recorrido = range(len(listado)/3)
	for i in recorrido:

		# Si se lleva a la ultima linea se rompe el for	
		if i==recorrido[-1]:break

		# Se transforman el tipo de datos
		numero = long(listado[i*3+3])
		coordenadas = str(listado[i*3+4])
		frecuencia = long(listado[i*3+5])
		tupla = (numero, coordenadas , frecuencia)
		listResp.append(tupla)

	# se devuelde el listado de tuplas
	return listResp
