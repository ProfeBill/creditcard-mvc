# creditcard-mvc
Sample Database application using MVC pattern bound to postgresql

## Prerrequisitos

Instale el paquete psycopg2 con:

    pip install psycopg2

Asegurese de tener una base de datos PostgreSQL y sus respectivos datos de acceso

Copie el archivo SecretConfig-sample.py como SecretConfig.py y establezca en este archivo los
datos de conexion a su base de datos.

## Configuracion de la base de datos

Esta aplicacion requiere que este creada una tabla llamada usuarios.

Utilice el script en sql\crear-usuarios.sql para crear antes de ejecutar la aplicacion
o las pruebas unitarias para que se creen las tablas necesarias

