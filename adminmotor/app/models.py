from django.db import models
from django.contrib.auth.models  import User

# Create your models here.

class Pais(models.Model):
	nombre_pais=models.CharField(('Nombre'),max_length=140)
	lat=models.FloatField(max_length= 120)
	lon=models.FloatField(max_length=120)
	cod_tel= models.CharField(max_length=5)
	def __unicode__(self):
		return self.nombre_pais

class Tipo_Usuario(models.Model):
	nombre_tu=models.CharField(max_length =50)
	def __unicode__(self):
		return self.nombre_tu

class Paquete(models.Model):
	tipo_paquete = models.CharField(max_length=50)
	def __unicode__(self):
		return self.tipo_paquete

class Estado(models.Model):
	nombre_estado = models.CharField(('Nombre'), max_length= 150)
	lat=models.FloatField()
	lon=models.FloatField()
	pais = models.ForeignKey(Pais,verbose_name=('Pais'))
	def __unicode__(self):
		return self.nombre_estado

class Ciudad(models.Model):
	nombre_ciudad = models.CharField(('Nombre'), max_length =150)
	lat=models.FloatField()
	lon=models.FloatField()
	pais = models.ForeignKey(Pais,verbose_name=('Pais'))
	estado = models.ForeignKey(Estado, verbose_name= ('Estado'))
	def __unicode__(self):
		return self.nombre_ciudad

class Modelo(models.Model):
	nombre_modelo = models.CharField(max_length =80)
	#imagen = models.ImagenField()
	def __unicode__(self):
		return self.nombre_modelo

class Marca(models.Model):
	nombre_marca = models.CharField(max_length = 80)
	modelo = models.ForeignKey(Modelo)
	def __unicode__(self):
		return self.nombre_marca

class Vehiculo(models.Model):
	placas = models.CharField(max_length = 9)
	color = models.CharField( max_length = 120)
	ano = models.DateField()
	numero_serie = models.CharField(max_length=16)
	#marca =models.ForeignKey(Marca)
	modelo = models.ForeignKey(Modelo)
	def __unicode__(self):
		return "%s-%s-%s"%(self.modelo,self.color,self.placas)

class Proveedor(models.Model):
	nombre_proveedor = models.CharField(max_length =50)
	direccion_proveedor = models.CharField(max_length =50)
	telefono_proveedor = models.CharField(max_length = 50)

class Tipo_Servicio(models.Model):
	nombre_tipoServicio = models.CharField(max_length = 100)
	vehiculo= models.ForeignKey(Vehiculo)

class Marca_producto(models.Model):
	nombre_marca_producto = models.CharField(max_length = 80)
 	def __unicode__(self):
		return self.nombre_marca_producto
		
class Tipo_pago(models.Model):
	nombre_pago =models.CharField(max_length=140)																	
	
class Compra(models.Model):
   	nombre_producto = models.CharField(max_length=50)
	fecha = models.DateField()
	cantidad = models.IntegerField(max_length = 4)
	proveedor = models.ForeignKey(Proveedor)
	tipo_pago = models.ForeignKey(Tipo_pago)


class Cliente(models.Model):
	user= models.OneToOneField(User,unique=True)
	telefono_cliente = models.CharField(max_length =140)
	estado=models.ForeignKey(Estado)
	vehiculo = models.ForeignKey(Vehiculo)
	#tipo_pagoc = models.ForeignKey(Tipo_pago)
	#citasc = models.ForeignKey(Citas)

class Cita(models.Model):
	dia_hora = models.DateField()
	cliente = models.ForeignKey(Cliente)
										
class Venta(models.Model):
	cantidad= models.IntegerField(max_length = 4)
	nombre_producto = models.CharField(max_length = 20)
	cliente= models.ForeignKey(Cliente)

class Producto(models.Model):
	nombre_producto =models.CharField(max_length=50)
	cantidad_existencia =models.IntegerField(max_length=4)
	venta= models.ForeignKey(Venta)
	compra = models.ForeignKey(Compra)
	marca = models.ForeignKey(Marca_producto)
						

class Usuario(models.Model):
	user = models.ForeignKey(User, unique=True)	
   	direccion_u = models.CharField(max_length =140)
	#email_usuario = models.CharField(max_length =50)
	tipo_usuariou = models.ForeignKey(Tipo_Usuario)		
	paquete =models.ForeignKey(Paquete)

class Empleado(models.Model):
	user = models.ForeignKey(User,unique=True)
	direccion_emp = models.CharField(max_length=140)
	telefono_emp = models.CharField(max_length = 140)
	usuario = models.ForeignKey(Usuario)

class Servicio(models.Model):
	nombre_servicio = models.CharField(max_length=100)
	descripcion = models.TextField(max_length =500)
	tipo_servicio = models.ForeignKey(Tipo_Servicio)
	#vehiculo = models.ForeignKey(Vehiculo)
