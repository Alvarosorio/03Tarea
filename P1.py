import numpy as np
import matplotlib.pyplot as plt
from RK3 import *

'''
Aca resolvemos el problema del oscilador de Van der Pool
usando lo implementado en el script RK3
'''

#discretizamos el dominio
pasos = np.int(10000)
t = np.linspace(0, 20*np.pi, pasos)

#inicializamos los vectores que guardaran las soluciones
x1 = np.zeros(pasos)
v1 = np.zeros(pasos)
x2 = np.zeros(pasos)
v2 = np.zeros(pasos)

h = 20*np.pi/pasos

#resolvemos el problema para las primeras condiciones iniciales entregadas
x1[0] = 0.1
v1[0] = 0
for i in range(1, pasos):
    x, v = pasoRK_3(x1[i-1], v1[i-1], h)
    x1[i] = x
    v1[i] = v

#y para las segundas condiciones iniciales
x2[0] = 4.0
v2[0] = 0.0
for i in range(1, pasos):
    x, v = pasoRK_3(x2[i-1], v2[i-1], h)
    x2[i] = x
    v2[i] = v


#graficamos

fig = plt.figure()

plt.plot(x1, v1, label="Condiciones iniciales y=0.1, dy/ds=0")
plt.xlabel('y')
plt.ylabel('dy/ds')
plt.title("Oscilador de Van der Pool")
plt.legend(loc='lower right', fontsize=11)
plt.grid()

fig = plt.figure()

plt.plot(x2, v2, label="Condiciones iniciales y=4, dy/ds=0")
plt.xlabel('y')
plt.ylabel('dy/ds')
plt.title("Oscilador de Van der Pool")
plt.legend(loc='lower right', fontsize=11)
plt.grid()

fig = plt.figure()

plt.plot(t, x1,  label="Condiciones iniciales y=0.1, dy/ds=0")
plt.title("y(s)")
plt.xlabel('s')
plt.ylabel('y(s)')
plt.legend(fontsize=12)
plt.grid()

fig = plt.figure()

plt.plot(t, x2, label="Condiciones iniciales y=4, dy/ds=0")
plt.title("y(s)")
plt.xlabel('s')
plt.ylabel('y(s)')
plt.legend(fontsize=12)
plt.grid()

plt.show()
