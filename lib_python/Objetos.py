####################################################################################################
# DECLARACION DE LIBRERIAS
####################################################################################################
# Se importa la libreria que permite tratamiento de fechas
from datetime import date,timedelta,datetime

# Se importa la libreria que el uso de decimales
from decimal import *



####################################################################################################
# DEFINICION DE CLASES
####################################################################################################
class Objeto:
	"""Esta es una clase cuasi abstracta. Sus metodos son:
			asignarNombr(self, nombrViejo="",nombrNuevo="")
			asignarFormat(self, encabezado="" , formato="")
		Sus atributos son variables.

		Modus Operandi:
		1)Se crea UN objeto, al entregarse un listado de tuplas con valores
			Objeto(( valor1 , valor2 , valor3, .... ))
		2)Se asignan nombres nuevos en reemplazo de los antiguos
		3)Se le asigna formato a cada uno de los elementos de la tupla. Por defecto son String"""
	

	def __init__(self, tupla=() ):
		# Se recorre la tupla elemento por elemento
		for indElem in range(len(tupla)):
			# Se anade el atributo a self, que es parte de la clase
			setattr(self,'atr'+str(indElem),tupla[indElem])



	def asignarNombr(self, nombrViejo="",nombrNuevo=""):
		"""Esta funcion renombra el nombre para conseguir el atributo"""
		# Se crea un nuevo atributo con el nuevo nombre
		# nombrNuevo es un STRING. getattr( self , nombrViejo) consigue el valor de la instancia self.nombrViejo
		setattr(self , nombrNuevo , getattr( self , nombrViejo) )
		# Se borra el nombre viejo
		delattr(self, nombrViejo )



	def asignarFormat(self, encabezado="" , formato=""):
		"""Esta funcion realiza un cambio en el formato, de STRING al formato indicado (fecha,hora,string, o decimal)"""
		# Para cambiar a String
		if formato=='cadena' or formato=='string':setattr(self, encabezado, str(getattr(self,encabezado)))
		# Para cambiar a float
		elif formato=='float' :
			try:
				if getattr(self,encabezado) != 'NULL':
					valorFloat = float(getattr(self,encabezado))
					setattr(self, encabezado, valorFloat)
			except ValueError:
				pass

		# Para cambiar a decimal
		elif formato=='decimal' :
			valorDecimal = Decimal(getattr(self,encabezado))
			setattr(self, encabezado, valorDecimal)
		# Para cambiar a entero
		elif formato=='entero' or formato=='int':
			if (getattr(self,encabezado)==None or getattr(self,encabezado)=='NULL' ):
				setattr(self, encabezado, 'NULL')
			else:
				setattr(self, encabezado, int(getattr(self,encabezado)))
		# Para cambiar a fecha
		elif formato=='fecha':
			# Se asigna el ano en entero
			ano=int(getattr(self,encabezado)[0:4])
			# Se asigna el mes en entero
			mes=int(getattr(self,encabezado)[5:7])
			#Se asigna el dia en entero
			dia=int(getattr(self,encabezado)[8:10])
			setattr(self, encabezado, date( ano , mes , dia ) )
		# Para cambiar a hora
		elif formato=='hora':
			# Se asignan los segundos en entero
			segundos =int(getattr(self,encabezado)[6:8])
			# Se asignan los minutos en entero
			minutos =int(getattr(self,encabezado)[3:5])
			# Se asignan las horas en entero
			horas =int(getattr(self,encabezado)[0:2])
			setattr(self, encabezado, timedelta( seconds=segundos , minutes=minutos , hours=horas))




####################################################################################################################################################
class ListadoObjetos:
	"""A esta clase se le entrega UN string, que es una tabla separada por tabs. Sus metodos son:
			DarEncabezados(self,*encabezados)
			DarFormatos(self,**formatos)
			ListarValores(self)
		Sus atributos son:
			listaInstancias
			encabezados
			formatos
			listaValores"""



	def __init__(self , cadena = "", num_columnas = 0):

		# Se lleva el string de respuesta a un listados de consulta.
		cadena = cadena.split()
		# tupla
		tupla = ()
		#lista dinamica
		listaDinamica = []
		# el listado respuesta
		self.listaInstancias = []

		# Recorrido de la lista
		recorrido = range(num_columnas,len(cadena))
		for i in recorrido:
			# Si se lleva a la ultima linea se rompe el for	
			if i==recorrido[-1]:break
			# Se crean las filas
			listaDinamica.append(cadena[i])
			# Si se completa en una listaDinamica una fila, esta se transforma en tupla y se mete en el listado oficials
			if (i%num_columnas==num_columnas-1):
				tupla = tuple(listaDinamica)
				self.listaInstancias.append( Objeto(tupla) )
				listaDinamica = []

	def DarEncabezados(self,*encabezados):
		self.encabezados = encabezados
		# Se recorre cada instancia
		for instancia in self.listaInstancias:
			# Se recorre cada elemento al cual se le quiere dar un nombre
			for indElem in range(len(encabezados)):
				# Se reproduce el nombre viejo
				nombrViejo = 'atr'+str(indElem)
				# Se reproduce el nombre nuevo
				nombrNuevo = encabezados[indElem]
				# Se entregan al metodo de la instancia generada de la clase Objeto
				instancia.asignarNombr(nombrViejo,nombrNuevo)

	def DarFormatos(self,**formatos):
		"""En esta funcion se entrega una listado de la siguiente manera:"""
		""" nombreColumna = 'tipoFormato'. Los tipos de formatos son: cadena/string, decimal,entero,fecha,hora."""
		self.formatos=formatos
		# Se aceptan los siguientes formatos: cadena/string, decimal,entero,fecha,hora.
		for instancia in self.listaInstancias:
			# Luego se recorre el diccionario formato dando los nombres
			for encabezado , formato in formatos.iteritems():
				# A cada instancia se le da un formato
				instancia.asignarFormat( encabezado , formato )

	def ListarValores(self):
		"""Esta funcion crea un listado pero con los valores reales de las instancias"""
		self.listaValores = []
		#Se recorren las instancias de la lista
		for instancia in self.listaInstancias:
			# Se crea lo que SERA una tupla que se agregara
			tupla = []
			# Se recorre nombre por nombre la instancia
			for nombre in self.encabezados:
				# Se van agregando a lo que SERA una tupla
				tupla.append( getattr( instancia, nombre) )
			# Terminada la tupla la lista de transforma en tupla
			tupla = tuple(tupla)
			# Y se agrega al atributo correspondiente
			self.listaValores.append(tupla)

