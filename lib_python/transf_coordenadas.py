"""Con este Script genero el KML"""

# Libreria Numpy
import numpy as np

# Se importa la libreria de las transformaciones entre coordenadas
from pyproj import Proj


def transformador_coordenadas(listado_coordenadas):
    # Se declara la instancia para realizar las transformaciones entre tipos de
    # coordenadas.
    transformador = Proj(proj='utm', zone='19', ellps='WGS84')
    # Se recorren las neuronas
    for neurona in datos_brutos:
        # Transformacion de UTM a angulares
        lon_sub = transformador(neurona[0],
                                -10000000 + neurona[1],
                                inverse='true')[0]
        lat_sub = transformador(neurona[0],
                                -10000000 + neurona[1],
                                inverse='true')[1]


if "__main__" == __name__:
    print "hola"
    # Se importa el archivo
    datos_brutos = [[-33, -70],[-33., -70.]]
