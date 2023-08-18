from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import ReservaForm
# Create your views here.

def inicio(request):
    return render(request, "aplicacion/inicio.html")

def carta_menú(request):
    contexto = {'carta_menú': Carta_Menú.objects.all() }
    return render(request, "aplicacion/carta_menú.html", contexto)

def bebidas(request):
    contexto = {'bebidas': Bebida.objects.all() }
    return render(request, "aplicacion/bebidas.html", contexto)

def reservas(request):
    contexto = {'reservas': Reserva.objects.all() }
    return render(request, "aplicacion/reservas.html", contexto)

def contactos(request):
    contexto = {'contactos': Contacto.objects.all() }
    return render(request, "aplicacion/contactos.html", contexto)


def reservasForm(request):
    if request.method == "POST":
        miForm = ReservaForm(request.POST)
        if miForm.is_valid():
            reserva_apellido = miForm.cleaned_data.get('apellido')
            reserva_nombre = miForm.cleaned_data.get('nombre')
            reserva_comensales = miForm.cleaned_data.get('comensales')
            reserva_observacion = miForm.cleaned_data.get('observacion')
            reserva = Reserva(apellido=reserva_apellido,
                              nombre=reserva_nombre,
                              comensales=reserva_comensales,
                              observacion=reserva_observacion)
            reserva.save()
            return render(request, "aplicacion/base.html")
            
    else:
         miForm = ReservaForm()

    return render(request, "aplicacion/reservasForm.html", {"form": miForm})

def buscarReserva(request):
    return render(request, "aplicacion/buscarReserva.html")

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        reservas = Reserva.objects.filter(apellido__icontains=patron)
        contexto = {"reservas":reservas}
        return render(request, "aplicacion/reservas.html", contexto)
    return HttpResponse("Debe ingresar una palabra")