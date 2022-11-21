from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Database

def home(request):
    return render(request, "home.html")

def cartelera(request):
    return render(request, "cartelera.html")

def login(request):
    return render(request, "login.html")


def agregar(request):
    db=Database()
    info=db.all_genres()
    return render(request, "form-movie.html", {"info":info})

def recibiendoPeliculaNueva(request):
    # if request.method == "POST":   anidar?

    titulo=request.POST.get("titulo")
    duracion=request.POST.get("duracion")
    calificacion=request.POST.get("calificacion")
    imagenLink=request.POST.get("imagenLink")
    idioma=request.POST.get("idioma")
    genero=request.POST.get("genero")
    resenia=request.POST.get("resenia")


    db=Database()
    db.insert_movie(titulo, duracion, calificacion, imagenLink, idioma, genero, resenia)

    return render(request, "home.html")


