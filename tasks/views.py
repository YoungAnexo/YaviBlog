from asyncio import tasks
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task, TaskComment
from .forms import TaskForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import TaskComment

# Create your views here.
def list_tasks(request):
    task1 = TaskComment.objects.all()
    return render(request, 'paginas/comentarios.html', {"task1": task1})

def create_task(request):
    task = TaskComment(tittle=request.POST['tittle'], hora=request.POST['hora'],fecha=request.POST['fecha'], description=request.POST['description'])
    task.save()
    return redirect('/Comentarios/')

def delete_task(request, task_id):
    task = TaskComment.objects.get(id=task_id)
    task.delete()
    return redirect('/Comentarios/')


def actualizar(request, task_id):
    task = TaskComment.objects.get(pk = task_id)

    if request.method == "POST":
        task.tittle    = request.POST["tittle"]
        task.hora    = request.POST["hora"]
        task.fecha     = request.POST["fecha"]
        task.description   = request.POST["description"]
        task.save()
        return redirect("/Comentarios/")
    return render(request, 'actualizar.html', {'task': task})

# Create your views here.
@login_required
def inicio(request):
    task = Task.objects.all()
    return render(request, "libros/index.html", {'tasks': task})

def Contactos(request):
    return render(request, "paginas/nosotros.html")

def Comentarios(request):
    return render(request, "paginas/comentarios.html")

def Anuncios(request):
    tasks = Task.objects.all()
    return render(request, "libros/index.html", {'tasks': tasks})

def crear(request):
    tasks = TaskForm(request.POST or None, request.FILES or None)
    if tasks.is_valid():
       tasks.save()
       messages.success(request, "creado correctamente")
       return redirect('Anuncios')
    return render(request, "libros/crear.html", {'tasks': tasks})

def editar(request, task_id):
    task = Task.objects.get(id=task_id)
    tasks = TaskForm(request.POST or None, request.FILES or None, instance=task)
    if tasks.is_valid()and request.POST:
        tasks.save()
        messages.success(request, "editado correctamente")
        return redirect('Anuncios')
    return render(request, "libros/editar.html", {'tasks': tasks})

def eliminar(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    messages.success(request, "eliminado correctamente")
    return redirect('Anuncios')

def publicacion(request):
    return render(request, "paginas/publicacion.html")

def iniciarSesion(request):
    return render(request, "registrations/login.html")





