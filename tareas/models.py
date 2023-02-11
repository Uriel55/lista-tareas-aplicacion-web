from django.db import models

# Create your models here.
# Crear modelo de las tareas para la base de datos
class Tarea(models.Model):
    titulo = models.CharField(max_length=2000)
    
    #5 Realizar migraciones a la base de datos después de crear el modelo. También llegado a este paso; crear superusuario, django admin
    
    def __str__(self):
        return self.titulo