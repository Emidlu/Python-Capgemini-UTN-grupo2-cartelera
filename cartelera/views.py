from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Database

# def home(request):
#     try:
#         user_id = request.session["user_id"]
#         return render(request, "home.html", {"user_id":True})
#     except:
#         return render(request, "home.html")


# def cartelera(request):
#     return render(request, "cartelera.html")


def agregar(request):
    db=Database()
    info=db.all_genres()

    return render(request, "form-movie.html", {"info":info, "user_id":True})



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

        case "none":
            funcion = kwargs["funcion"]
            return funcion(request)

        case "noneSimple":
            view = kwargs["view"]
            try:
                user_id = request.session["user_id"]
                return render(request, view, {"user_id":True})
            except:
                return render(request, view)
        

