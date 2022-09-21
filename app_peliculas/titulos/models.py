from django.db import models
from .list import *
# Create your models here.

class Localidad(models.Model):
    nombre = models.CharField("Nombre de la Localidad: ", max_length=50)
    cp = models.CharField("Código Postal: ", max_length=10)
    provincia = models.CharField("Provincia: ", max_length=50, choices=LISTA_PROV)    
    class Meta:
        ordering = ["pk"]
    
    def __str__(self):
        return "%s - CP: %s" % (self.nombre, self.cp)

class Persona(models.Model):
    nombre = models.CharField("Nombre/s", max_length=150)
    apellido = models.CharField(max_length=150)
    edad = models.IntegerField(null=True, blank=True)
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT)
    email = models.EmailField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_nacimiento = models.DateTimeField("Fecha de Nacimiento - (dd/mm/aaaa)")
    tipo_iva = models.CharField("Tipo de IVA", max_length=2, choices=TIPO_IVA_CHOICE, default="CF")
    
    class Meta:
        ordering = ["apellido", "nombre"]
    
    def __str__(self):
        return "%s %s" % (self.nombre, self.apellido)
    
    