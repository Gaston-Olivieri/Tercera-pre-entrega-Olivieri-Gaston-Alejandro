from django import forms

class ReservaForm(forms.Form):
    apellido = forms.CharField(max_length=50, required=True)
    nombre = forms.CharField(max_length=50, required=True)
    comensales = forms.IntegerField(required=True)
    observacion = forms.CharField(max_length=250)
