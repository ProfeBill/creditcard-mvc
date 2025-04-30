
import sys
sys.path.append( "." )
sys.path.append( "src" )

import psycopg2
import datetime

from model.tarjeta import Tarjeta
import SecretConfig

class CreditCardController:

    def BorrarTodo():
        """ Borra todos las filas de la tabla tarjetas """
        cursor = CreditCardController.ObtenerCursor()
        cursor.execute(  "delete from tarjetas;")
        cursor.connection.commit()

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


    def Insertar( tarjeta : Tarjeta ):
        """ Recibe un a instancia de la clase Tarjeta y la inserta en la tabla respectiva"""
        cursor = CreditCardController.ObtenerCursor()
        cursor.execute( f"""insert into tarjetas (numero_tarjeta, cedula, franquicia, codigo_banco, fecha_vencimiento, cupo, tasa_interes, cuota_manejo) 
                        values ('{tarjeta.numero_tarjeta}', '{tarjeta.cedula}', '{tarjeta.franquicia}', '{tarjeta.codigo_banco}', '{tarjeta.fecha_vencimiento}', {tarjeta.cupo}, {tarjeta.tasa_interes}, {tarjeta.cuota_manejo})""" )

        cursor.connection.commit()

    def BuscarTarjeta( numero_tarjeta ) -> Tarjeta:
        """ Trae una tarjeta dado su numero """
        cursor = CreditCardController.ObtenerCursor()

        cursor.execute(f"""select numero_tarjeta, cedula, franquicia, codigo_banco, fecha_vencimiento, cupo, tasa_interes, cuota_manejo
        from tarjetas where numero_tarjeta = '{numero_tarjeta}'""" )
        fila = cursor.fetchone()
        resultado = Tarjeta( numero_tarjeta=fila[0], cedula=fila[1], franquicia=fila[2], codigo_banco=fila[3], fecha_vencimiento=fila[4], cupo=fila[5], tasa_interes=fila[6], cuota_manejo=fila[7]  )
        return resultado



    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor
