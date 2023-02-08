from django.shortcuts import render
from django.http import HttpResponse
from App1.models import *

# Create your views here.

def inicio(request):
    return render(request, "App1/inicio.html")

def curso(request):

    cur1 = Curso(nombre="Desarrollo Web", camada= 11111)
    cur1.save()
    return render(request, "App1/cursos.html")

def estudiante(request):
    return render(request, "App1/estudiantes.html")

def profesor(request):
    return render(request, "App1/profesores.html")

def cursoFormulario(request):
    return render(request, "App1/cursoFormulario.html")