# Trabajar MySQL/Infobright
import MySQLdb

# Se importa la libreria que permite tratamiento de fechas
from datetime import date,timedelta,datetime


####################################################################################################
# TIMESTAMP
####################################################################################################
now=datetime.now()
print('\n')
print('Tiempo de inicio')
print(now)



# Se crea la coneccion con la base de datos
db = MySQLdb.connect( host = "127.0.0.1", user = "root", passwd = "eadh5148", db = "mobility", port = 5029 )
BaseDatos = db.cursor()

# Se realiza la primera consulta de donde se saca la muestra
consulta_muestra = 'select NUM_CELULAR_CONTRATO FROM Contratos_Canon_Nov12  where REGION_CONTRATO= "RM" ORDER BY RAND() LIMIT 1000;'
consulta_muestra = str(consulta_muestra)
BaseDatos.execute(consulta_muestra)
# Se extrae la informacion entregada en una lista
listaNumeros = BaseDatos.fetchall()

# Se abre el archivo donde se escribira
Escribir = open( '/media/discoExternoRAID/raul/muestraCDROne.csv', 'a')

# Se recorre el listado numero por numero
for numero in listaNumeros:



	# Se escriben los resultados en un listado en CSV
	consulta = 'SELECT DISTINCT NUMERO, STR_TO_DATE(Fecha_Hora,"%d-%m-%Y") AS FECHA, time(substring(Fecha_Hora,12,8)) AS HORA ,LATITUD , LONGITUD  FROM Antenas_Limpio_Nov12Ene13 , (SELECT Fecha_Hora, Origen as NUMERO, BTS_ID FROM CDR_One_BRUTO WHERE Origen= '+str(numero[0])+' AND Direccion = "Origen"  UNION  SELECT Fecha_Hora, Destino, BTS_ID FROM CDR_One_BRUTO WHERE Destino= '+str(numero[0])+' AND Direccion = "Destino") AS Tabla WHERE Tabla.BTS_ID = Antenas_Limpio_Nov12Ene13.BTS_ID;'
	consulta = str(consulta)
	BaseDatos.execute(consulta)
	# Se extrae la informacion entregada en una lista
	listaInteracciones = BaseDatos.fetchall()

	# Se anotan una por una las interacciones
	for interaccion in listaInteracciones:

		#print interaccion

		# Se limpia la linea
		linea = ''
		# Se arma la linea a escribir
		for campo in interaccion:
			linea = linea + ',' + str(campo)
		# Se escribe la linea armada
		Escribir.write(linea+'\n')

# Se cerro el archivo donde se escribio
Escribir.close()



####################################################################################################
# TIMESTAMP
####################################################################################################
now=datetime.now()
print('Tiempo de fin')
print(now)
print('\n')

