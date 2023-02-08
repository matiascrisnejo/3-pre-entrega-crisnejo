from django.shortcuts import render
from django.http import HttpResponse
from App1.models import *
from App1.forms import *

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



def crear_cursos(request):
    if request.method == 'POST':
        
        miFormulario = CursoFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            infodic = miFormulario.cleaned_data
            
            curso1 = Curso(nombre= infodic['nombre'], camada = infodic['camada'])
            
            curso1.save()
            
            return render(request, "App1/inicio.html")
    
    else:
        
        miFormulario= CursoFormulario()
        
    return render(request, "App1/crearCursos.html",{"formulario1":miFormulario})

def busquedaCamada(request):
    return render(request, "App1/inicio.html")

def resultados(request):
    
    if request.GET["camada"]:
        
        camada = request.GET["camada"]
        cursos = Cursos.objects.filter(camada__icontains=camada)
        
        return render(request, "App1/inicio.html", {"cursos":cursos, "camada":camada})
    
    else:
        respuesta= "no enviaste datos"
    
    return HttpResponse(respuesta)
