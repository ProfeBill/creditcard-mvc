
import sys
sys.path.append( "." )
sys.path.append( "src" )

import psycopg2
import datetime

from model.tarjeta import Tarjeta
import secret_config

class TarjetasController:

    def crear_tabla():
        cursor = TarjetasController.obtener_cursor()

        with open( "sql/crear-tarjetas.sql", "r"  ) as archivo:
            consulta = archivo.read()

        cursor.execute( consulta )
        cursor.connection.commit()

    def borrar_tabla():
        cursor = TarjetasController.obtener_cursor()

        with open( "sql/borrar-tarjetas.sql", "r"  ) as archivo:
            consulta = archivo.read()

        cursor.execute( consulta )
        cursor.connection.commit()


    def insertar( tarjeta : Tarjeta ):
        """ Recibe un a instancia de la clase Tarjeta y la inserta en la tabla respectiva"""
        cursor = TarjetasController.obtener_cursor()
        consulta = f"""insert into tarjetas (numero_tarjeta, cedula, franquicia, codigo_banco, fecha_vencimiento, cupo, tasa_interes, cuota_manejo) 
                        values ('{tarjeta.numero_tarjeta}', '{tarjeta.cedula}', '{tarjeta.franquicia}', '{tarjeta.codigo_banco}', '{tarjeta.fecha_vencimiento}', {tarjeta.cupo}, {tarjeta.tasa_interes}, {tarjeta.cuota_manejo})"""
    
        cursor.execute( consulta )

        cursor.connection.commit()

    def buscar_tarjeta( numero_tarjeta ) -> Tarjeta:
        """ Trae una tarjeta dado su numero """
        cursor = TarjetasController.obtener_cursor()

        consulta = f"""select numero_tarjeta, cedula, franquicia, codigo_banco, fecha_vencimiento, cupo, tasa_interes, cuota_manejo
        from tarjetas where numero_tarjeta = '{numero_tarjeta}'"""

        cursor.execute(consulta )
        fila = cursor.fetchone()
        resultado = Tarjeta( numero_tarjeta=fila[0], cedula=fila[1], franquicia=fila[2], codigo_banco=fila[3], fecha_vencimiento=fila[4], cupo=fila[5], tasa_interes=fila[6], cuota_manejo=fila[7]  )
        return resultado

    def buscar_por_cedula( numero_tarjeta ) -> list[Tarjeta]:
        """ Trae todas las tarjetas asociadas a la cedula de un usuario """
        cursor = TarjetasController.obtener_cursor()

        consulta = f"""select numero_tarjeta, cedula, franquicia, codigo_banco, fecha_vencimiento, cupo, tasa_interes, cuota_manejo
        from tarjetas where cedula = '{numero_tarjeta}'"""

        cursor.execute(consulta )
        lista = cursor.fetchall()
        if lista is None or lista.__len__ == 0:
            return

        resultado = []

        for fila in lista:                
            tarjeta = Tarjeta( numero_tarjeta=fila[0], cedula=fila[1], franquicia=fila[2], codigo_banco=fila[3], fecha_vencimiento=fila[4], cupo=fila[5], tasa_interes=fila[6], cuota_manejo=fila[7]  )
            resultado.append(tarjeta)
            
        return resultado


    def obtener_cursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=secret_config.PGDATABASE, user=secret_config.PGUSER, password=secret_config.PGPASSWORD, host=secret_config.PGHOST, port=secret_config.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor
