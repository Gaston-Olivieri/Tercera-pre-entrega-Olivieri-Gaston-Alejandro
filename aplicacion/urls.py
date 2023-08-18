from django.urls import path, include
from .views import *

urlpatterns = [
    path('', inicio, name="inicio" ),
    path('carta_menú/', carta_menú, name="carta_menú" ),
    path('bebidas/', bebidas, name="bebidas" ),
    path('reservas/', reservas, name="reservas" ),
    path('contactos/', contactos, name="contactos" ),

    path('reservasform/', reservasForm, name="reservasform" ),

    path('buscarReserva/', buscarReserva, name="buscarReserva" ),
    path('buscar2/', buscar2, name="buscar2" ),
]