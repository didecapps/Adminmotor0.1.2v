from django.contrib import admin
from models import Marca,Modelo,Estado,Ciudad,Pais,Tipo_Usuario,Paquete,Tipo_Servicio,Marca_producto,User

class MarcaAdmin(admin.ModelAdmin):
	list_display =('id','nombre_marca')
	search_fields=('nombre_marca',)
	
class ModeloAdmin(admin.ModelAdmin):
	list_display=('id','nombre_modelo')
	search_fields=('nombre_modelo',)
	
class CiudadAdmin(admin.ModelAdmin):
	list_display=('id','nombre_ciudad')
	search_fields=('nombre_mciudad',)
	
class EstadoAdmin(admin.ModelAdmin):
	list_display=('id','nombre_estado')
	search_fields=('nombre_estado',)

class PaisAdmin(admin.ModelAdmin):
	list_display =('id','nombre_pais','lon','lat')
	search_fields=('nombre_pais','lon','lat',)

class Tipo_UsuarioAdmin(admin.ModelAdmin):
	list_display = ('id','nombre_tu')
	search_fields = ('nombre_tu',)

class PaqueteAdmin(admin.ModelAdmin):
	list_display = ('id','tipo_paquete')
	search_fields = ('tipo_paquete',)

class Tipo_ServicioAdmin(admin.ModelAdmin):
	list_display = ('id','nombre_tipoServicio')
	search_fields = ('nombre_tipoServicio',)

class Marca_ProductoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre_marca_producto')
	search_fields = ('nombre_marca_producto',)
	

		
		

admin.site.register(Marca,MarcaAdmin)
admin.site.register(Modelo,ModeloAdmin)
admin.site.register(Ciudad,CiudadAdmin)
admin.site.register(Estado,EstadoAdmin)
admin.site.register(Pais,PaisAdmin)
admin.site.register(Tipo_Usuario,Tipo_UsuarioAdmin)
admin.site.register(Paquete,PaqueteAdmin)
admin.site.register(Tipo_Servicio,Tipo_ServicioAdmin)
admin.site.register(Marca_producto,Marca_ProductoAdmin)




