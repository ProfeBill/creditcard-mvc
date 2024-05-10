import sys
sys.path.append("src")

from model.Usuario import Usuario
from controller.ControladorUsuarios import ControladorUsuarios


# Insertar un Usuario en la tabla
usuario  = Usuario( cedula="", nombre="", apellido="", direccion="",
                            correo="", telefono="", codigo_departamento="", codigo_municipio="" )

print("Por favor ingrese los datos del usuario que desea crear")

usuario.cedula = input("Cedula : ")
usuario.nombre = input("Nombre : ")
usuario.apellido = input("Apellido : ")
usuario.direccion = input("Direccion : ")
usuario.correo = input("Correo : ")
usuario.telefono = input("Telefono : ")
usuario.codigo_departamento = input("Codigo Departamento : ")
usuario.codigo_municipio = input("Codigo departamento : ")

ControladorUsuarios.InsertarUsuario( usuario )

print("Usuario insertado correctamente!")
