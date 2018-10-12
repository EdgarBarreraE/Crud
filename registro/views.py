from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona
# Create your views here.

def index(request):
    return render(request,'index.html',{'name':'Registro de personas','personas':Persona.objects.all()})

def crear(request):
    nombre = request.POST.get('nombre','')
    correo = request.POST.get('correo','')
    persona = Persona(nombre=nombre,correo=correo)
    persona.save()
    return HttpResponse('datos cargados'+nombre+' '+correo)

def eliminar(request,id):
    persona = Persona.objects.get(pk = id)
    persona.delete()
    return HttpResponse('Persona eliminada')

def editar(request):
    nombre = request.POST.get('nombre','')
    correo = request.POST.get('correo','')
    id = request.POST.get('id',0)
    persona = Persona.objects.get(pk = id)
    persona.nombre = nombre
    persona.correo = correo
    persona.save()
    return HttpResponse('Persona Guardada')
