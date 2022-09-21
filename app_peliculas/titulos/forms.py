from django import forms
from django.forms import ModelForm
from .models import Persona, Localidad
from .list import *

class FormularioPeliculas(forms.Form):    
    nombre = forms.CharField(label="Nombre", max_length=128)    
    genero = forms.ChoiceField(label="Género", choices=GENERO)
    fecha = forms.DateField(
        label="Fecha de Filmación",
        widget=forms.DateInput(attrs={"type": "date"})
    )
    cantidad = forms.IntegerField(label="Cantidad de Ejemplares: ")   
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