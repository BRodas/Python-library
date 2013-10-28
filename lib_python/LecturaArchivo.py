# LecturaArchivo ES UN LISTADO DE FUNCIONES UTILES EN LA LECTURA Y MANIPULACION DE ARCHIVOS


import random
import datetime



########################################################################################################################
# funcion que lee un archivo y pone cada LINEA DEL ARCHIVO en una 'lista' de python. Cada elemento de la 'lista' es a su vez otra 'lista' con las PALABRAS de cada linea del archivo original
def leer(ubicacion):
	# Abre el archivo
	f = open(ubicacion, 'r')
	# Lee 'la' linea
	linea = f.readline()
	# La guarda en la lista, posicion 0
	lineaS = [linea.split()]
	# Se lee el resto de las lineas
	while 1:
		linea=f.readline()
		if not linea: break
		lineaS.append(linea.split())
	f.close()	
	
	return lineaS





########################################################################################################################
# esta funcion saca un extracto de un archivo, saltandose la cantidad de lineas indicadas
def extracto(ubicacion_original, Saltos_De_Linea,ubicacion_destino):
	# Abre el archivo a leer
	f = open(ubicacion_original, 'r')
	# Abre el archivo a escribir
	e = open(ubicacion_destino, 'w')
	# Lee 'la' linea
	linea = f.readline()
	# Se lee el resto de las lineas
	j=1
	i=0
	while 1:
		linea=f.readline()
		if not linea: break

		if i == Saltos_De_Linea * j :
			e.write(linea)
			j=j+1
		i=i+1
	f.close()	
	e.close()
	return 




 
########################################################################################################################
# funcion que recive una lista talque cada elemento de la lista es una fila de una tabla. Esta tabla incluye encabezado
def DicionarioTabla(TablaConEncabezado):

	# Se transpone la TABLA
	Traspuesto = zip(*TablaConEncabezado)
	# Se declara el diccionario
	Diccionario = {}
	# Se crea el diccionario
	for columna in Traspuesto:
		Diccionario[columna[0]] = list(columna[1:])

	return Diccionario




########################################################################################################################
# Creacion de archivo, se crea un archivo con los datos de la lista entregada. Cada elemento de la lista es una fila
def escribir(lista,directorio):
	# Abre archivo
	f = open(directorio, 'w')
	limite = len(lista)	
	i=0
	while i<limite:
		f.write(lista[i])
		i=i+1

	f.close()

	return




########################################################################################################################
# Funcion que borra la primera fila de un archivo. (16-Ene-2012)
def BPLinea(UbicacionOrigen,UbicacionDestino):
	# Abre el archivo a leer
	f = open(UbicacionOrigen, 'r')
	# Abre el archivo a escribir
	e = open(UbicacionDestino, 'w')
	# Lee 'la primera' linea
	linea = f.readline()
	while 1:
		linea=f.readline()
		if not linea: break
		e.write(linea)
	f.close()	
	e.close()
	return




########################################################################################################################
# Funcion que extrae al azar el numero de lineas seleccionadas
def LineAzar(UbicacionOrigen,UbicacionDestino):
	# Se indica el numero de lineas que se desea
	NumLineas = raw_input("Ingresa el numero de lineas aleatorias: ")
	NumLineas = int(NumLineas)
	# Se cuenta el total de lineas en el archivo , que se considera la poblacion
	TotaLineas = ConteoLineas(UbicacionOrigen)
	TotaLineass = []	
	for x in range(TotaLineas-2):
		TotaLineass.append(x+2)
	#print (TotaLineass)
	# Se selecciona la muestra de lineas
	muestra = random.sample(TotaLineass, NumLineas)
	#print ( muestra )
	# Se ordena la muestra
	muestra.sort()
	#print ( muestra )
	# Se seleccionan las lineas elegidas al azar
	# Apertura de archivo a leer
	f = open(UbicacionOrigen, 'r')
	# Apertura archivo a escribir
	e = open(UbicacionDestino, 'w')
	# Indice del listado "muestra"
	i = 0
	# Indice de la linea que se esta leyendo
	conteo = 1
	while 1:
		# Se lee la linea 'k'
		linea=f.readline()
		# Si el numero de linea 'k' = Numero linea muestra
		if conteo == muestra[i]:
			# Entonces se escribe aquella linea			
			e.write(linea)
			# Si se han seleccionado ya todas las lineas muestra, se cierra el loop
			if i == NumLineas - 1: break
			# Se actualiza al siguiente termino de la lista de muestras
			i = i + 1
		conteo = conteo + 1
	f.close()	
	e.close()	
	return




########################################################################################################################
# Funcion que cuenta el numero de lineas del archivo
def ConteoLineas(UbicacionOrigen):
	TotalDeLineas = 0
	f = open(UbicacionOrigen, 'r')
	while 1:
		linea=f.readline()
		if not linea: break
		TotalDeLineas = TotalDeLineas + 1
		
	f.close()
	return TotalDeLineas



########################################################################################################################
def ListadoSelectivo(UbicacionOrigen,UbicacionDestino):
	return



########################################################################################################################
# Extraccion de una linea puntual
def LineaPuntual(UbicacionOrigen):
	LineaPuntual = raw_input("Que linea buscas? ")
	TotalDeLineas = 0
	ContTab = 0
	f = open(UbicacionOrigen, 'r')
	while 1:		
		linea=f.readline()
		TotalDeLineas = TotalDeLineas + 1

		if (TotalDeLineas == int(LineaPuntual)): 
			print('\n')			
			print(linea)
			print('\n')
			print(str.split(linea))
			print('\n')
			print('Numero de palabras en la fila '+str(len(str.split(linea))))
			print('\n')
			for NumCaracteresLista in range(len(list(linea))):
				if(list(linea)[NumCaracteresLista] == '\t'):ContTab=ContTab+1
			print('Numero de "tabs" en la fila '+str(ContTab))
			break

		if not linea: break
		
		
	f.close()
	return 




########################################################################################################################
# Contador de lineas incorrectas
def NumLinTabsExcecivos(UbicacionOrigen,UbicacionDestino):
	now=datetime.datetime.now()
	print(now)
	LimiteDeTabs = raw_input("Cual es el limite de Tabs? ")
	LimiteDeTabs = int(LimiteDeTabs)
	f = open(UbicacionOrigen, 'r')
	e = open(UbicacionDestino, 'w')

	ContLinExc = 0

	while 1:		
		linea=f.readline()
		ContTab =  0		
		for NumCaracteresLista in range(len(list(linea))):
			if(list(linea)[NumCaracteresLista] == '\t'):ContTab=ContTab+1
		if (ContTab >= (LimiteDeTabs+1)):
			ContLinExc=ContLinExc+1
			e.write(linea)	

		if not linea: break

	print('Numero de lineas con "tabs" excecivos son: '+str(ContLinExc))	

		
	
	f.close()
	e.close()
	now=datetime.datetime.now()
	print(now)
	return 



###################################################################################################################################################
###################################################################################################################################################

# Filtrador de filas segun exceso de tabs: crea un archivo nuevo en el que NO se incluyen las filas con exceso de Tabs.
def ExcesoTabs(UbicacionOrigen,UbicacionDestino):
	now=datetime.datetime.now()
	print(now)
	LimiteDeTabs = raw_input("Cual es el limite de Tabs? ")
	LimiteDeTabs = int(LimiteDeTabs)
	f = open(UbicacionOrigen, 'r')
	e = open(UbicacionDestino, 'w')

	ContLinExc = 0

	while 1:		
		linea=f.readline()
		ContTab =  0		
		for NumCaracteresLista in range(len(list(linea))):
			if(list(linea)[NumCaracteresLista] == '\t'):ContTab=ContTab+1

		ContLinExc=ContLinExc+1
		if not (ContTab >= (LimiteDeTabs+1)):
			ContLinExc=ContLinExc-1
			e.write(linea)	

		if not linea: break

	print('Numero de lineas con "tabs" excecivos son: '+str(ContLinExc)+'\n')
	print('Archivo destido: '+ str(UbicacionDestino))	

		
	
	f.close()
	e.close()
	now=datetime.datetime.now()
	print(now)
	return 




###################################################################################################################################################
###################################################################################################################################################

# Funcion pensada en lenguajes basados en etiquetas: XML, HTML, KML, etc.
# Cuenta el numero de lineas correspondientes a algun bloque.

#Definicion de la funcion
def EtiquetaAbreCierra(ArchivoOrigen):


        #Preparar archivo de origen
        f = open(ArchivoOrigen, 'r')
	#print(ArchivoOrigen)

        #Preguntar por la etiqueta de abertura: EtiquetaAbertura
        #Preguntar por la etiqueta de cierre:   EtiquetaCierre
	#Alguna etiqueta opcional
        EtiquetaAbertura = raw_input("Ingresa la etiqueta de abertura: ")
        EtiquetaCierre = raw_input("Ingresa la etiqueta de cierre: ")

	EtiquetaOpcional= raw_input("Alguna otra linea (Opcional): ")


        #Ir llevando el conteo de las lineas que se van leyendo, Declaracion Variable: NumLinea = 0
        NumLinea = 0

        #Puerta que busca la etiqueta de apertura, puertaUNO abierta, puertaUNO = 1
        puertaUNO = 1
        #Puerta que busca la etiqueta de cierre, puertaDOS cerrada, puertaDOS = 0
        puertaDOS = 0

	#Declaracion de la lista
	ListaNumLineas = []
	ListaNumLineas.append([])
	ListaNumLineas.append([])
	ListaNumLineas.append([])

	#print(ListaNumLineas)


	# Estampilla de tiempo correspondiente al de inicio
	now=datetime.datetime.now()
	print(now)

        #While: El que recorre linea por linea todo el archivo buscando la etiqueta de abertura
        while 1:
	
		#print("entro en el while")
                # Pasar a la siguiente linea,  NumLinea = NumLinea + 1
                NumLinea = NumLinea + 1
		#print(NumLinea)

                # Lectura de la linea en la variable "ContenidoLinea"
                ContenidoLinea = f.readline()
		#print(ContenidoLinea)

                # Separacion de la variable "ContenidoLinea" en un listado "ListadoLinea"
                LineaEnlistada = ContenidoLinea.split()
	
                # Contar desde la primera palabra de la linea, NumPalabraListado = 0
                NumPalabraLista = 0

                #While (PuertaUno Abierta AND NumPalabraListado <= Largo.ListadoLinea): Recorre "ListadoLinea" buscando la etiqueta de abertura
		#print(len(LineaEnlistada),NumPalabraLista)
                while (puertaUNO == 1 and NumPalabraLista <= len(LineaEnlistada)-1 ):

			#SI la "NumLinea-esima" linea contiene la etiqueta de abertura:
                        if LineaEnlistada[NumPalabraLista] == EtiquetaAbertura:
                                #agregar Variable NumLinea a la posicion
                                ListaNumLineas[0].append(NumLinea)
                                #Cerrar, puertaUno = 0
                                puertaUNO = 0
                                #Abre la puerta al while que busca la EtiquetaCierre, puertaDOS =1
                                puertaDOS = 1
                        # Pasar a la siguiente palabra, NumPalabraListado = NumPalabraListado + 1
                        NumPalabraLista = NumPalabraLista + 1





                # Contar desde la primera palabra de la linea, NumPalabraListado = 0            
                NumPalabraLista = 0
                #While (PuertaDOS abierta AND NumPalabraListado <= Largo.ListadoLinea), El que recorre buscando la etiqueta de cierre
                while ( puertaDOS == 1 and NumPalabraLista <= len(LineaEnlistada)-1 ) :
 

			#SI la k-esima linea contiene la etiqueta opcional:
                        if LineaEnlistada[NumPalabraLista] == EtiquetaOpcional:
                                # agregar el numero de linea a la posicion
                                ListaNumLineas[1].append(NumLinea)



                       #SI la k-esima linea contiene la etiqueta de cierre:
                        if LineaEnlistada[NumPalabraLista] == EtiquetaCierre:
                                # agregar el numero de linea a la posicion
                                ListaNumLineas[-1].append(NumLinea)

                                # Cerrar la puertaDOS del while, puertaDOS = 0
                                puertaDOS = 0
                                # Re abrir la puertaUNO, puertaUNO = 1
                                puertaUNO = 1
                        # Pasar a la siguiente palabra, NumPalabra = NumPalabra + 1
                        NumPalabraLista = NumPalabraLista + 1





                #Si se acaba el archivo: cerrar el loop "while"
                if not ContenidoLinea: break
        #Cerrar el archivo que se estaba leyendo
        f.close()
        #Retornar ListNumLineas
        #print(ListaNumLineas)

	#Estampilla de tiempo correspondiente al final
	now=datetime.datetime.now()
	print(now)

	print( 'Numero etiquetas de abertura: ' +str(len(ListaNumLineas[0]))+ '\n'+ 'Numero etiquetas de cierre: ' + str(len(ListaNumLineas[-1])) + '\n'+ 'Numero etiquetas opcionales: ' + str(len(ListaNumLineas[1]))  )
	


        return ListaNumLineas






########################################################################################################################
#Funcion de reemplazo especial. Esta funcion recive dos valores, ambos parte de un archivo kml. Por ejemplo sean tres lineas de un archivo kml: "<name>kml_1</name>" , "<th>CELLBTS</th>" y "<td>SALCEU04_2-1</td>" . Uno ingresa como PRIMER valor SOLO "<name>" y luego como SEGUNDO valor "<th>CELLBTS</th>", el programa reemplaza los contenido en las etiquetas "<name>" y "</name>", por lo contenido en las etiquetas "<td>" y "</td>".

def ReemplazoTipoUno(UbicacionOrigen,UbicacionDestino):

	#Declaracion de variables
	IndiceApertura = 0	#Indice de la etiqueta de apertura 
	IndiceCierre = 0	#Indice de la etiqueta de cierre
	IndiceReemplazador = 0	#Indice de la etiqueta a reemplazar
	IndiceOrdenada = 0	#Indice de la lista ordenada

	#Declaracion lista ordenada
	ListaOrdenada = []
	ListaOrdenada.append([])
	ListaOrdenada[0].append(0)
	ListaOrdenada.append([])
	ListaOrdenada[1].append(0)

	#Estampilla de tiempo correspondiente al principio
	now=datetime.datetime.now()
	print(now)


	#Listado con numero de ubicacion claves 
	NumerosLineasClaves = EtiquetaAbreCierra(UbicacionOrigen)
	

	#While que ordena el listado. El primero recorre toda la lista del patron que reemplazara
	while IndiceReemplazador <= len(NumerosLineasClaves[1])-1 and IndiceApertura <= len(NumerosLineasClaves[0])-1 :
		
		#Este segundo while va recorriendo la lista de la etiqueta de apertura
		#while IndiceApertura <= len(NumerosLineasClaves[0])-1 :
			
		#print(IndiceApertura , IndiceReemplazador , len(NumerosLineasClaves[0]) , len(NumerosLineasClaves[1]))
		if (NumerosLineasClaves[0][IndiceApertura] <= NumerosLineasClaves[1][IndiceReemplazador]):

			ListaOrdenada[0][IndiceOrdenada] = NumerosLineasClaves[0][IndiceApertura]
			ListaOrdenada[1][IndiceOrdenada] = NumerosLineasClaves[1][IndiceReemplazador]
			
			
			IndiceApertura +=  1
			
		else:
			IndiceReemplazador += 1
			IndiceOrdenada += 1

			ListaOrdenada[0].append(0)
			ListaOrdenada[1].append(0)


	#Se abre el archivo
	f = open(UbicacionOrigen, 'r')
	e = open(UbicacionDestino, 'w')			

	
	#Declaracion de variables
	ContenidoLineaOriginal = ""
	indice = 0
	NumLinea = 0
	BuferLineas = []

	#Este while es el que recorre el archivo reemplazando	
	while 1:

		# Lectura de la linea en la variable "ContenidoLinea"
		ContenidoLineaOriginal = f.readline()
		NumLinea += 1
		#print(ContenidoLineaOriginal)
		#print(NumLinea)

		# Si el numero de linea corresponde al numero de la etiqueta "inicial" comienza a guardar en Buffer
		if NumLinea == ListaOrdenada[0][indice]:
			
			#Guarda la primera linea de Bufer
			BuferLineas.append(ContenidoLineaOriginal)

			#print(NumLinea,ListaOrdenada[1][indice])
			#Mientras el numero de linea sea menor al numero de linea limite guardar en el bufer
			while NumLinea <= ListaOrdenada[1][indice]:

				#Guarda la linea en la variable ContenidoLineaOriginal 
				ContenidoLineaOriginal = f.readline()
				NumLinea += 1
				# Guarda la linea en el Bufer
				BuferLineas.append(ContenidoLineaOriginal)
			
			
			# EXTRACCION, ARMADO Y REEMPLAZO DE LO QUE SE BUSCA 
			BuferLineas[1]="<name>"+BuferLineas[-1][4:-6]+"</name>"+'\n'
			
			# Recorrido linea por linea del Bufer
			for current in range(len(BuferLineas)):
				# Escritura de cada linea del Bufer en el archivo
				e.write(BuferLineas[current])

			# Vaciado del Bufer. IMPORTANTE: si no estuviera esta linea se crearia un archivo sin fin. Se crearia de manera constante un archivo. 
			del BuferLineas[:]
			BuferLineas[:] = []

			# Se pasa al siguiente "hito"
			indice += 1
			#print("indice "+str(indice))

		# Si no corresponde el if, se escribe la linea de manera directa.
		else:
			e.write(ContenidoLineaOriginal)


		#Se termina si no hay mas lineas, o se revisaron todos los indices
		if not ContenidoLineaOriginal: break
		

	#Cerrar el archivo que se estaba leyendo
        f.close()
	e.close()

	#Estampilla de tiempo correspondiente al final
	now=datetime.datetime.now()
	print(now)
	return
