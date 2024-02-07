from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms  import *

# Create your views here.

def home(request):
    return render(request, "Flujos/home.html")


def ver_locales(request):
    contexto = {'locales': Locales.objects.all()}
    return render(request, "Flujos/locales.html", contexto)


def ver_productos(request):
    contexto = {'productos': Productos.objects.all()}
    return render(request, "Flujos/productos.html", contexto)


def ver_entregas(request):
    pass


def ver_repartidores(request):
    contexto = {'repartidores': Repartidor.objects.all()}
    return render(request, "Flujos/repartidores.html", contexto)


def localForm(request):
    if request.method == "POST":
        miForm = LocalesForm(request.POST)
        if miForm.is_valid():
            local_nombre = miForm.cleaned_data.get("nombre")
            local_ubicacion = miForm.cleaned_data.get("ubicacion")
            newLocal = Locales(nombre=local_nombre,ubicacion=local_ubicacion)
            newLocal.save()
            return render(request, "Flujos/home.html") 
    else:
        miForm = LocalesForm()

    return render(request, "Flujos/localForm.html", {"form": miForm}) 


def productoForm(request):
    if request.method == "POST":
        miForm = ProductosForm(request.POST)
        if miForm.is_valid():
            prod_nombre = miForm.cleaned_data.get("nombre")
            prod_umedida = miForm.cleaned_data.get("unidadMedida")
            prod_tipoprod = miForm.cleaned_data.get("tipoProducto")
            newProd = Productos(nombre=prod_nombre,unidadMedida=prod_umedida, tipoProducto = prod_tipoprod)
            newProd.save()
            return render(request, "Flujos/home.html") 
    else:
        miForm = ProductosForm()
    
    return render(request, "Flujos/productoForm.html", {"form": miForm}) 


def repartidorForm(request):
    if request.method == "POST":
        miForm = RepartidorForm(request.POST)
        if miForm.is_valid():
            rep_nombre = miForm.cleaned_data.get("nombre")
            rep_rut = miForm.cleaned_data.get("rut")
            rep_direccion = miForm.cleaned_data.get("direccion")
            newRep = Repartidor(nombre=rep_nombre,rut=rep_rut, direccion = rep_direccion)
            newRep.save()
            return render(request, "Flujos/home.html") 
    else:
        miForm = RepartidorForm()
    
    return render(request, "Flujos/repartidorForm.html", {"form": miForm}) 


def buscar(request):
    return render(request, "Flujos/buscar.html")


def buscarProd(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        prod = Productos.objects.filter(nombre__icontains=patron)
        contexto = {"productos": prod}
        return render(request, "Flujos/productos.html", contexto)
    return HttpResponse("No se ingresaron patrones de búsqueda")
