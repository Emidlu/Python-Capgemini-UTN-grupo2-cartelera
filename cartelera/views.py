from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# from .models import Database

def home(request):
    return render(request, "home.html")

def cartelera(request):
    return render(request, "cartelera.html")

def login(request):
    return render(request, "login.html")

# def pruebaDB(request):
    # db=Database()
    # info=db.all_users()
    # return render(request, "index.html", {"info": info})


