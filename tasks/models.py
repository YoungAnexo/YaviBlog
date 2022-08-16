from distutils.command.upload import upload
from xmlrpc.client import Boolean
from django.db import models

# Create your models here.
class Task(models.Model):
    Titulo = models.CharField(max_length=200)
    Fecha = models.CharField(max_length=200)
    NombreDeAutor = models.CharField(max_length=200)
    Cuerpo = models.CharField(max_length=200)
    Imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen", null=True)
    
    def __str__(self):
        fila = "Titulo:" + self.Titulo + " - " + "Fecha: " + self.Fecha + " - " + "NombreDeAutor: " + self.NombreDeAutor + " - " + "Cuerpo: " + self.Cuerpo
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.Imagen.storage.delete(self.Imagen.name)
        super().delete()
        
class TaskComment(models.Model):
    tittle = models.CharField(max_length=100)
    hora = models.CharField(max_length=100,null=True,blank=True)
    fecha = models.DateField('%A, %B %d, %Y %H:%M:%S',null=True,blank=True)
    description = models.TextField(blank=True)
