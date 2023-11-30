#===============================
# Chávez Mendoza Bryan Alexis
#===============================
# Paradigmas de Programación
# Matemática Algorítmica
# ESFM IPN Noviembre 2023
#===============================

#==============================
# Importar módulos necesarios
#==============================
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time
from numba import jit
from numba import cuda
from numba import *


#==========================
# Parámetros de entrada
#==========================
#----------------------------------------
# Número de celdas
n = np.array([512,512], dtype=np.intk64)
# Tamaño del dominio (menor que uno)
L = np.array([1.0,1.0],dtype=np.float64)
# Constante de difusión
kd:float64 = 0.2
# Pasos de tiempo
pasos:int = 1000
#-----------------------------------------

#===========================
# Parámetros secundarios
#===========================
# Tamaño de las celdas
dx = L/n
udx2 = 1.0/(dx*dx)
# Paso de tiempo
dt = 0.25*(min(dx[0], dx[1])**2)/kd
print("dt = ", dt)
# Total de celdas
nt = n[0]*n[1]
print("celdas = ", nt)

#=================================
# Función sin intérprete de python
#=================================
@jit(nopython= True)
def evolucion(u,n_0,n_1,udx2_0,udx2_1,dt,kd,i):
    jpl = i + n_0
    jml = i - n_0
    laplaciano = (u[i-1] -2.0*u[i] + u[i+1]) * udx2_0 + (u[jml]-2.0*u[i]+u[jpl])*udx2[1]
    unueva = u[i] + dt*k*laplaciano
    return unueva

#==========================================
# Loop acelerado sin intérprete de python
#==========================================
@jit(nopython=True)
def solucion (u, un, udx2, dt, n, k):
    for jj in range(1,n[1]-1):
        for ii in range(1,n[0]-1):
            i = ii + n[0]*jj
            #=====================================
            # Avanzar la ecuación en un punto
            #=====================================
            unueva = evolucion(u, n, udx2, dt, i, k)
            #==================================================
            # En medio de la malla poner temperatura fija 1
            #==================================================
            if i == int(nt/2) + int(n[0]/2):
                unueva = 1.0
            un[i] = unueva


#=======================
# PROGRAMA PRINCIPAL
#=======================
start = time.time()
#=====================
# Pasos de tiempo
#=====================
for t in range(1,pasos+1):
    #====================================
    # Avanzar ecuación en toda la malla
    #====================================
    solucion(u,un,udx2,dt,n,k)
    #================================
    # Copiar arreglo nuevo al viejo
    #================================
    u = un
    #=============================================
    # Avisar en pantalla el paso en el que va
    #=============================================
    if t%100 == 0: print("Iteración = ",t)


end = time.time()
print("Tardó: ", end-start, "s")

#=============================================
# Gráfico de la solución al tiempo final
#=============================================
u = np.reshape(u,(n[0],n[1]))
x,y = np.meshgrid(np.arange(0,L[0],dx[0]), np.arange(0,L[1],dx[1]))
ax = plt.axes(projection='3d')
ax.plot_surface(x,y,u,cmap=cm.hsv)
plt.show()
