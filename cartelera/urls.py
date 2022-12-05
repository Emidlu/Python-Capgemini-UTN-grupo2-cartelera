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
from .views import * 

urlpatterns = [

    # Auth tiene 3 opciones de string segun el nivel de acceso: 
    # user admin anybody anybodySimple(sin funcion, solo muestra el html con el logueo) notLogged
    # view solo es requerido si se usa anybodySimple
    path('', auth_required_pro, kwargs={'funcion': 'none', 'auth':'anybodySimple' ,'view':'home.html'}),


# PROCESO DE COMPRA
    path('cartelera/', auth_required_pro, kwargs={'funcion': cartelera, 'auth':'anybody' ,'view':'none'}),
    path('estrenos/', auth_required_pro, kwargs={'funcion': estrenos, 'auth':'anybody' ,'view':'none'}),

    path('funcion/funciones/', auth_required_pro, kwargs={'funcion': mostrarFunciones, 'auth':'user' ,'view':'none'}),
    path('funcion/butacas/', auth_required_pro, kwargs={'funcion': mostrarButacas, 'auth':'user' ,'view':'none'}),
    path('entradas/', auth_required_pro, kwargs={'funcion': entrada, 'auth':'user' ,'view':'none'}),
    # path('funcion/butacas/', mostrarButacas),
    # path('entradas/', entrada),

# RUTAS DE USUARIO
    path('login/', auth_required_pro, kwargs={'funcion': login, 'auth':'notLogged' ,'view':'none'}),
    path('register/', auth_required_pro, kwargs={'funcion': register, 'auth':'notLogged' ,'view':'none'}),
    path('user/', auth_required_pro, kwargs={'funcion': userEdit, 'auth':'user' ,'view':'none'}),
    path('user/delete/', auth_required_pro, kwargs={'funcion': userDelete, 'auth':'user' ,'view':'none'}),

    path('cerrarsesion/', cerrarsesion),


# RUTAS DE ADMIN
    path('admin/', auth_required_pro, kwargs={'funcion': adminView, 'auth':'admin' ,'view':'none'}),
    path('admin/agregar/pelicula/', auth_required_pro, kwargs={'funcion': agregarPelicula, 'auth':'admin' ,'view':'none'}),
    path('admin/agregar/funcion/', auth_required_pro, kwargs={'funcion': agregarFuncion, 'auth':'admin' ,'view':'none'}),
    path('movies/', auth_required_pro, kwargs={'funcion': recibiendoPeliculaNueva, 'auth':'admin' ,'view':'none'}),
    # path('movies/', recibiendoPeliculaNueva),
    
    path('admin/seleccionar/pelicula/',auth_required_pro, kwargs={'funcion': seleccionarPelicula, 'auth':'admin' ,'view':'none'} ),
    path('admin/editar/pelicula/', auth_required_pro, kwargs={'funcion': seleccionarPelicula, 'auth':'admin' ,'view':'none'} ),
    path('admin/editando/pelicula/', auth_required_pro, kwargs={'funcion': editandoPelicula, 'auth':'admin' ,'view':'none'} ),
    path('admin/eliminar/pelicula/', auth_required_pro, kwargs={'funcion': eliminarPelicula, 'auth':'admin' ,'view':'none'} ),
    #path('admin/editar/funcion/', editarFuncion),
    path('admin/eliminar/funcion/', eliminarFuncion),
    path('admin/editar/funcion/', seleccionarFuncion),
    path('admin/editando/funcion/', editandoFuncion)
]
