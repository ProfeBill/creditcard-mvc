from datetime import date

class Usuario:
    """
    Pertenece la Capa de Reglas de Negocio (Model)

    Representa a un usuario de la Tarjeta de Credito en la aplicación
    """
    def __init__( self, cedula, nombre, apellido, correo, direccion, telefono, codigo_departamento, codigo_municipio )  :
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono
        self.codigo_departamento = codigo_departamento
        self.codigo_municipio = codigo_municipio


    def is_equal( self, comparar_con ) :
        """
        Compara el objeto actual, con otra instancia de la clase Usuario
        """
        assert( self.cedula == comparar_con.cedula )
        assert( self.nombre == comparar_con.nombre )
        assert( self.apellido== comparar_con.apellido )
        assert( self.direccion== comparar_con.direccion )
        assert( self.correo== comparar_con.correo )
        assert( self.telefono== comparar_con.telefono )
        assert( self.codigo_departamento== comparar_con.codigo_departamento )
        assert( self.codigo_municipio== comparar_con.codigo_municipio )

