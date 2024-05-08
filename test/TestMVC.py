# Todas las prueba sunitarias importan la biblioteca unittest
import unittest

import sys
sys.path.append("src")

from datetime import date

from model.Usuario import Usuario
from controller.ControladorUsuarios import ControladorUsuarios

class ControllerTest(unittest.TestCase):

    def testCreateTable( self ):
        """ Prueba que se cree correctamente la tabla en la BD """

        # Llamar a la clase COntrolador para que cree la tabla
        ControladorUsuarios.EliminarTabla()
        ControladorUsuarios.CrearTabla()

        # Insertar un Usuario en la tabla
        usuario_prueba = Usuario( cedula="1234657", nombre="Prueba", apellido="Unitaria", direccion="kjgjhfjkhfhgfhgfh",
                                 telefono="654321654", correo="no@tiene.com", codigo_municipio="05001", codigo_departamento="05" )
        ControladorUsuarios.InsertarUsuario( usuario_prueba )

        # Buscar al usuario
        usuario_buscado = ControladorUsuarios.BuscarUsuarioCedula( "1234657" )

        # Verificar Si lo trajo correctamente
        self.assertEqual(  usuario_prueba.cedula, usuario_buscado.cedula )



if __name__ == '__main__':
    # print( Payment.calcularCuota.__doc__)
    unittest.main()