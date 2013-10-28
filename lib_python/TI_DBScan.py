# Libreria numpy
import numpy as np
# Libreria para ordenar instancias en una lista
import operator


def TI_ExpandCluster(conj_puntos, conj_revisado,
                     p, ClId, eps, MinPts):
    return


def Distance(punto, pnt_ref):
    """Funcion que calcula la distancia en dos dimenciones"""
    punto = np.array(punto[0:2])
    pnt_ref = np.array(pnt_ref[0:2])
    return np.sqrt(np.sum(np.power(punto - pnt_ref, 2)))


class clase_punto:
    """Clase que genera un punto con sus atributos"""
    def __init__(self, punto, pnt_ref):
        # p.ClusterId = UNCLASSIFIED;
        self.ClusterId = "Sin Clasificar"
        # p.dist = Distance(p,r)
        self.dist = Distance(punto, pnt_ref)
        # p.NeighborsNo = 1
        self.NeighborsNo = 1
        # p.Border = vacio
        self.Border = None


def TI_DBScan(conj_puntos, eps, MinPts):
    """Esta clase aplica el algoritmo TI-DBScan al conjunto
    de puntos entregados.

    conj_puntos = [[coord1, coord2, ...], ...]:
        Es un listado de tuplas o listas, donde los dos
    primeros elementos de cada lista son las coordenadas."""
    # /* assert: r denotes a reference point */
    pnt_ref = conj_puntos[0]
    # D’ = empty set of points;
    conj_revisado = []

    # for each point p in set D do
        # p.ClusterId = UNCLASSIFIED;
        # p.dist = Distance(p,r)
        # p.NeighborsNo = 1
        # p.Border = vacio
    # endfor
    conj_puntos = [clase_punto(punto, pnt_ref)
                   for punto in conj_puntos]

    # sort all points in D non-decreasingly w.r.t. field dist;
    conj_ordenado = sorted(conj_puntos, key=operator.attrgetter('dist'))
    conj_puntos = sorted(conj_puntos, key=operator.attrgetter('dist'))

    # ClusterId = label of first cluster;
    i = 1
    ClusterId = "Cluster %s" % (i)

    # for each point p in the ordered set D starting from
    # the first point until last point in D do
    for p in conj_ordenado:
        # if TI-ExpandCluster(D, D’, p, ClusterId, Eps, MinPts) then
        if TI_ExpandCluster(conj_puntos, conj_revisado,
                            p, ClusterId, eps, MinPts):
            # ClusterId = NextId(ClusterId)
            i += 1
            ClusterId = "Cluster %s" % (i)
        # endif
    # endfor

    # return D’// D’ is a clustered set of points
    return conj_revisado
