
import sys
sys.path.append( "src" )

import psycopg2

from model.Usuario import Usuario
import SecretConfig

class ControladorUsuarios :

    def CrearTabla():
        """ Crea la tabla de usuario en la BD """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)

        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        cursor.execute("""create table usuarios (
  cedula varchar( 20 )  NOT NULL,
  nombre text not null,
  apellido text not null,
  telefono varchar(20),
  correo text,
  direccion text not null,
  codigo_municipio varchar(40) not null,
  codigo_departamento varchar(40) NOT NULL
); """)
        connection.commit()

    def EliminarTabla():
        """ Borra la tabla de usuarios de la BD """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)

        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        cursor.execute("""drop table usuarios""" )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        connection.commit()


    def InsertarUsuario( usuario : Usuario ):
        """ Inserta una instancia de la clase Usuario en la tabla Usuarios """
        try:
            # Todas las instrucciones se ejecutan a tavés de un cursor
            connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
            # Todas las instrucciones se ejecutan a tavés de un cursor
            cursor = connection.cursor()
            cursor.execute(f"""
            insert into usuarios (
                cedula,   nombre,  apellido,  telefono,  correo, direccion, codigo_municipio, codigo_departamento
            )
            values 
            (
                '{usuario.cedula}',  '{usuario.nombre}', '{usuario.apellido}', '{usuario.telefono}', '{usuario.correo}', '{usuario.direccion}', '{usuario.codigo_municipio}', '{usuario.codigo_departamento}'
            );    """)
            
            # Las instrucciones DDL y DML no retornan resultados, por eso no necesitan fetchall()
            # pero si necesitan commit() para hacer los cambios persistentes
            cursor.connection.commit()
        except  :
            cursor.connection.rollback() 
            raise Exception("No fue posible insertar el usuario : " + usuario.cedula )        