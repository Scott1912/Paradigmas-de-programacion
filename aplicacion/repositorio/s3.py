from aplicacion.repositorio.repositorodeusuario import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

#======================================
# S3 es hijo de RepositorioDeUsuarios
#======================================
class S3(RepositorioDeUsuarios):
    __clientId: str
    __secretKey: str
    __bucket: str

    def __init__(mi, clienteId: str, secretKet: str, bucket: str):
        mi.__clienteId = clientId
        mi.__secretKey = secretKey
        mi.__bucket = bucket

    def abrir(mi) -> None:
        print(f"Estableciendo conexión a AWS S3 {mi.__clientId}:{mi.__secretKey}")
    def guardar(mi, usuario:Usuario) -> None:
        userData = { "nombre": usuario.getNombre(),
                    "apellido":
