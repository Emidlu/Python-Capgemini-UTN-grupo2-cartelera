from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Database
from datetime import date, time, datetime, timedelta
from .aux_shows import *

# def home(request):
#     try:
#         user_id = request.session["user_id"]
#         return render(request, "home.html", {"user_id":True})
#     except:
#         return render(request, "home.html")


# def cartelera(request):
#     return render(request, "cartelera.html")


# def cartelera(request):
#     db=Database()
#     info=db.all_movies()

#     return render(request, "cartelera.html")




def agregarPelicula(request):
    db=Database()
    info=db.all_genres()

    return render(request, "form-movie.html", {"info":info, "user_id":True})


def agregarFuncion(request):
    if request.method == "POST": #Si entra por POST
        peliculaId=request.POST.get("peliculaId")
        salaId=request.POST.get("salaId")
        date=request.POST.get("date")
        time=request.POST.get("time")

        #Convertir a datetime
        fechaConcatenada = date + " " + time
        fecha_dt = datetime.strptime(fechaConcatenada, '%Y-%m-%d %H:%M:00')

        db=Database()
        db.insert_show(peliculaId, salaId, fecha_dt)

        #Hacer que redireccione a la pagina de panel de administrador
        movies=db.all_movies()
        rooms=db.all_rooms()
        fechaHoraActual = datetime.now()

        lunesAnterior = primerLunesAnterior(fechaHoraActual)
        lunesSiguiente = lunesAnterior + timedelta(days=7)
        matrizSemana1 = matriz_shows(lunesAnterior)
        matrizSemana2 = matriz_shows(lunesSiguiente)
        dias = catorceDias(lunesAnterior)

        return render(request, "form-show.html", {"movies":movies, "rooms":rooms, "user_id":True, "matrizSemana1":matrizSemana1, "matrizSemana2":matrizSemana2, "dias":dias })

    else:
        db=Database()
        movies=db.all_movies()
        rooms=db.all_rooms()

        fechaHoraActual = datetime.now()

        lunesAnterior = primerLunesAnterior(fechaHoraActual)
        lunesSiguiente = lunesAnterior + timedelta(days=7)
        matrizSemana1 = matriz_shows(lunesAnterior)
        matrizSemana2 = matriz_shows(lunesSiguiente)
        dias = catorceDias(lunesAnterior)

        return render(request, "form-show.html", {"movies":movies, "rooms":rooms, "user_id":True, "matrizSemana1":matrizSemana1, "matrizSemana2":matrizSemana2, "dias":dias })




def recibiendoPeliculaNueva(request):
    # if request.method == "POST":   anidar?

    titulo=request.POST.get("titulo")
    duracion=request.POST.get("duracion")
    calificacion=request.POST.get("calificacion")
    imagenLink=request.POST.get("imagenLink")
    idioma=request.POST.get("idioma")
    genero=request.POST.get("genero")
    resenia=request.POST.get("resenia")
    fechaEstreno=request.POST.get("date")


    db=Database()
    db.insert_movie(titulo, duracion, calificacion, imagenLink, idioma, genero, resenia, fechaEstreno)

    return render(request, "home.html")


####################### USUARIOS
def login(request):
    if request.method == "POST": #Si entra por POST
        email=request.POST.get("email")
        password=request.POST.get("password")

        db=Database()
        info=db.login(email, password)

        if info:
            request.session["user_id"] = info[0]
            return redirect("/")
        else:
            return render(request, "login.html")

    else: #Si entra por GET
        try:
            user_id = request.session["user_id"]
            return redirect("/")
        except:
            return render(request, "login.html")



def register(request):
    if request.method == "POST": #Si entra por POST
        usuario=request.POST.get("usuario")
        fecha_nacimiento=request.POST.get("fecha_nacimiento")
        email=request.POST.get("email")
        password=request.POST.get("password")

        db=Database()
        db.insert_user(usuario, fecha_nacimiento, email, password)

        return render(request, "login.html")

    else: #Si entra por GET
        return render(request, "register.html")



def cerrarsesion(request):
    del request.session['user_id']
    return redirect("/")


# def auth_required(request, **kwargs):
#     try:
#         funcion = kwargs["funcion"]
#         user_id = request.session["user_id"]
#         return funcion(request)

#     except:
#         return redirect("/login")



def auth_required_pro(request, **kwargs):

    auth = kwargs["auth"]

    match auth:
        case "user":
            try:
                user_id = request.session["user_id"]
                funcion = kwargs["funcion"]
                return funcion(request)
            except:
                return redirect("/login")

        case "admin":
                try:
                    db=Database()
                    info=db.isAdmin(request.session["user_id"])
                    if info:
                        funcion = kwargs["funcion"]
                        return funcion(request)
                    return redirect("/") #aca se podria hacer un HTML que diga que no tiene permisos
                except:
                    return redirect("/login")

        case "anybody":
            funcion = kwargs["funcion"]
            return funcion(request)

        case "anybodySimple":
            view = kwargs["view"]
            try:
                user_id = request.session["user_id"]
                return render(request, view, {"user_id":True})
            except:
                return render(request, view)

        case "notLogged":
            try:
                user_id = request.session["user_id"]
                return redirect("/")
            except:
                funcion = kwargs["funcion"]
                return funcion(request)


def adminView(request):
    return render(request, "admin-side-panel.html", {"user_id":True})

