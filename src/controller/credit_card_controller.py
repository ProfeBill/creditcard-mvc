
import sys
sys.path.append( "src" )

import psycopg2

from model.credit_card import CreditCard
import SecretConfig

class CreditCardController:

    def CrearTabla():
        """ Crea la tabla de tarjetas en la BD """
        cursor = CreditCardController.ObtenerCursor()

        cursor.execute("""create table tarjetas (
  numero_tarjeta varchar(16) primary key not null,
  cedula varchar(20) not null,
  franquicia varchar(20) not null,
  codigo_banco varchar(5) not null,
  fecha_vencimiento date,
  cupo decimal,
  tasa_interes decimal,
  cuota_manejo decimal
); """)
        cursor.connection.commit()

    def EliminarTabla():
        """ Borra la tabla de usuarios de la BD """
        cursor = CreditCardController.ObtenerCursor()

        cursor.execute("""drop table tarjetas""" )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()


    def InsertarUsuario( tarjeta : CreditCard ):
        """ Recibe un a instancia de la clase Usuario y la inserta en la tabla respectiva"""
        cursor = CreditCardController.ObtenerCursor()
        cursor.execute( f"""insert into tarjetas (cedula, nombre, apellido, 
                            direccion, telefono, 
                            codigo_municipio, codigo_departamento) 
                        values ({tarjeta.numero_tarjeta}, {tarjeta.cedula}, {tarjeta.franquicia}, {tarjeta.codigo_banco}, {tarjeta.fecha_vencimiento}, {tarjeta.cupo}, {tarjeta.tasa_interes}, {tarjeta.cuota_manejo})""" )

        cursor.connection.commit()

    def BuscarTarjeta( numero_tarjeta ) -> CreditCard:
        """ Trae una tarjeta dado su numero """
        cursor = CreditCardController.ObtenerCursor()

        cursor.execute(f"""select numero_tarjeta, cedula, franquicia, codigo_banco, fecha_vencimiento, cupo, tasa_interes, cuota_manejo
        from usuarios where numero_tarjeta = '{numero_tarjeta}'""" )
        fila = cursor.fetchone()
        resultado = CreditCard( numero_tarjeta=fila[0], cedula=fila[1], franquicia=fila[2], codigo_banco=fila[3], fecha_vencimiento=fila[4], cupo=fila[5], tasa_interes=fila[6], cuota_manejo=fila[7]  )
        return resultado



    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor
