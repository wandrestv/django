from django.shortcuts import redirect, render
from .models import Curso
from django.contrib import messages


# Create your views here.

def home(request):
    cursos = Curso.objects.all()
    messages.success(request,'¡Cursos listados!')
    return render(request, "gestioncursos.html", {"cursos": cursos})

def registrarcurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request,'¡Cursos registrado!')
    return redirect('/')

def edicioncurso(request,codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicioncurso.html", {"curso":curso})

def editarcurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    messages.success(request,'¡Cursos actualizado!')

    return redirect('/')

def eliminarcurso(request,codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    messages.success(request,'¡Cursos eliminado!')

    return redirect('/')