create table compras (
  id_compra varchar(40) primary key not null,
  numero_tarjeta varchar(16) not null,
  fecha date not null,
  valor_compra decimal not null,
  tasa_interes decimal not null,
  cuotas int not null,
  cuota_mensual decimal not null
);