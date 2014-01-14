#encoding:utf-8 
from django.forms import ModelForm
from django import forms
from models import User 
from models import Cliente, Empleado, Cita, Vehiculo, Proveedor, Compra, Venta, Producto, Usuario, Servicio
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	class Meta:
		model= User
		fields=('first_name','last_name','email')

class ClienteForm(forms.ModelForm):
	class Meta:
		model= Cliente

class EmpleadoForm(forms.ModelForm):
	class Meta:
		model= Empleado

class CitaForm(forms.ModelForm):
	class Meta:
		model= Cita

class VehiculoForm(forms.ModelForm):
	class Meta:
		model= Vehiculo

class ProveedorForm(forms.ModelForm):
	class Meta:
		model= Proveedor

class CompraForm(forms.ModelForm):
	class Meta:
		model= Compra

class VentaForm(forms.ModelForm):
	class Meta:
		model= Venta

class ProductoForm(forms.ModelForm):
	class Meta:
		model= Producto

class UsuarioForm(forms.ModelForm):
	class Meta:
		model= Usuario

class ServicioForm(forms.ModelForm):
	class Meta:
		model= Servicio

