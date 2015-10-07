'''
Implementacion del de un paso del metodo Runge Kutta
de orden 3 para la resolucion de la EDO de Van der Pool
'''

#con esta funcion pasamos convertimos el problema
#en un sistema de dos edos de orden 1
def vector(x, v, mu=1.786):
    return [v, -x - mu * ((x**2) - 1) * v]

#definimos los K
def K_1(x_n, v_n, h):
    paso = vector(x_n, v_n)
    paso[0] *= h
    paso[1] *= h
    return paso[0], paso[1]

def K_2(x_n, v_n, h):
    k1 = K_1(x_n, v_n, h)
    paso = vector(x_n + k1[0]/2.0, v_n + k1[1]/2.0)
    paso[0] *= h
    paso[1] *= h
    return paso[0], paso[1]

def K_3(x_n, v_n, h):
    k1 = K_1(x_n, v_n, h)
    k2 = K_2(x_n, v_n, h)
    paso = vector(x_n - k1[0] - 2*k2[0],  v_n - k1[1] - 2*k2[1])
    paso[0] *= h
    paso[1] *= h
    return paso[0], paso[1]

#un paso del metodo
def pasoRK_3(xn, vn, h):
    k1 = K_1(xn, vn, h)
    k2 = K_2(xn, vn, h)
    k3 = K_2(xn, vn, h)
    x = xn + (1/6.0) * (k1[0] + 4*k2[0] + k3[0])
    v = vn + (1/6.0) * (k1[1] + 4*k2[1] + k3[1])

    return [x, v]
