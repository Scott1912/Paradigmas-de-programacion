#=================================
# Chávez Mendoza Bryan Alexis
#=================================
#  Paradigmas de Programación
#  Matemática Algorítmica
#  ESFM-IPN sept-2023
#=================================

''' ESTE ES UN SUKPERCOMENTARIO
    DE INICIO A NUESTRO RESUMEN
'''
#====================
# Operaciones básicas
#====================
print (2+3)
print (2*3)
print (2**10)    # raíz cuadrada
print (2**0.5)   # exclusivo en python

#==========================================
# Para saber el tipo de objeto se usa type
#==========================================
t=0
print(type(t)) # entero
t=3.6
print(type(t)) #real (flotante)
t=True
print(type(t)) # booleano (bool)

#=========================
# Mensajes a pantalla
#=========================
print ("Este es un comando de python. ", "Este es otro enunciado.", t)
print('id: ', 1)
print('First Name: ', 'Steve')
print('Last Name: ', 'Jobs')
print("vamos a sumar esto" + " con esto otro")

#===============================================
# Continuar una instrucción en varios renglones
#===============================================
if 100 > 99 and \
        200 <= 300 and \
        True != False:
            print('Hello World!')

#================================================
# Usando paŕentesis redondos, cuadrrados o llaves
# se puede escribir en varios renglones
#=================================================
list = [1, 2, 3, 4, 
        5, 6, 7, 8,
        9, 10, 11, 12]

matriz = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]

print(list)
print(matriz)

#====================================================================
# Indentación estricta para procesos dependientes de :  (dos puntos)
#====================================================================
if 10>5:
    print ("diez es mayor que cinco")
    print("otra identación")
for i in list:
    print (i)
    print("ok")
if 10>5:
    print("verdadero")
    if 10<20:
        print("verdadero")
elif 5>3: # comienza segundo condicional
    print ("esto no se imprimirá")
else:
    print ("aquí nunca llega")

#===========
# Funciones
#==========
def say_hello(name):
    print("Hello ", name)
    print("Welcome to Python Tutorials")

say_hello("Scott")
