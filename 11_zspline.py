#===============================
# Chávez Mendoza Bryan Alexis
# Paradigmas de Programación
# Matemática Algorítmica
# ESFM IPN Octubre 2023
#==============================

#================================================
# Cálculo de curva Z-spline en n dimensiones
#================================================
import numpy as np

#===============
# Clase Curva
#===============
class Curva:

    """====================================================
       Curva construye la curva qeu pasa por los puntos x
       ====================================================
       Parámetros: x coordenadas ordenadas ((x1),(x2),...)
                   f propiedades (f1(x),f2(x),...)
                   dim dimensiones
       ====================================================
    """
    #==============
    # Cosntructor
    #==============
    def __init__(s, x:float=[], dim:int=3):

        s.x = np.array(x,dtype=np.flot64)
        s.dim:np.int32 = dim
        s.n:np.int32 = int(len(s.x)/s.dim)  # Número de puntos
        s.l = []                            # Longitud sobre la curva
        s.lista_de_puntos()

    #====================
    # Lista de puntos
    #====================
    def lista_de_puntos(s) -> str:

        print(f"Número de puntos = {str(s.n)}")

        # Formato de datos
        s.formato = ""
        for j in range(s.dim):
            s.formato += "%15.8e"
        s.formato += "\n"

        # Tupla de varibles a imprimir
        for i in range(0,s.n):
            s.tup = (s.x[i],)
            for ii in range (1,s.dim):
                s.tup = s.tup + (s.x[i+ii*s.n],)
            print(s.formato % s.tup)

    #=========================
    # Longitud punto a punto
    #=========================
    def longitud(s) -> None:
        t:np.float64 = 0.0
        for i in range(0,s.n):
            ip1 = i +1
            if i == s.n-1:
                ip1 = 0
            d:np.float64 = (s.x[ip1]-s.x[i]**2
            for j in range(1,s.dim):
                d += (s.x[ip1 + j *s.n] - s.x[i+j * s.n]) **2
            t += d**0.5
            s.l.append(t)
        s.L = t
        s.dx = t/float(s.n)

    #===============
    # Interpolación 
    #===============
    def interpolacion(s,p:int=0,r:float=0.0) -> list:
        """ r es el parámetro sobre la curva [0,1]
            p es la suavidad de la curva """
        rdx:np.float64 = 1.0/s.dx
        xi:float = []
        i:np.int32 = int(r*s.L*rdx)
        a:np.float64 = r*s.L*rdx - float(i)  # Distancia normalizada

        #===========================
        # Interpolación lineal C0
        #===========================
        if p == 0:
           ip1:np.int32 = i+1
           if i == s.n - 1:
              ip1 = 0
           xi.append(a*s.x[ip1] + (1.0-a)*s.x[i+j*s.n])
        #=========================
        # Interpolación cúbica C1
        #=========================

