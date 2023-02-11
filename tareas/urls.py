from django.urls import path
from . import views

#2 URL de pagina principal
urlpatterns = [
    path('', views.index, name='index'),
    path('eliminar/<str:pk>', views.eliminar, name='eliminar') #9 URL dinamica para eliminar la tarea con la id que recibe la URL
]
