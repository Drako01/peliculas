from django import forms

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