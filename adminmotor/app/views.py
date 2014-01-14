from django.conf import settings
from django.shortcuts import render_to_response,get_object_or_404, render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from models import *
from forms import * 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from social.backends.google import GooglePlusAuth


def formas(request):
    #usuarios = User.object.all()
    template="agregar_cliente.html"
    return render_to_response(template,locals())

def home(request):
	#usuarios = User.object.all()
	template="index.html"
	return render_to_response(template,locals())

"""
def nuevo_usuario(request):
    if request.method=='POST':
        formcreateuser = UserCreationForm(request.POST)
        if formcreateuser.is_valid:
            formcreateuser.save()
            return redirect('done')
    else:
        formcreateuser = UserCreationForm()
    return render_to_response('index.html',{'formulario':formcreateuser}, context_instance=RequestContext(request))
"""
def login(request):
    if not request.user.is_anonymous():
        return redirect('done')
    if request.POST:
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return redirect('done')
                else:
                    return render_to_response('noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('index.html',{'formulario':formulario}, context_instance=RequestContext(request))

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return render_to_response('index.html', {}, RequestContext(request))


def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return redirect('done')
    return render_to_response('index.html', {
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None)
    }, RequestContext(request))


@login_required
def done(request):
    """Login complete view, displays user data"""
    scope = ' '.join(GooglePlusAuth.DEFAULT_SCOPE)
    return render_to_response('done.html', {
        'user': request.user,
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None),
        'plus_scope': scope
    }, RequestContext(request))


def signup_email(request):
    return render_to_response('email_signup.html', {}, RequestContext(request))


def validation_sent(request):
    return render_to_response('validation_sent.html', {
        'email': request.session.get('email_validation_address')
    }, RequestContext(request))


def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')

def require_email(request):
    if request.method == 'POST':
        request.session['saved_email'] = request.POST.get('email')
        backend = request.session['partial_pipeline']['backend']
        return redirect('social:complete', backend=backend)
    return render_to_response('email.html', RequestContext(request))

def Registro_cliente(request):
   # cliente=Clientes.objects.all()
    if request.method == "POST" :
        user_form = UserForm(request.POST, instance=request.user)
        cliente_form = ClienteForm(request.POST, instance=request.user.Cliente) 
        if user_form.is_valid() and cliente_form.is_valid():
           user_form.save()
           cliente_form.save()
           return HttpResponseRedirect("/")
    else: 
        user_form = UserForm(instance=request.user)
        cliente_form = ClienteForm(instance=request.user.Cliente)
    template = "agregar_cliente.html"
    return render_to_response(template,{'user_form': user_form,'clientes_form': cliente_form }, context_instance = RequestContext(request))
    
def Registro_empleado(request):
    #empleado=Empleado.objects.all()
    if request.method == "POST" :
        user_form = UserForm(request.POST, instance=request.user)
        empleado_form = EmpleadoForm(request.POST, instance=request.user.Empleado) 
        if user_form.is_valid() and empleado_form.is_valid():
           user_form.save()
           empleado_form.save()
           return HttpResponseRedirect("/")
    else: 
        user_form = UserForm(instance=request.user)
        empleado_form = EmpleadoForm(instance=request.user.Empleado)
    template = "agregar_cliente.html"
    return render_to_response({'user_form': user_form,'empleado_form': empleado_form }, context_instance = RequestContext(request))

def Registro_usuario(request):
    #usuario=Usuario.objects.all()
    if request.method == "POST" :
        user_form = UserForm(request.POST, instance=request.user)
        usuario_form = UsuarioForm(request.POST, instance=request.user.Usuario) 
        if user_form.is_valid() and usuario_form.is_valid():
           user_form.save()
           usuario_form.save()
           return HttpResponseRedirect("/")
    else: 
        user_form = UserForm(instance=request.user)
        usuario_form = UsuarioForm(instance=request.user.Usuario)
    template = "agregar_cliente.html"
    return render_to_response(template,{'user_form': user_form,'usuario_form': usuario_form }, context_instance = RequestContext(request,locals()))

def Registro_cita(request):
    cita=Cita.objects.all()
    if request.method == "POST":
        form = CitaForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect("/")
    else: 
        form = CitaForm()
    template = "agregar_cliente.html"
    return render_to_response(template,context_instance = RequestContext(request,locals()))

def Registro_vehiculo(request):
    vehiculo=Vehiculo.objects.all()
    if request.method == "POST":
        form = VehiculoForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect("/")
    else: 
        form = VehiculoForm()
    template = "agregar_cliente.html"
    return render_to_response(template,context_instance = RequestContext(request,locals()))

def Registro_proveedor(request):
    proveedor=Proveedor.objects.all()
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect("/")
    else: 
        form = ProveedorForm()
    template = "agregar_cliente.html"
    return render_to_response(template,context_instance = RequestContext(request,locals()))

def Registro_compra(request):
    compra=Compra.objects.all()
    if request.method == "POST":
        form = CompraForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect("/")
    else: 
        form = CompraForm()
    template = "agregar_cliente.html"
    return render_to_response(template,context_instance = RequestContext(request,locals()))

def Registro_venta(request):
    venta=Venta.objects.all()
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect("/")
    else: 
        form = VentaForm()
    template = "agregar_cliente.html"
    return render_to_response(template,context_instance = RequestContext(request,locals()))

def Registro_producto(request):
    producto=Producto.objects.all()
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect("/")
    else: 
        form = ProductoForm()
    template = "agregar_cliente.html"
    return render_to_response(template,context_instance = RequestContext(request,locals()))

def Registro_servicio(request):
    servicio=Servicio.objects.all()
    if request.method == "POST":
        form = ServicioForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect("/")
    else: 
        form = ServicioForm()
    template = "agregar_cliente.html"
    return render_to_response(template,context_instance = RequestContext(request,locals()))