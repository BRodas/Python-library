#Importa la libreria correspondiente al tratamiento del tiempo
from datetime import date,timedelta
#Importa la libreria para el tratamiento de Decimal('3.66')
from decimal import *

#############################################################################

def estilos():
	"""Funcion que define los estilos"""

	codigo = """
	<StyleMap id="msn_ltblu-pushpin">
		<Pair>
			<key>normal</key>
			<styleUrl>#sn_ltblu-pushpin</styleUrl>
		</Pair>
		<Pair>
			<key>highlight</key>
			<styleUrl>#sh_ltblu-pushpin</styleUrl>
		</Pair>
	</StyleMap>
	<Style id="sh_purple-pushpin">
		<IconStyle>
			<scale>1.3</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/purple-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
	</Style>
	<StyleMap id="msn_grn-pushpin">
		<Pair>
			<key>normal</key>
			<styleUrl>#sn_grn-pushpin</styleUrl>
		</Pair>
		<Pair>
			<key>highlight</key>
			<styleUrl>#sh_grn-pushpin</styleUrl>
		</Pair>
	</StyleMap>
	<Style id="sn_pink-pushpin">
		<IconStyle>
			<scale>1.1</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/pink-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
	</Style>
	<Style id="sn_grn-pushpin">
		<IconStyle>
			<scale>1.1</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/grn-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
	</Style>
	<Style id="sn_ltblu-pushpin">
		<IconStyle>
			<scale>1.1</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ltblu-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
	</Style>
	<Style id="sn_purple-pushpin">
		<IconStyle>
			<scale>1.1</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/purple-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
	</Style>
	<StyleMap id="msn_purple-pushpin">
		<Pair>
			<key>normal</key>
			<styleUrl>#sn_purple-pushpin</styleUrl>
		</Pair>
		<Pair>
			<key>highlight</key>
			<styleUrl>#sh_purple-pushpin</styleUrl>
		</Pair>
	</StyleMap>
	<Style id="sn_blue-pushpin">
		<IconStyle>
			<scale>1.1</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/blue-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
	</Style>
	<Style id="sh_blue-pushpin">
		<IconStyle>
			<scale>1.3</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/blue-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
	</Style>
	<StyleMap id="msn_blue-pushpin">
		<Pair>
			<key>normal</key>
			<styleUrl>#sn_blue-pushpin</styleUrl>
		</Pair>
		<Pair>
			<key>highlight</key>
			<styleUrl>#sh_blue-pushpin</styleUrl>
		</Pair>
	</StyleMap>
	<Style id="sh_pink-pushpin">
		<IconStyle>
			<scale>1.3</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/pink-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
	</Style>
	<StyleMap id="msn_pink-pushpin">
		<Pair>
			<key>normal</key>
			<styleUrl>#sn_pink-pushpin</styleUrl>
		</Pair>
		<Pair>
			<key>highlight</key>
			<styleUrl>#sh_pink-pushpin</styleUrl>
		</Pair>
	</StyleMap>
	<Style id="sh_grn-pushpin">
		<IconStyle>
			<scale>1.3</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/grn-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
	</Style>
	<Style id="sh_ltblu-pushpin">
		<IconStyle>
			<scale>1.3</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ltblu-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
	</Style>"""

	estilos =["sh_purple-pushpin","sn_pink-pushpin","sn_grn-pushpin","sn_ltblu-pushpin","sn_purple-pushpin","sn_blue-pushpin","sh_pink-pushpin","sh_grn-pushpin","sh_ltblu-pushpin"]

	diccionarioEstilos = {'Codigo': codigo ,'Estilos': estilos}
	return diccionarioEstilos


#############################################################################


def etiquetas( etiqueta , contenidoEtiqueta  , contenido):
	"""Funcion para la creacion de etiquetas"""
	etiquetaLinea = "<"+str(etiqueta)+" "+str(contenidoEtiqueta)+">"+str(contenido)+"</"+str(etiqueta)+">"+'\n'
	return etiquetaLinea



#############################################################################


def archivoXML( Diccionario , NombreArchivo = 'Resultados.xml', NombreEj = 'testeo'):
	"""Agregacion de puntos al archivo XML, para ello se debe entregar un diccionario. El arbol de este es: EL Diccionario con VARIOS Diccionarios, y cada uno a su ves con VARIAS Listas"""

	# Debo crear un archivo donde se vallan grabando las lineas que escribo, recordar que debo cerrar luego este open. Luego para escribir: trazadoKML.write(contenido)

	# Se define el destino del archivo
	Destino = '/media/discoExternoRAID/raul/Python/Resultados/'+NombreArchivo

	# Se abre el archivo a escribit
	archivoXML = open( Destino, 'a')

	#Variable que cambia el color de los pinches
	i=0

	# Etiqueta "folder_1"
	archivoXML.write('\t'+'<Folder>'+'\n')
	# Nombre del "folder_1"
	archivoXML.write('\t'+'\t'+etiquetas('name','',NombreEj))

	# Aqui comienzan las carpetas varias, o sea el uso del diccionario
	for fecha, fecha_contenido in iter(sorted(Diccionario.iteritems())):

		# Etiqueta "folder_1"
		archivoXML.write('\t'+'<Folder>'+'\n')
		# Nombre del "folder_1"
		archivoXML.write('\t'+'\t'+etiquetas('name','',fecha))
		
		# Aqui recorre el bloque horario de la fecha en que se esta
		for horaLimite, bloque in iter(sorted(fecha_contenido.iteritems())):

			# Esta variable va cambiando el color de los pinches
			i+=1
			i= i%int(len(estilos()['Estilos'])-1)


			# Etiqueta "folder_1_1"
			archivoXML.write('\t'+'\t'+'\t'+'<Folder>'+'\n')
			
			# Nombre del "folder_1_1"
			archivoXML.write('\t'+'\t'+'\t'+'\t'+etiquetas('name','',horaLimite))
			
		
			# Escritura de los varios PLACEMARKS
			for CDR in range(len(bloque)):
				

					# Escritura de los placemark
					archivoXML.write('\t'+'\t'+'\t'+'\t'+'<Placemark>'+'\n')

					# Nombre del placemark
					archivoXML.write('\t'+'\t'+'\t'+'\t'+'\t'+etiquetas('name','',str(bloque[CDR][1][0])+' '+str(bloque[CDR][0]) ))

					# Indica si el pinche esta prendido o apagado
					archivoXML.write("<visibility>0</visibility>")

					# Escritura de las coordenadas geograficas
					archivoXML.write('\t'+'\t'+'\t'+'\t'+'\t'+'<LookAt>'+'\n')

					# Etiqueta de longitud
					archivoXML.write('\t'+'\t'+'\t'+'\t'+'\t'+'\t'+etiquetas('longitude','',str(bloque[CDR][1][2] )))

					# Etiqueta de latitud
					archivoXML.write('\t'+'\t'+'\t'+'\t'+'\t'+'\t'+etiquetas('latitude','', str(bloque[CDR][1][1]) ))

					# Etiqueta de latitud
					archivoXML.write('\t'+'\t'+etiquetas('range','','1000'))


					# Escritura de las coordenadas geograficas
					archivoXML.write('\t'+'\t'+'\t'+'</LookAt>'+'\n')


					# Estilo de la escritura
					archivoXML.write('\t'+'\t'+etiquetas('styleUrl','', '#'+estilos()['Estilos'][i] ))

					# Ubicacion geografica del pinche
					coordenadasPinche = etiquetas('coordinates','', str(bloque[CDR][1][2])+','+str(bloque[CDR][1][1])+',0')
					archivoXML.write('\t'+'\t'+etiquetas('Point','', coordenadasPinche ))
			
					# Escritura de los placemark
					archivoXML.write('\t'+'\t'+'\t''</Placemark>'+'\n')




			# FIN Escritura de los varios PLACEMARKS


			# Etiqueta "folder_1_1"
			archivoXML.write('\t'+'\t'+'</Folder>'+'\n')


		# Etiqueta "folder_1"
		archivoXML.write('\t'+'</Folder>'+'\n')


	# Etiqueta "folder_1"
	archivoXML.write('\t'+'</Folder>'+'\n')

	#Cierre del archivo
	archivoXML.close()

	return 




###########################################################################



def aperturaXML(NombreArchivo = 'Resultados.xml'):
	"""Crea la apertura del archivo XML, ocupa la funcion de estilos"""

	# Se define el destino del archivo
	Destino = '/media/discoExternoRAID/raul/Python/Resultados/'+NombreArchivo

	# Se abre el archivo a escribit
	archivoXML = open( Destino, 'w')

	
	#El encabezado del archivo:
	archivoXML.write('<?xml version="1.0" encoding="UTF-8"?>'+'\n')
	
	# Primera etiqueta abertura
	archivoXML.write('<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">'+'\n')

	# Ahora comienta el llenado intermedio
	archivoXML.write('<Document>'+'\n')
	# Nombre del documento
	archivoXML.write('\t'+etiquetas('name','',str(NombreArchivo)))
	# Los estilos
	archivoXML.write('\t'+estilos()['Codigo']+'\n'+'\n')


	#Cierre del archivo
	archivoXML.close()


############################################################################

def cierreXML(NombreArchivo = 'Resultados.xml'):
	"""Crea el cirre del XML, las etiquetas finales"""

	# Se define el destino del archivo
	Destino = '/media/discoExternoRAID/raul/Python/Resultados/'+NombreArchivo

	# Se abre el archivo a escribit
	archivoXML = open( Destino, 'a')

	# Fin del Document
	archivoXML.write('</Document>'+'\n')

	# Etiqueta cierre
	archivoXML.write('</kml>'+'\n')

	#Cierre del archivo
	archivoXML.close()






###########################################################################

def diccionario_4_Niveles( listadoTuplas = [(-33.4, -70.6), (-33.4, -70.5)] , Diccionario = { 'Nivel01' : {'Nivel02' : {'Nivel03': [  ( date(2012, 11, 9), timedelta(0, 72757), Decimal('-33.45') , Decimal('-70.57') , 1000000, 571.661) , ( date(2012, 11, 9), timedelta(0, 73040), Decimal('-33.4'), Decimal('-70.5'), 571, 571) ] }  } } , NombreArchivo = 'borrable' , NombreDocumento = 'Default') :
	"""Esta funcion esta orientada para armar el XML correspondiente al algoritmo optics"""

	# Importa una libreria para el tratamiento de las etiquetas
	import EnsambleXML

	# El diccionario filtrado
	Diccionario_02 = {}

	# Diccionario con centroides
	Diccionario_centros = {}

	# En el siguiente recorrido se sacan los registros vacioas
	# Se parte recorriendo los dias del diccionario
	for Dias , valoresDias in iter( sorted(Diccionario.iteritems() ) ):

		# Se recorren los bloques
		for bloques , valoresBloques in iter( sorted( valoresDias.iteritems() ) ):

			# Se recorren los cluster que son parte del bloque horario
			for clusters, valoresClusters in iter( sorted( valoresBloques.iteritems() ) ):


				# Creacion de las llaves en la medida en que existan
				if (not Diccionario_02.has_key(Dias)): Diccionario_02[Dias] = {}
				if (not Diccionario_02[Dias].has_key(bloques)): Diccionario_02[Dias][bloques] = {}
				if (not Diccionario_02[Dias][bloques].has_key(clusters)): Diccionario_02[Dias][bloques][clusters] = []
				Diccionario_02[Dias][bloques][clusters] = Diccionario[Dias][bloques][clusters]


				if (not clusters == 'ruido'):
					if (not Diccionario_centros.has_key(Dias)): Diccionario_centros[Dias] = {}
					if (not Diccionario_centros[Dias].has_key(bloques)): Diccionario_centros[Dias][bloques] = {}
					if (not Diccionario_centros[Dias][bloques].has_key(clusters)): Diccionario_centros[Dias][bloques][clusters] = []
					Diccionario_centros[Dias][bloques][clusters] = Diccionario[Dias][bloques][clusters]






	# Creacion del archivo con los centroides
	# Creacion de las etiquetas de documento
	docuMento = EnsambleXML.EnsXML( 'Document' , NombreDocumento+'_Centroides' )

	# Este es el contador que va haciendo cambiar el color de los pinches
	i = 0

	# Se parte recorriendo los dias del diccionario
	for Dias , valoresDias in iter( sorted(Diccionario_centros.iteritems() ) ):

		# Se crea una carpeta correspondiente al dia, en la que se van agregando al final los bloques horarios
		CarpetaDia = EnsambleXML.EnsXML( 'Folder' , Dias ) 

		# Se recorren los bloques
		for bloques , valoresBloques in iter( sorted( valoresDias.iteritems() ) ):

			# Se crea un carpeta por los bloques horarios
			CarpetaBloques = EnsambleXML.EnsXML( 'Folder' , bloques )

			# Se recorren los cluster que son parte del bloque horario
			for clusters, valoresClusters in iter( sorted( valoresBloques.iteritems() ) ):

				# Se crea una carpeta para cada cluster
				#CarpetaCluster = EnsambleXML.EnsXML( 'Folder' , clusters )


				# El cambio de color es por cluster
				color = i%9

				# Se cambia el color
				i+=1

				# Se agrega el centroide, que es el ultimo elemento de la lista
				longitud = valoresClusters[-1][1]
				latitud = valoresClusters[-1][0]
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

	# Se define el destino del archivo
	Destino = '/media/discoExternoRAID/raul/Python/Resultados/CentroMasas_'+NombreArchivo

	# Se abre el archivo a escribit
	archivoXML = open( Destino, 'w')

	# Fin del Document
	archivoXML.write( ElScript )

	archivoXML.close()







	# Creacion del archivo con el detalle
	# Creacion de las etiquetas de documento
	docuMento = EnsambleXML.EnsXML( 'Document' , NombreDocumento+'_Detalle' )

	# Este es el contador que va haciendo cambiar el color de los pinches
	i = 0

	# Se parte recorriendo los dias del diccionario
	for Dias , valoresDias in iter( sorted(Diccionario_02.iteritems() ) ):

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
						longitud = tupla[3]
						latitud = tupla[2]
						coord = [(longitud,latitud)]
						Placemark =  EnsambleXML.EnsXML( 'Placemark' , str(tupla[1]) , coord , color )

						CarpetaCluster.agregar(Placemark.cuerpo)

				# Si el cluster NO es de ruido
				else:

					# Se recorre todo menos el ultimo elemento que es el centroide
					for tupla in valoresClusters[:-1]:
						longitud = tupla[3]
						latitud = tupla[2]
						coord = [(longitud,latitud)]
						Placemark = EnsambleXML.EnsXML( 'Placemark' , str(tupla[1]) , coord , color )

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
	Destino = '/media/discoExternoRAID/raul/Python/Resultados/Detalle_'+NombreArchivo

	# Se abre el archivo a escribit
	archivoXML = open( Destino, 'w')

	# Fin del Document
	archivoXML.write( ElScript )

	archivoXML.close()










	# Creacion del archivo con el detalle
	# Creacion de las etiquetas de documento
	docuMento = EnsambleXML.EnsXML( 'Document' , NombreDocumento+'_Centroides_De_Centroides' )

	# Este es el contador que va haciendo cambiar el color de los pinches
	i = 0

	CarpetaCluster = EnsambleXML.EnsXML( 'Folder' , 'Centros de Centros' )

	# Se parte recorriendo los dias del 
	for tupla in listadoTuplas:

		color = i%9
		longitud = tupla[1]
		latitud = tupla[0]
		coord = [(longitud,latitud)]
		Placemark =  EnsambleXML.EnsXML( 'Placemark' , 'CentroideDeCentroide' , coord , color )

		CarpetaCluster.agregar(Placemark.cuerpo)

		# Se cambia el color
		i+=1

	# El dia revisado se agrega al documento
	docuMento.agregar(CarpetaCluster.cuerpo)


	# El docuMento crea un consolidado de si mismo que se encuentra en el atributo "docuMento.consolidado"
	docuMento.consolidar( docuMento.cuerpo )
	ElScript = docuMento.consolidado

	# Se define el destino del archivo
	Destino = '/media/discoExternoRAID/raul/Python/Resultados/CentrosDeCentros_'+NombreArchivo

	# Se abre el archivo a escribit
	archivoXML = open( Destino, 'w')

	# Fin del Document
	archivoXML.write( ElScript )

	archivoXML.close()




##################################################################################################################################################
def ruta_diccionario_3_Niveles( Diccionario = { 'Nivel01' : {'Nivel02' : [ ['nombreUbicacion', ( timedelta(0, 1) , Decimal('-33.45') , Decimal('-70.68') ) ] ]} } , NombreArchivo = 'borrable' , NombreDocumento = 'Default'):
	"""En la tupla de ceros, el primero es """

	# Importa una libreria para el tratamiento de las etiquetas
	import EnsambleXML

	# Variable dando se guardan las instancias de carpetas
	Carpeta = {}
	Rutas = {}
	listadoTuplas = []
	Estilo = {}
	ultimaTupla = ( 0 , 0 )
	ultimoDia = ''

	# Variable de recorrido auxiliar.
	i=0		

	# Creacion de las etiquetas de documento
	docuMento = EnsambleXML.EnsXML( 'Document' , NombreDocumento )

	# Comienza a recorrerse los distintos niveles del diccionario, partiendo por el nivel 1 de manera ordenada.
	for llaveNivel01 , valorNivel01 in iter( sorted(Diccionario.iteritems() ) ):

		# Tira las llaves ordenadas y luego los valores
		Carpeta[llaveNivel01] = EnsambleXML.EnsXML( 'Folder' , llaveNivel01 )	

		# Recorrido del segundo nivel
		for llaveNivel02 , valorNivel02 in iter(sorted( valorNivel01.iteritems() )):


			# Recorrido de las listas, los valores ya estan ordenados. Por mejorar esta que se ordene la lista segun la hora
			listadoTuplas = []
			
		 ## ESTA LINEA ES LA CLAVE PARA CREAR LA UNION ENTRE LAS RUTAS ##
			if not ultimaTupla == (0,0) and (ultimoDia == llaveNivel01):
				listadoTuplas.append( ultimaTupla )
			ultimoDia = llaveNivel01
			for valorNivel03 in valorNivel02:
				Long = valorNivel03[1][2]
				Lat = valorNivel03[1][1]
				listadoTuplas.append( ( Long , Lat ) )
				# CON ESTA LINEA SE CREA UN CONEXION ENTRE EL ULTIMO PUNTO DE LA RUTA Y EL PRIMER PUNTO DE LA SIGUIENTE RUTA.
				ultimaTupla = ( Long , Lat )


			# Es un numero que va del 0 al 7
			i+=1
			if not Estilo.has_key(llaveNivel02): Estilo[llaveNivel02] = i%8
			
			# Se crea la instancia
			Rutas[llaveNivel02] =  EnsambleXML.EnsXML( 'Route' , llaveNivel02 , listadoTuplas , Estilo[llaveNivel02] )

			
			# Las rutas que se van creando se van agregando altiro a la carpeta correspondiente
			Carpeta[llaveNivel01].agregar( Rutas[llaveNivel02].cuerpo )


		# Las carpetas que se van creando se van agregando a docuMento
		docuMento.agregar( Carpeta[llaveNivel01].cuerpo )	


	# El docuMento crea un consolidado de si mismo que se encuentra en el atributo "docuMento.consolidado"
	docuMento.consolidar( docuMento.cuerpo )
	ElScript = docuMento.consolidado

	# Se define el destino del archivo
	Destino = '/media/discoExternoRAID/raul/Python/Resultados/'+NombreArchivo

	# Se abre el archivo a escribit
	archivoXML = open( Destino, 'w')

	# Fin del Document
	archivoXML.write( ElScript )

	archivoXML.close()





###########################################################################

def puntos_diccionario_1_Niveles( listado, NombreArchivoXML , nombreSecundario = 'Puntos mas vistos'):
	"""Se dibujan las 10 ubicaciones mas visitadas"""

	# Importa una libreria para el tratamiento de las etiquetas
	import EnsambleXML
	from decimal import Decimal

	# Creacion de las etiquetas de documento
	docuMento = EnsambleXML.EnsXML( 'Document' , nombreSecundario )
	Puntos = {}

	# tupla
	tupla = [(0,0)]

	# Recorrido de la lista
	for fila in listado:
		frec = str(fila[2])
		longitud = Decimal( fila[1][15:26] )
		latitud = Decimal( fila[1][0:11] )
		tupla = [(longitud,latitud)]
		Puntos[frec] =  EnsambleXML.EnsXML( 'Placemark' , frec , tupla , 1 )
		docuMento.agregar(Puntos[frec].cuerpo)



	docuMento.consolidar(docuMento.cuerpo)
	ElScript = docuMento.consolidado


	# El docuMento crea un consolidado de si mismo que se encuentra en el atributo "docuMento.consolidado"
	docuMento.consolidar( docuMento.cuerpo )
	ElScript = docuMento.consolidado

	# Se define el destino del archivo
	Destino = '/media/discoExternoRAID/raul/Python/Resultados/'+NombreArchivoXML

	# Se abre el archivo a escribit
	archivoXML = open( Destino, 'w')

	# Fin del Document
	archivoXML.write( ElScript )

	archivoXML.close()






###########################################################################

def ruta_diccionario_3_Niveles_Pinches(    Diccionario = { 'Nivel01' : {'Nivel02' : [ ['nombreUbicacion', ( timedelta(0, 1) , Decimal('-33.45') , Decimal('-70.68') ) ] ]} } ,     NombreArchivo = 'borrable' , NombreDocumento = 'Default'):
	"""En la tupla de ceros, el primero es """

	# Importa una libreria para el tratamiento de las etiquetas
	import EnsambleXML

	# Variable dando se guardan las instancias de carpetas
	Carpeta = {}
	Puntos = {}
	listadoTuplas = []
	Estilo = {}
	ultimaTupla = ( 0 , 0 )
	ultimoDia = ''

	# Variable de recorrido auxiliar.
	i=0		

	# Creacion de las etiquetas de documento
	docuMento = EnsambleXML.EnsXML( 'Document' , NombreDocumento )

	# Comienza a recorrerse los distintos niveles del diccionario, partiendo por el nivel 1 de manera ordenada.
	for llaveNivel01 , valorNivel01 in iter( sorted(Diccionario.iteritems() ) ):

		# Tira las llaves ordenadas y luego los valores
		Carpeta[llaveNivel01] = EnsambleXML.EnsXML( 'Folder' , llaveNivel01 )	

		# Recorrido del segundo nivel
		for llaveNivel02 , valorNivel02 in iter(sorted( valorNivel01.iteritems() )):

			# Es un numero que va del 0 al 7
			i+=1
			if not Estilo.has_key(llaveNivel02): Estilo[llaveNivel02] = i%8
			# Se crea la instancia
			if not valorNivel02 == []: 
				Puntos[llaveNivel02] =  EnsambleXML.EnsXML( 'Placemark' , llaveNivel02 , valorNivel02 , Estilo[llaveNivel02] )
				# Los puntos que se van creando se van agregando altiro a la carpeta correspondiente
				Carpeta[llaveNivel01].agregar( Puntos[llaveNivel02].cuerpo )

		# Las carpetas que se van creando se van agregando a docuMento
		docuMento.agregar( Carpeta[llaveNivel01].cuerpo )	


	# El docuMento crea un consolidado de si mismo que se encuentra en el atributo "docuMento.consolidado"
	docuMento.consolidar( docuMento.cuerpo )
	ElScript = docuMento.consolidado

	# Se define el destino del archivo
	Destino = '/media/discoExternoRAID/raul/Python/Resultados/'+NombreArchivo

	# Se abre el archivo a escribit
	archivoXML = open( Destino, 'w')

	# Fin del Document
	archivoXML.write( ElScript )

	archivoXML.close()



###########################################################################

