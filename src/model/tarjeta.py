import datetime
class Tarjeta :
    
    def __init__(self, numero_tarjeta : str ,
  cedula : str,
  franquicia : str,
  codigo_banco : str,
  fecha_vencimiento : datetime,
  cupo : float,
  tasa_interes : float,
  cuota_manejo : float):
        """  Representa los datos de una tarjeta de credito que se almacenana en la tabla tarjetas """
        self.numero_tarjeta = numero_tarjeta
        self.cedula = cedula
        self.franquicia = franquicia
        self.codigo_banco = codigo_banco
        self.fecha_vencimiento = fecha_vencimiento
        self.cupo = cupo
        self.tasa_interes = tasa_interes
        self.cuota_manejo = cuota_manejo
        
    def EsIgual( self, otro ):
        """ Verifica si esta instancia de la clase es igual a otra """
        
        assert( self.numero_tarjeta == otro.numero_tarjeta )
        assert( self.cedula            == otro.cedula)
        assert( self.franquicia        == otro.franquicia)
        assert( self.codigo_banco      == otro.codigo_banco)
        # assert( self.fecha_vencimiento == otro.fecha_vencimiento)
        assert( self.cupo              == otro.cupo)
        assert( self.tasa_interes      == otro.tasa_interes)
        assert( self.cuota_manejo      == otro.cuota_manejo)
        
        return True
        
        