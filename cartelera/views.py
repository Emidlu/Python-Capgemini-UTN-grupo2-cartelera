from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# from .models import Database

def prueba(request):
    return render(request, "index.html")


# def pruebaDB(request):
    # db=Database()
    # info=db.all_users()
    # return render(request, "index.html", {"info": info})


