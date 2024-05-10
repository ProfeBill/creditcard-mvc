import sys
sys.path.append("src")

from datetime import date

from model.Usuario import Usuario
from controller.ControladorUsuarios import ControladorUsuarios

try:
    cedula = input("Ingrese la cedula del usuario que desea buscar: ")
    usuario_buscado = ControladorUsuarios.BuscarUsuario( cedula )
    print(  f"Usuario encontrado : {usuario_buscado.nombre} {usuario_buscado.apellido}" )
except Exception as err:
    print("Error : " )
    print( str( err ) )
