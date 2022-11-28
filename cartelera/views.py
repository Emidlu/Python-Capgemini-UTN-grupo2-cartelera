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


def cartelera(request):

    try:
        user_id = request.session["user_id"]
        db=Database()
        fechaHoraActual = datetime.now()
        info=db.cartelera(fechaHoraActual)
        generos=db.all_genres()
    # print(info)
        return render(request, "cartelera.html", {"peliculas": info, "user_id":True, "generos":generos, "titulo":"Cartelera"})
    except:
        db=Database()
        fechaHoraActual = datetime.now()
        info=db.cartelera(fechaHoraActual)
        generos=db.all_genres()
        # print(info)
        return render(request, "cartelera.html", {"peliculas": info, "generos":generos, "titulo":"Cartelera"})


def compraEntrada(request):
        peliculaId=request.POST.get("peliculaId")

        db=Database()
        fechaActual = datetime.now()
        peliculaShows = db.movie_show_by_id(peliculaId, fechaActual)
        pelicula = db.movie_by_id(peliculaId)
        # print(peliculaShows)
        # print(pelicula)
        
        return render(request, "movie-show.html",{ "pelicula":pelicula, "user_id":True, "titulo": "Elegir Función", "shows":peliculaShows})




def estrenos(request):
    db=Database()
    fechaHoraActual = datetime.now()
    info=db.estrenos(fechaHoraActual)
    generos=db.all_genres()
    print(info)

    return render(request, "cartelera.html", {"peliculas": info, "user_id":True, "generos":generos, "titulo":"Próximos Estrenos"})


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
        matrizSemana1 = matriz_shows_semana(lunesAnterior)
        matrizSemana2 = matriz_shows_semana(lunesSiguiente)
        dias = proximosDias(lunesAnterior, 14)


        return render(request, "form-show.html", {"movies":movies, "rooms":rooms, "user_id":True, "matrizSemana1":matrizSemana1, "matrizSemana2":matrizSemana2, "dias":dias })

    else:
        db=Database()
        movies=db.all_movies()
        rooms=db.all_rooms()

        fechaHoraActual = datetime.now()

        lunesAnterior = primerLunesAnterior(fechaHoraActual)
        lunesSiguiente = lunesAnterior + timedelta(days=7)
        matrizSemana1 = matriz_shows_semana(lunesAnterior)
        matrizSemana2 = matriz_shows_semana(lunesSiguiente)
        dias = proximosDias(lunesAnterior, 14)

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







def elegirFuncion(request):
    if request.method == "POST":
        db=Database()
        show_id=request.POST.get("show_id")
        entradas = db.entradas_by_show_id(show_id)
        butacasOcupadas = []
        for i in range(100):
            butacasOcupadas.append(False)
        print(butacasOcupadas)
        for entrada in entradas:
            butacasOcupadas[entrada[3]-1] = True
        print(butacasOcupadas)

    return render(request, "compra.html", { "user_id":True, "butacasOcupadas":butacasOcupadas, "show_id":show_id})







def entrada(request):
    if request.method == "POST":
        db=Database()
        butacas=request.POST.get("butacas")
        show_id=request.POST.get("show_id")
        arr = butacas.replace('[', '').replace(']', '').split(',')
        show = db.show_by_id(show_id)
        sala_id = show[2]
        user_id = request.session["user_id"]

        for butaca in arr:
            db.crearEntrada(show_id, user_id, butaca, 600)

        return render(request, "compra.html", { "user_id":True})

    else:
        return render(request, "home.html", { "user_id":True})












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

