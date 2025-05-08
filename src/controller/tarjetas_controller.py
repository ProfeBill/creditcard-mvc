
import sys
sys.path.append( "." )
sys.path.append( "src" )

import psycopg2
import datetime

from model.tarjeta import Tarjeta
import SecretConfig

class TarjetasController:

    def CrearTabla():
        cursor = TarjetasController.ObtenerCursor()

        with open( "sql/crear-tarjetas.sql", "r"  ) as archivo:
            consulta = archivo.read()

        cursor.execute( consulta )
        cursor.connection.commit()

    def BorrarTabla():
        cursor = TarjetasController.ObtenerCursor()

        with open( "sql/borrar-tarjetas.sql", "r"  ) as archivo:
            consulta = archivo.read()

        cursor.execute( consulta )
        cursor.connection.commit()


    def Insertar( tarjeta : Tarjeta ):
        """ Recibe un a instancia de la clase Tarjeta y la inserta en la tabla respectiva"""
        cursor = TarjetasController.ObtenerCursor()
        cursor.execute( f"""insert into tarjetas (numero_tarjeta, cedula, franquicia, codigo_banco, fecha_vencimiento, cupo, tasa_interes, cuota_manejo) 
                        values ('{tarjeta.numero_tarjeta}', '{tarjeta.cedula}', '{tarjeta.franquicia}', '{tarjeta.codigo_banco}', '{tarjeta.fecha_vencimiento}', {tarjeta.cupo}, {tarjeta.tasa_interes}, {tarjeta.cuota_manejo})""" )

        cursor.connection.commit()

    def BuscarTarjeta( numero_tarjeta ) -> Tarjeta:
        """ Trae una tarjeta dado su numero """
        cursor = TarjetasController.ObtenerCursor()

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
