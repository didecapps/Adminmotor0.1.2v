from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'adminmotor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','app.views.home', name='home'),
   # url(r'^add/$','add.views.add', name='add'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup-email/', 'app.views.signup_email'),
    url(r'^email-sent/', 'app.views.validation_sent'),
    url(r'^login/$', 'app.views.home'),
    url(r'^logout/$', 'app.views.logout', name='logout'),
    url(r'^done/$', 'app.views.done', name='done'),
    url(r'^email/$', 'app.views.require_email', name='require_email'),
    url(r'^clienteR/$','app.views.Registro_cliente', name='clienteR'),
    url(r'^empleadoR/$','app.views.Registro_empleado', name='empleadoR'),
    url(r'^usuarioR/$','app.views.Registro_usuario', name='usuarioR'),
    url(r'^citaR/$','app.views.Registro_cita', name='citaR'),
    url(r'^vehiculoR/$','app.views.Registro_vehiculo', name='vehiculoR'),
    url(r'^proveedorR/$','app.views.Registro_proveedor', name='proveedorR'),
    url(r'^compraR/$','app.views.Registro_compra', name='compraR'),
    url(r'^ventaR/$','app.views.Registro_venta', name='ventaR'),
    url(r'^productoR/$','app.views.Registro_producto', name='productoR'),
    url(r'^servicioR/$','app.views.Registro_servicio', name='servicioR'),
    url(r'', include('social.apps.django_app.urls', namespace='social'))
)
