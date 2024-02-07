from django import forms

class LocalesForm(forms.Form):
    nombre = forms.CharField(max_length = 50, required=True)
    ubicacion = forms.CharField(max_length = 50, required=True)


class ProductosForm(forms.Form):
    nombre = forms.CharField(max_length = 50, required=True)
    unidadMedida = forms.CharField(max_length = 50, required=True, label="Unidad de Medida")   
    tipoProducto = forms.CharField(max_length = 50, required=True, label= "Tipo de Producto")  


class RepartidorForm(forms.Form):
    nombre = forms.CharField(max_length = 50, required=True)
    rut = forms.CharField(max_length = 50, required=True, label="RUT")   
    direccion = forms.CharField(max_length = 50, required=True, label= "Dirección")      
