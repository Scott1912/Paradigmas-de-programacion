#===============================
# Chávez Mendoza Bryan Alexis
# ==============================
# Paradigmas de Programación
# Matemática Algorítmica
# ESFM IPN Septiembre 2023
#===============================

#===================================
# PROGRAMACIÓN ORIENTADA A OBJETOS
#===================================

#====================================
# Una clase para un objeto vacío
# No está tan vacío, necesita
# la palabra pass = pasar
#====================================
class ObjetoVacio:
    pass

#===========================
# nada es un ObjetoVacio
#===========================
nada = ObjetoVacio()
print(type(nada))

#===================
# La clase llanta
#===================
class Llanta:
    #========================================
    # Variable cuenta es de toda la clase
    #========================================
    cuanta = 0
    #========================================
    # Función constructora de identidad
    # __init__ es una función reservada
    # comienza con uno mismo : self
    # pero puede ser otro nombre (mi)
    # parámetros de entrada = default
    #========================================
    def __init__(mi,radio=50,ancho=30,presión=1.5):
        pass

