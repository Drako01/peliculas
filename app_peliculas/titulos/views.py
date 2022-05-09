from certifi import contents
from django.http import HttpResponse, Http404
from django.shortcuts import render
import sqlite3
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import forms


# Create your views here.

def index(request):

    return render(request, "titulos/index.html")


def nueva_pelicula(request):
    if request.method == "POST":
        form = forms.FormularioPeliculas(request.POST)
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
            return HttpResponse("Pelicula añadida Correctamemte.!!")            
    else:
        form = forms.FormularioPeliculas()
    ctx = {"form": form}
    return render(request, "titulos/nueva_pelicula.html", ctx)


def peliculas(request, template_name="titulos/peliculas.html"):
    conn = sqlite3.connect('peliculas.db')
    pelicula = conn.cursor()
    pelicula.execute("select * from peliculas")  
    pelicula_list = pelicula.fetchall()  
    conn.close()
    dato = {"peliculas": pelicula_list}
    return render(request, template_name, dato)
