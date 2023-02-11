from django.shortcuts import render, redirect
from .models import Tarea

# Create your views here.
#2 Crear vista de la página principal
def index(request):
    #8 Extraer todas las tareas desde la base de datos
    tareas = Tarea.objects.all()
    
    #7 Recibir título de nueva tarea ingresado en la entrada
    if request.method == 'POST':
        nueva_tarea = Tarea(
            titulo = request.POST['titulo']
        )
    
        nueva_tarea.save()
        return redirect('/')
    
    return render(request, 'index.html', {'tareas':tareas}) #8 Pasar la lista de tareas de la base de datos para mostrarlas en la página

#9 Eliminar la tarea con la id que se pasa por medio de la URL de eliminar
def eliminar(request, pk):
    tarea = Tarea.objects.get(id=pk)
    tarea.delete()
    return redirect('/')  #9 Redireccionar a la página principal para mostrar las tareas sin la tarea recién eliminada