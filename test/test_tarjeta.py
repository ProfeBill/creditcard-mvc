import unittest
import sys
sys.path.append( "src" )

from model.tarjeta import Tarjeta
from controller.tarjetas_controller import TarjetasController

class TestTarjeta( unittest.TestCase ):
    
    def test_insert( self ):
        TarjetasController.BorrarTodo()
        
        # Crear una tarjeta de credito
        tarjeta = Tarjeta( numero_tarjeta="1234567890123456",
                             cedula="101010101010", franquicia="VISA", codigo_banco="07", fecha_vencimiento="2027-12-01", cupo=5000000, tasa_interes=3.5, cuota_manejo=40000)
        
        # Guardarla en la BD
        TarjetasController.Insertar( tarjeta )
        
        # Buscarla
        tarjeta_buscada = TarjetasController.BuscarTarjeta( tarjeta.numero_tarjeta )
        
        # Verificar si la trajo bien
        self.assertTrue(  tarjeta_buscada.EsIgual( tarjeta )  )
        
        

if __name__ == '__main__':
    unittest.main()        