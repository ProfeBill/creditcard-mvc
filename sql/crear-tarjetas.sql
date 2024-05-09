drop table tarjetas;
create table tarjetas (
  numero_tarjeta varchar(16) primary key not null,
  cedula varchar(20) not null,
  franquicia varchar(20) not null,
  codigo_banco varchar(5) not null,
  fecha_vencimiento date,
  cupo decimal,
  tasa_interes decimal,
  cuota_manejo decimal
);