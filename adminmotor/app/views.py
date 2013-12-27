from django.shortcuts import render_to_response,get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from models import *
from forms import * 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required



def home(recuest):
	#usuarios = User.object.all()
	template="index.html"
	return render_to_response(template,locals())


def home(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/privado')
    if request.POST:
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/admin')
                else:
                    return render_to_response('noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('index.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/home')
def privado(request):
    usuario = request.user
    return render_to_response('servicios.html', {'usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='/home')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')