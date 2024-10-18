import unittest
import sys
sys.path.append( "src" )

from model.credit_card import CreditCard
from controller.credit_card_controller import CreditCardController

class TestCreditCard( unittest.TestCase ):
    
    def test_insert( self ):
        CreditCardController.BorrarTodo()
        
        # Crear una tarjeta de credito
        tarjeta = CreditCard( numero_tarjeta="1234567890123456",
                             cedula="101010101010", franquicia="VISA", codigo_banco="07", fecha_vencimiento="2027-12-01", cupo=5000000, tasa_interes=3.5, cuota_manejo=40000)
        
        # Guardarla en la BD
        CreditCardController.Insertar( tarjeta )
        
        # Buscarla
        tarjeta_buscada = CreditCardController.BuscarTarjeta( tarjeta.numero_tarjeta )
        
        # Verificar si la trajo bien
        self.assertTrue(  tarjeta_buscada.EsIgual( tarjeta )  )
        
        

if __name__ == '__main__':
    unittest.main()        