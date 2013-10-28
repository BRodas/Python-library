"""Este codigo tiene como objetivo modificar los numeros de
telefono para generar muestras anonimizadas de los datos de telefonica"""

# Se define donde esta el archivo
file_name = '../muestraIBM.csv'

# Se lee el archivo
with open(file_name) as f:
    contenido = f.readlines()

# Se declara el listado donde se guardaran las lineas
archivo_modificado = []

# Se hace un recorrido linea por linea
for linea in contenido:
    # Se modifica la linea
    linea_nueva = linea[:-10]
    # Se hacen las permutaciones. Notese que para volver a la originalidad
    # basta con realizar este mismo proceso con el listado de permutaciones de
    # manera inversa.
    listado_permutaciones = [-3, -7, -8, -9, -6, -10, -5, -4]
    for permutacion in listado_permutaciones:
        linea_nueva += linea[permutacion]

    # Se agrega el ultimo cacho de la linea.
    linea_nueva += linea[-2:]

    # Se agrega esta linea al listado final
    archivo_modificado.append(linea_nueva)

# Se escribe el archivo modificado en un csv.
escribir = open('../muestraIBM_2.csv', 'w')

# Se recorre linea por linea
for linea_a_escribir in archivo_modificado:
    escribir.write(linea_a_escribir)

# Se cierra el archivo
escribir.close()
