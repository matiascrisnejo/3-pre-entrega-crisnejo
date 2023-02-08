
from django.urls import path
from App1.views import *

urlpatterns = [
    path("",inicio, name="start"),
    path("cursos",curso, name= "cursos"),
    path("profesores",profesor, name= "profes"),
    path("estudiantes",estudiante, name= "estudiantes"),
    path("crear_curso/",crear_cursos, name="crear_curso"),
    path("buscar_camada/",busquedaCamada, name="buscar camadas"),
    path("resultados/",resultados, name="resultados busqueda"),
]
