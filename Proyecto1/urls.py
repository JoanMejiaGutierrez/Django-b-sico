"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from Proyecto1.views import Mostrar_Mi_Primer_Plantilla, calcularEdad, despedida, miHijo1, miHijo2, obtenerFecha, saludo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('nosveremos/', despedida),
    path('fecha/', obtenerFecha),
    path('edades/<int:ano>/<int:edad>', calcularEdad),#la url se le colocn los argumentos y debe especificar el tipo de dato a entero ya que por defecto se toma como cadena
    #a la hora de colocar la url se coloca por ejemplo edades/18/2021 nombre del endpoint, parametro edad y parametro año.
    path('plantilla/', Mostrar_Mi_Primer_Plantilla),
    path('hijo1/', miHijo1),
    path('hijo2/', miHijo2)
]