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
    
class LocalidadForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=120)
    cp = forms.CharField(label="Código Postal", max_length=8)
    
    LISTA_PROV = (
        ("Buenos Aires","Buenos Aires"),
        ("Santa Fe","Santa Fe"),
        ("Códoba","Códoba"),
        ("CABA","CABA"),
        ("Catamarca","Catamarca"),
        ("Chaco","Chaco"),
        ("Chubut","Chubut"),
        ("Corrientes","Corrientes"),
        ("Entre Ríos","Entre Ríos"),
        ("Formosa","Formosa"),
        ("Jujuy","Jujuy"),
        ("La Pampa","La Pampa"),
        ("La Rioja","La Rioja"),
        ("Mendoza","Mendoza"),
        ("Misiones","Misiones"),
        ("Neuquén","Neuquén"),
        ("Río Negro","Río Negro"),
        ("Salta","Salta"),
        ("San Juan","San Juan"),
        ("San Luis","San Luis"),
        ("Santa Cruz","Santa Cruz"),
        ("Santiago del Estero","Santiago del Estero"),
        ("Tierra del Fuego","Tierra del Fuego"),
        ("Tucumán","Tucumán"),    
    )
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
    TIPO_IVA_CHOICE = (
    ("CF", 'Consumidor Final'),
    ("RI", 'Responsable Inscripto'),
    ("MT", 'Monotributo')
    )
    tipo_iva = forms.ChoiceField(label="Tipo de IVA", choices=TIPO_IVA_CHOICE)
    
