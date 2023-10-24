from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

#==================================
# Clase ManejoDeInscripciones
# NO TIENE VARIABLES !!!
#==================================
class ManejoDeInscripciones:
    #======================================================
    # Decorador staticmethod
    # El objeto sólo tiene la función inscribirUsuario
    # ENVUALVE LA FUNCIÓN SIN LLAMAR VARIABLES LOCALES
    #======================================================
    @staticmethod
    def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
        print("-----> Guardando usuario ... \n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()

