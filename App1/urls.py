
from django.urls import path
from App1.views import *

urlpatterns = [
    path("",inicio, name="start"),
    path("cursos",curso, name= "cursos"),
    path("profesores",profesor, name= "profes"),
    path("estudiantes",estudiante, name= "estudiantes"),
    path("cursoFormulario",cursoFormulario, name="formularioCurso"),
]
