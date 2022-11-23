"""cartelera URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cartelera.views import *

urlpatterns = [

    # Auth tiene 3 opciones de string segun el nivel de acceso: 
    # user admin none noneSimple(sin funcion, solo muestra el html con el logueo)
    # view solo es requerido si se usa noneSimple
    path('', auth_required_pro, kwargs={'funcion': 'none', 'auth':'noneSimple' ,'view':'home.html'}),
    path('cartelera/', auth_required_pro, kwargs={'funcion': 'none', 'auth':'noneSimple' ,'view':'cartelera.html'}), #user admin none
    path('login/', login),
    path('movies/', recibiendoPeliculaNueva),
    path('cerrarsesion/', cerrarsesion),
    path('admin/agregar/', auth_required_pro, kwargs={'funcion': agregarPelicula, 'auth':'admin' ,'view':'none'}), #user admin none
    
    
    path('admin/agregar/funcion/', agregarFuncion),





    
]
