from django.shortcuts import redirect, render
import sqlite3
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import forms
from .forms import *
from . models import Localidad, Persona
from titulos import models

# Create your views here.

def index(request, template_name="titulos/index.html"):
    return render(request, template_name)


def nueva_pelicula(request, template_name="titulos/nueva_pelicula.html"):
    if request.method == "POST":
        form = FormularioPeliculas(request.POST)
        if form.is_valid():
            conn = sqlite3.connect("peliculas.db")
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO peliculas VALUES (?, ?, ?, ?, ?, ?)",
                (form.cleaned_data["nombre"], form.cleaned_data["genero"], form.cleaned_data["fecha"],
                form.cleaned_data["cantidad"], form.cleaned_data["edades"], form.cleaned_data["preventa"])
            )
            conn.commit()
            conn.close()
            return HttpResponseRedirect(reverse("carga_pelicula"))            
    else:
        form = FormularioPeliculas()
    ctx = {"form": form}
    return render(request, template_name, ctx)


def peliculas(request, template_name="titulos/peliculas.html"):
    conn = sqlite3.connect('peliculas.db')
    pelicula = conn.cursor()
    pelicula.execute("select * from peliculas")  
    pelicula_list = pelicula.fetchall()  
    conn.close()
    dato = {"peliculas": pelicula_list}
    return render(request, template_name, dato)


def carga_pelicula(request, template_name="titulos/carga_pelicula.html"):
    return render(request, template_name)

def localidades(request, template_name="titulos/localidades.html"):
    lista_localidades = Localidad.objects.all()
    dato = {"localidades": lista_localidades}
    return render(request, template_name, dato)

def localidad(request, id_localidad, template_name="titulos/localidad.html"):
    localidad_dato = Localidad.objects.get(id=id_localidad)
    dato = {"localidad" : localidad_dato}
    return render(request, template_name, dato)

def nueva_localidad(request, template_name="titulos/nueva_localidad.html"):
    if request.method == "POST":
        form = LocalidadForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('localidades')
    else:
        form = LocalidadForm()
    dato = {"form": form }    
    return render(request, template_name, dato)


def personas(request, template_name="titulos/personas.html"):
    lista_personas = Persona.objects.all()
    dato = {"personas": lista_personas}
    return render(request, template_name, dato)


def nueva_persona(request, template_name="titulos/nueva_persona.html"):
    if request.method == "POST":
        form = FormularioPersona(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('personas')
    else:
        form = FormularioPersona()
    dato = {"form": form }    
    return render(request, template_name, dato)