from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Persona, Localidad

class FormularioPeliculas(forms.Form):    
    nombre = forms.CharField(label="Nombre", max_length=128)
    GENERO = (
        ("Accion", "Accion"),
        ("Drama", "Drama"),
        ("Romantica", "Romantica"),
        ("Infantil", "Infantil")
    )
    genero = forms.ChoiceField(label="Género", choices=GENERO)
    fecha = forms.DateField(
        label="Fecha de Filmación",
        widget=forms.DateInput(attrs={"type": "date"})
    )
    cantidad = forms.IntegerField(label="Cantidad de Ejemplares: ")
    EDADES = (
        ("ATP", "ATP - Apto para Todo Público"),
        ("INF", "INF - Peliculas Infantiles"),
        ("+18", "+18 - Contenido para Adultos")
    )
    edades = forms.ChoiceField(label="Audiencia: ", choices=EDADES)
    preventa = forms.BooleanField(label="¿Preventa OnLine?", required=False)
    
class LocalidadForm(ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'

class FormularioPersona(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'