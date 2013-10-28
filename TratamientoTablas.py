# RUTINA ORIENTADA AL TRATAMIENTO DE DOCUMENTOS, CON VARIAS OPCIONES


import os
import sys

# Libreria que permite el tratamiento de documentos
from lib_python import LecturaArchivo


print('\n'+"Esta rutina esta orientada a tratar tablas de datos."+'\n'+'\n')

print ('Archivo de Origen')
UbicacionOrigen = '/media/discoExternoRAID/raul/01B_DatosIndra/doc.kml'
print (UbicacionOrigen+'\n')


print ('Archivo de Destino')
UbicacionDestino = '/media/discoExternoRAID/raul/01B_DatosIndra/ListadoAntenasModificado.kml'
print (UbicacionDestino+'\n')

while 1:

	

	print("Elige opcion:"+'\n')
	print("Si quieres una descripcion elige la opcion seguida de una 'a'. Por ejemplo: '8a'"+'\n')
	print("1:Borrar la primera linea del archivo"+'\n')
	#print("2:Agregar un indice auto incremental al archivo"+'\n')
	print("3:Extraccion de lineas al azar"+'\n')
	#print("4:Extraccion amplia selectiva de CDR. Corresponde extraer CDRs correspondientes a un listado de numero de telefono de celular"+'\n')
	print("5:Extraccion de una linea puntual"+'\n')
	print("6:Contador de lineas que excedan el numero de tabs"+'\n')
	print("7:Eliminador de filas con excesos de Tabs"+'\n')
	print("8:Cuenta bloques (Orientado a lenguajes de etiquetas) "+'\n')
	print("9:Reemplazo tipo 01 (Orientado a lenguajes de etiquetas) "+'\n')
	print("S:Salir"+'\n')
	EntradaTeclado = raw_input("Ingresa la opcion: ")



	print(EntradaTeclado)	



	if (EntradaTeclado == "1"):
		LecturaArchivo.BPLinea(UbicacionOrigen,UbicacionDestino)

	#if (EntradaTeclado == "2"):
	#	EntradaTeclado2 = 2

	if (EntradaTeclado == "3"):
		LecturaArchivo.LineAzar(UbicacionOrigen,UbicacionDestino)

	#if (EntradaTeclado == "4"):
	#	LecturaArchivo.ListadoSelectivo(UbicacionOrigen,UbicacionDestino)

	if (EntradaTeclado == "5"):
		LecturaArchivo.LineaPuntual(UbicacionOrigen)

	if (EntradaTeclado == "6"):
		LecturaArchivo.NumLinTabsExcecivos(UbicacionOrigen,UbicacionDestino)

	if (EntradaTeclado == "7"):
		LecturaArchivo.ExcesoTabs(UbicacionOrigen,UbicacionDestino)

	if (EntradaTeclado == "8"):
		LecturaArchivo.EtiquetaAbreCierra(UbicacionOrigen)

	if (EntradaTeclado == "8a"):
		print('Funcion pensada en lenguajes basados en etiquetas: XML, HTML, KML, etc. Cuenta el numero de lineas correspondientes a algun bloque.')

	if (EntradaTeclado == "9"):
		LecturaArchivo.ReemplazoTipoUno(UbicacionOrigen,UbicacionDestino)

	if (EntradaTeclado == "9a"):
		print('Funcion de reemplazo especial. Esta funcion recive dos valores, ambos parte de un archivo kml. Por ejemplo sean tres lineas de un archivo kml: "<name>kml_1</name>" , "<th>CELLBTS</th>" y "<td>SALCEU04_2-1</td>" . Uno ingresa como PRIMER valor SOLO "<name>" y luego como SEGUNDO valor "<th>CELLBTS</th>", el programa reemplaza los contenido en las etiquetas "<name>" y "</name>", por lo contenido en las etiquetas "<td>" y "</td>".')


	EntradaTeclado = raw_input("Salir? [s/n] ")
	if (EntradaTeclado == "s") |(EntradaTeclado == "S"): break
