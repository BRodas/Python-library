class EnsXML:

#########################################################################################################################################################
	def __init__(self , tipo='Placemark' , nombre='defecto' , Pocisiones = [( -70.65 , -33.43 )] , numEstilo=0):
		"""Clase orientada a la generacion de XML. Los parametros para definir la instancia son los siguientes:

			tipo='Placemark' , Se elige un tipo de los siguientes: 
				
				Document
				Folder
				Placemark
				Route

			nombre='defecto' , Nombre de la etiqueta que se esta agregando.

			Pocisiones = [( -70.65 , -33.43 )] , Corresponde a un listado de tuplas. El PRIMER valor de la tupla es la LONGITUD, el SEGUNDO valor de la tupla es la LATITUD . Si es un pinche basta con una lista con solo una tupla, esto es asi ya que para las rutas basta con escribir un listado con varias tuplas.

			numEstilo=0, Para los pinches los estilos pueden variar del numero 0 al numero 9, mientras que para las rutas el color de la linea puede ir del numero 0 al 7.
"""

		# Ingreso de las variables dentro de "self"
		self.tipo = tipo
		self.nombre = nombre
		
		# Si la etiqueta es de tipo documento
		if self.tipo =='Document' or self.tipo == 'document':

			# Se crea el diccionario correspondiente
			self.cuerpo = {'ini':str(),'fin':str()}


			codigoEstilo = """

	<!-- Este es el codigo que define el estilo de los pinches-->

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
	</Style>


<!--Aqui comienza la definicion de los colores para las lineas-->



	<StyleMap id="msn_ylw-pushpin">
		<Pair>
			<key>normal</key>
			<styleUrl>#sn_ylw-pushpin2</styleUrl>
		</Pair>
		<Pair>
			<key>highlight</key>
			<styleUrl>#sh_ylw-pushpin4</styleUrl>
		</Pair>
	</StyleMap>


	<StyleMap id="msn_ylw-pushpin0">
		<Pair>
			<key>normal</key>
			<styleUrl>#sn_ylw-pushpin</styleUrl>
		</Pair>
		<Pair>
			<key>highlight</key>
			<styleUrl>#sh_ylw-pushpin1</styleUrl>
		</Pair>
	</StyleMap>


	<Style id="sh_ylw-pushpin">
		<IconStyle>
			<scale>1.3</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
		<LineStyle>
			<color>ffff00ff</color>
			<width>2</width>
		</LineStyle>
	</Style>
	<Style id="sh_ylw-pushpin0">
		<IconStyle>
			<scale>1.3</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
		<LineStyle>
			<color>ffffaa55</color>
			<width>2</width>
		</LineStyle>
	</Style>
	<Style id="sn_ylw-pushpin">
		<IconStyle>
			<scale>1.1</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
		<LineStyle>
			<color>ff000055</color>
			<width>2</width>
		</LineStyle>
	</Style>
	<Style id="sh_ylw-pushpin1">
		<IconStyle>
			<scale>1.3</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
		<LineStyle>
			<color>ff000055</color>
			<width>2</width>
		</LineStyle>
	</Style>


	<StyleMap id="msn_ylw-pushpin1">
		<Pair>
			<key>normal</key>
			<styleUrl>#sn_ylw-pushpin1</styleUrl>
		</Pair>
		<Pair>
			<key>highlight</key>
			<styleUrl>#sh_ylw-pushpin6</styleUrl>
		</Pair>
	</StyleMap>


	<StyleMap id="msn_ylw-pushpin2">
		<Pair>
			<key>normal</key>
			<styleUrl>#sn_ylw-pushpin5</styleUrl>
		</Pair>
		<Pair>
			<key>highlight</key>
			<styleUrl>#sh_ylw-pushpin5</styleUrl>
		</Pair>
	</StyleMap>


	<Style id="sn_ylw-pushpin0">
		<IconStyle>
			<scale>1.1</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
		<LineStyle>
			<color>ff000000</color>
			<width>2</width>
		</LineStyle>
	</Style>
	<Style id="sh_ylw-pushpin2">
		<IconStyle>
			<scale>1.3</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
		<LineStyle>
			<color>ffff0000</color>
			<width>2</width>
		</LineStyle>
	</Style>
	<Style id="sh_ylw-pushpin3">
		<IconStyle>
			<scale>1.3</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
		<LineStyle>
			<color>ff000000</color>
			<width>2</width>
		</LineStyle>
	</Style>
	<Style id="sn_ylw-pushpin1">
		<IconStyle>
			<scale>1.1</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
		<LineStyle>
			<color>ffff0055</color>
			<width>2</width>
		</LineStyle>
	</Style>


	<StyleMap id="msn_ylw-pushpin3">
		<Pair>
			<key>normal</key>
			<styleUrl>#sn_ylw-pushpin4</styleUrl>
		</Pair>
		<Pair>
			<key>highlight</key>
			<styleUrl>#sh_ylw-pushpin0</styleUrl>
		</Pair>
	</StyleMap>


	<StyleMap id="msn_ylw-pushpin4">
		<Pair>
			<key>normal</key>
			<styleUrl>#sn_ylw-pushpin6</styleUrl>
		</Pair>
		<Pair>
			<key>highlight</key>
			<styleUrl>#sh_ylw-pushpin</styleUrl>
		</Pair>
	</StyleMap>


	<StyleMap id="msn_ylw-pushpin5">
		<Pair>
			<key>normal</key>
			<styleUrl>#sn_ylw-pushpin0</styleUrl>
		</Pair>
		<Pair>
			<key>highlight</key>
			<styleUrl>#sh_ylw-pushpin3</styleUrl>
		</Pair>
	</StyleMap>


	<Style id="sh_ylw-pushpin4">
		<IconStyle>
			<scale>1.3</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
		<LineStyle>
			<color>ff00ff55</color>
			<width>2</width>
		</LineStyle>
	</Style>
	<Style id="sn_ylw-pushpin2">
		<IconStyle>
			<scale>1.1</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
		<LineStyle>
			<color>ff00ff55</color>
			<width>2</width>
		</LineStyle>
	</Style>


	<StyleMap id="msn_ylw-pushpin6">
		<Pair>
			<key>normal</key>
			<styleUrl>#sn_ylw-pushpin3</styleUrl>
		</Pair>
		<Pair>
			<key>highlight</key>
			<styleUrl>#sh_ylw-pushpin2</styleUrl>
		</Pair>
	</StyleMap>


	<Style id="sn_ylw-pushpin3">
		<IconStyle>
			<scale>1.1</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
		<LineStyle>
			<color>ffff0000</color>
			<width>2</width>
		</LineStyle>
	</Style>
	<Style id="sh_ylw-pushpin5">
		<IconStyle>
			<scale>1.3</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
		<LineStyle>
			<color>ff0000ff</color>
			<width>2</width>
		</LineStyle>
	</Style>
	<Style id="sn_ylw-pushpin4">
		<IconStyle>
			<scale>1.1</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
		<LineStyle>
			<color>ffffaa55</color>
			<width>2</width>
		</LineStyle>
	</Style>
	<Style id="sh_ylw-pushpin6">
		<IconStyle>
			<scale>1.3</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
		<LineStyle>
			<color>ffff0055</color>
			<width>2</width>
		</LineStyle>
	</Style>
	<Style id="sn_ylw-pushpin5">
		<IconStyle>
			<scale>1.1</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
		<LineStyle>
			<color>ff0000ff</color>
			<width>2</width>
		</LineStyle>
	</Style>
	<Style id="sn_ylw-pushpin6">
		<IconStyle>
			<scale>1.1</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
		<LineStyle>
			<color>ffff00ff</color>
			<width>2</width>
		</LineStyle>
	</Style>



"""


			# Definicion del cuerpo, pero la primera parte, con el encabezado correspondiente y sin cerrar
			self.cuerpo['ini'] = '<?xml version="1.0" encoding="UTF-8"?>'+'\n'+'<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">' + '<Document>' + '<name>'+self.nombre+'</name>' + codigoEstilo

			# Aqui se cierra el documento
			self.cuerpo['fin'] = '\t'+'</Document>'+'\n'+'</kml>'

			
		# Aqui se define una carpeta
		elif self.tipo =='Folder' or self.tipo =='folder':

			# Se crea el diccionario
			self.cuerpo = {'ini':str(),'fin':str()}
	
			# Apertura y cierre de la carpeta (la idea es la misma para todos)
			self.cuerpo['ini']='<Folder><name>'+ self.nombre + '</name>'
			self.cuerpo['fin']='</Folder>'






		# Aqui se define las lineas
		elif self.tipo == 'Route' or self.tipo == 'route' or self.tipo == 'Routes' or self.tipo == 'routes' or self.tipo == 'ruta' or self.tipo == 'Ruta' or self.tipo == 'Rutas' or self.tipo == 'rutas':
			
			# Se crea el diccionario
			self.cuerpo = {'ini':str(),'fin':str()}

			# Lista con los colores de las lineas
			colores = [ "msn_ylw-pushpin" , "msn_ylw-pushpin0" , "msn_ylw-pushpin1" , "msn_ylw-pushpin2" , "msn_ylw-pushpin3" , "msn_ylw-pushpin4" , "msn_ylw-pushpin5" , "msn_ylw-pushpin6" ]
			self.estilo = colores[numEstilo]


			# Agregacion de las coordenadas
			ruta = str('')
			for tuplas in Pocisiones:
				longitu = tuplas[0]
				latitu = tuplas[1]
				ruta = ruta + str(longitu) +','+ str(latitu) + ',0' + ' '

			# Apertura de la ruta
			self.cuerpo['ini'] = '<Placemark>'+'\n'+'\t'+'<name>'+ self.nombre +'</name>'+'<styleUrl>#' + self.estilo + '</styleUrl>' + '<LineString> 	<tessellate> 1 </tessellate> <coordinates>' + ruta

			# Cierre de la ruta
			self.cuerpo['fin'] = ' </coordinates> </LineString> </Placemark>'






		# Aqui se crea un Placemark pero correspondiente a los pinches
		elif self.tipo == 'Placemark' or self.tipo == 'placemark' :

			# Definicion de los estilos de los pinches.
			estilos =["sh_purple-pushpin","sn_pink-pushpin","sn_grn-pushpin","sn_ltblu-pushpin","sn_purple-pushpin","sn_blue-pushpin","sh_pink-pushpin","sh_grn-pushpin","sh_ltblu-pushpin"]
			self.estilo = estilos[numEstilo]


			# El PRIMER valor de la tupla es la LONGITUD, el SEGUNDO es la LATITUD
			self.coordenadas = Pocisiones[0]
			self.latitud = self.coordenadas[1]
			self.longitud = self.coordenadas[0]

			# Creacion del diccionario y luego llenado
			self.cuerpo = {'ini':'' , 'fin':'' }

			self.cuerpo['ini']= '<Placemark><name>' + self.nombre + '</name><visibility>0</visibility>'+'<LookAt><longitude>'+str(self.longitud) +'</longitude><latitude>' + str(self.latitud) +'</latitude>'+'<range>1000</range></LookAt>'+'<styleUrl>#'+self.estilo+'</styleUrl>'+ '<Point>' +'<coordinates>' + str(self.longitud) + ',' + str(self.latitud) + ',0'+ '</coordinates>' + '</Point>'

			self.cuerpo['fin'] = '</Placemark>'
				



		# Por si no se elige ninguna de las opciones correspondientes
		else:

			print("Parametros incorrectos")



#########################################################################################################################################################
	# Cone esta funcion se agrega uno de las etiquetas dentro de otra. Por ejemplo se da como atributo un "Folder", y este se mete dentro de "Document"	
	def agregar( self , Diccionario = {'ini':str(),'fin':str() } ):

		self.agregado = Diccionario

		self.cuerpo['ini'] = self.cuerpo['ini'] +'\n'+'\n'+ self.agregado['ini'] +'\n'+'\n' + self.agregado['fin']

		return self.cuerpo


#########################################################################################################################################################
	# Esta funcion consodila el diccionario en UN solo string 
	def consolidar( self , Diccionario={'ini':str(),'fin':str()}):
		self.consolidado = self.cuerpo['ini'] + self.cuerpo['fin']


