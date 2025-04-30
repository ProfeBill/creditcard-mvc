import sys
sys.path.append("src")

from model.tarjeta import Tarjeta
from controller.tarjetas_controller import TarjetasController

from datetime import datetime


# Crear una instancia del Modelo

tarjeta = Tarjeta( numero_tarjeta="", cedula="", franquicia="", codigo_banco="", fecha_vencimiento=None, cupo=0, tasa_interes=0, cuota_manejo=0)

# Pedir al usuario, los datos para llenar la instancia
tarjeta.numero_tarjeta = input( "Ingrese el número de la tarjeta de credito: ")
tarjeta.cedula = input("Ingrese el numero de cédula: ")
tarjeta.franquicia = input("Ingrese la franquicia: ")
tarjeta.fecha_vencimiento = datetime.strptime( input("Ingrese la fecha de vencimiento: "), "%Y-%m-%d" )

# Llamar al controlador para que inserte en la BD
TarjetasController.Insertar( tarjeta )

print( "Tarjeta insertada exitosamente!")