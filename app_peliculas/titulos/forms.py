from django import forms
from .models import LISTA_PROV, TIPO_IVA_CHOICE

class FormularioPeliculas(forms.Form):    
    nombre = forms.CharField(label="Nombre", max_length=128)
    GENERO = (
        ("ACC", "Accion"),
        ("DRA", "Drama"),
        ("ROM", "Romantica"),
        ("INF", "Infantil")
    )
    genero = forms.ChoiceField(label="Género", choices=GENERO)
    fecha = forms.DateField(
        label="Fecha de inicio",
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
    
class LocalidadForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=120)
    cp = forms.CharField(label="Código Postal", max_length=8)    
    provincia = forms.ChoiceField(label="Provincia", choices=LISTA_PROV)

class FormularioPersona(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=128)
    apellido = forms.CharField(label="Apellido",max_length=150)
    edad = forms.IntegerField(label="Edad")
    email = forms.EmailField(label="E-Mail",max_length=150)
    activo = forms.BooleanField(label="Es Activo?",required=False)
    fecha_nacimiento = forms.DateField(
        label="Fecha de Nacimiento",
        widget=forms.DateInput(attrs={"type": "date"})
    )    
    tipo_iva = forms.ChoiceField(label="Tipo de IVA", choices=TIPO_IVA_CHOICE)
    
