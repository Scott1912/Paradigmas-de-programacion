#===============================
# Chávez Mendoza Bryan Alexis
#===============================
# Paradigmas de Programación
# Matemática Algorítmica
# ESFM IPN Octubre 2023
#===============================

#==========================================================
# Del directorio aplicacion, el subdirectorio repostioro,
# el archivo basededatos.py : trae el objeto Basededatos
#==========================================================
from aplicacion.repositorio.basededatos import BaseDeDatos

#==========================================================
# Del directorio aplicacion, el subdirectorio repositorio,
# el archivo s3.py : trae el objeto S3
#==========================================================
from aplicacion.repositoro.s3 import S3

#=====================================================================
# Del directorrio aplicacion, el subdirectorio repositorio,
# el archivo sistemadearchivos.py : trae el objeto SistemaDeArchivos
#=====================================================================
from aplicacion.repositorio.sistemadearchivos import SistemaDeArchivos

#=============================================================
# Del adirectorio aplicacion, el subdirectoro modelos,
# el archivo usuario.py : trae el objeto Usuario
#=============================================================
from aplicacion.modelos.usario import Usuario

#============================================================================
# Del directorio aplicacion, el subdirectorio negocios,
# el archivo manejodeinscripciones.py : trae el objeto ManejoDeInscripciones
#============================================================================
from aplicacion.negocios.manejodeinscripciones import ManejoDeInscripciones

#==========================
# Crear el objeto Usuario
#==========================
usuario = Usuario("Roberto","Jimenez",18)

#========================
# Crear el objeto s3
#========================
repositoroS3 = S3("321321321", "sdf324223", "MiCubeta")

#================================================================
# Interface inscribirUsuario del objeto ManejoDeInscripciones
#================================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioS3)
print("\n")

#===================================
# Crear el objeto sistemadearchivos
#===================================
repositorioSistemaDeArchivos = SistemaDeArchivos("/home/users")

#===============================================================
# Interface inscribirUsuario del objeto ManejoDeInscripciones
#===============================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioSistemaDeArchivos)
print("\n")

#=============================
# Crear el objeto basededatos
#=============================
repositorioBaseDeDatos = BaseDeDatos("localhost","admin","admin123")

#=================================================================
# Insterface inscribirUsuario del objeto ManejoDeInscripciones
#=================================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioBaseDeDatos)
print("\n")

