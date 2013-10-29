"""La idea de este Script es:
    1) Entregar una tabla que tiene una columna con las latitudes
    y otra columna con las longitudes.
    2) Reemplazar esas columnas por las coordenadas UTM."""

# Se importa la libreria de las transformaciones entre coordenadas
from pyproj import Proj


def transformador_coordenadas(listado_coordenadas):
    """
    listado_coordenadas: un listado de tuplas con dos elementos,
    el primero la longitud y luego la latitud.
    [(lon1, lat1),(lon2, lat2),(lon3, lat3),...]

    camino_destino: Es un String con el camino dentro del
    sistema operativo donde guardara el mismo archivo
    pero con las coordenadas UTM en vez de
    las coordenadas angulares.
    '/home/nombre_usuario/archivo_destino.csv'
    """
    # Se declara la instancia para realizar las transformaciones entre tipos de
    # coordenadas.
    transformador = Proj(proj='utm', zone='19', ellps='WGS84')
    # Listado con el resultado
    resultado = []
    # Se recorren las neuronas
    for coordenadas in listado_coordenadas:
        # Selecciono en una variable la longitud y la latitud
        lon = float(coordenadas[0])
        lat = float(coordenadas[1])

        # Transformacion de UTM a angulares
        UTM_X = transformador(lon, lat)[0]
        # En este punto voy a hacer una aclaracion. El resultado de
        # transformador(lon, lat)[1] se le suma 10 millo. y luego el resultado
        # de eso se multiplica por -1 porque en Google Earth aquella coordenada
        # esta invertida de aquella manera. Eso es lo que justifica la linea.
        UTM_Y = -(10000000 + transformador(lon, lat)[1])
        # Se agrega al resultado
        resultado.append([UTM_X, UTM_Y])

    return resultado

if "__main__" == __name__:
    """ Esta parte es el ejemplo que se modifica dependiento del caso."""

#################################################
# ZONA DE ENTREGA DE PARAMETROS

    # Se importa el archivo, primero se lee la ruta.
    path_to_csv = '/home/bernardo/Experimentos_Mobility/'
    path_to_csv += '36_Comportamiento_Esporadico/'
    path_to_csv += 'muestra_SanCarlos_27Abr.csv'

    # Archivo de destino
    archivo_destino = '/home/bernardo/Experimentos_Mobility/'
    archivo_destino += '36_Comportamiento_Esporadico/'
    archivo_destino += 'tabla_con_UTMs.csv'

    # El numero de las columnas de interes.
    num_col_lon = 5
    num_col_lat = 4

    # El separados
    separador = ','

#################################################

    # Luego se lee este
    with open(path_to_csv) as f:
        content = f.readlines()

    # Se escribe la misma lista, pero en vez de tener lon y lat tiene utm_x y
    # utm_y.
    # Con la siguiente linea obligo a que se borre el archivo que tenga el
    # mismo nombre.
    escribir = open(archivo_destino, 'w')

    # Y a continuacion se hace el cambio linea por linea
    # Este se guarda en la siguiente lista
    lista_resultado = []
    primera_linea = True
    for linea in content:
        # Se separa la linea por el separados entregado
        linea = linea.split(separador)
        # Selecciono las columnas de interes
        resultado = transformador_coordenadas([(linea[num_col_lon],
                                                linea[num_col_lat])])
        # El resultado lo reemplazo
        linea[num_col_lon] = str(resultado[0][0])
        linea[num_col_lat] = str(resultado[0][1])

        escribir.write(separador.join(linea))
        #import pdb
        #pdb.set_trace()  # XXX BREAKPOINT

    # Se cierra
    escribir.close()
