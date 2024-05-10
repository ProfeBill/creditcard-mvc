# Todas las prueba sunitarias importan la biblioteca unittest
import unittest

import sys
sys.path.append("src")

from datetime import date

from model.Usuario import Usuario
from controller.ControladorUsuarios import ControladorUsuarios

import psycopg2

class ControllerTest(unittest.TestCase):

    # Test Fixture
    def setUpClass():
        # Llamar a la clase COntrolador para que cree la tabla
        ControladorUsuarios.EliminarTabla()
        ControladorUsuarios.CrearTabla()

    def testInsertAndSelect1( self ):
        """ Prueba que se cree correctamente la tabla en la BD """
        # Insertar un Usuario en la tabla
        usuario_prueba  = Usuario( cedula="1234657", nombre="Prueba", apellido="Unitaria", direccion="kjgjhfjkhfhgfhgfh",
                                 correo="no@tiene.com", telefono="321654987", codigo_departamento="05", codigo_municipio="05001" )
        ControladorUsuarios.InsertarUsuario( usuario_prueba )

        # Verificar si la tabla quedo creada correctamente
        usuario_buscado = ControladorUsuarios.BuscarUsuario( cedula="1234657" )

        # Comparar si el usuario que se insertó, contiene la misma información, que el retornado
        usuario_buscado.esIgual( usuario_prueba )


    def testInsertAndSelect2( self ):
        """ Prueba que se cree correctamente la tabla en la BD """

        # Insertar un Usuario en la tabla
        usuario_prueba  = Usuario( cedula="5555555", nombre="Otra", apellido="Prueba", direccion="no tiene",
                                 correo="otro@tiene.com", telefono="654654654", codigo_departamento="76", codigo_municipio="76001" )
        ControladorUsuarios.InsertarUsuario( usuario_prueba )

        # Verificar si la tabla quedo creada correctamente
        usuario_buscado = ControladorUsuarios.BuscarUsuario( cedula=usuario_prueba.cedula )

        # Comparar si el usuario que se insertó, contiene la misma información, que el retornado
        usuario_buscado.esIgual( usuario_prueba )

    def testPrimaryKey(self):
        # Insertar un Usuario en la tabla
        usuario_prueba  = Usuario( cedula="4444", nombre="Otra", apellido="Prueba", direccion="no tiene",
                                 correo="otro@tiene.com", telefono="654654654", codigo_departamento="76", codigo_municipio="76001" )
        ControladorUsuarios.InsertarUsuario( usuario_prueba )

        # Insertar un Usuario en la tabla
        usuario_otro  = Usuario( cedula="4444", nombre="Diferente", apellido="Prueba", direccion="no tiene",
                                 correo="otro@tiene.com", telefono="654654654", codigo_departamento="76", codigo_municipio="76001" )
        
        self.assertRaises( Exception, ControladorUsuarios.InsertarUsuario, usuario_otro )



if __name__ == '__main__':
    # print( Payment.calcularCuota.__doc__)
    unittest.main()
