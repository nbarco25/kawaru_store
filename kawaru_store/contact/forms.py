from django import forms
from django.forms.forms import Form

#Formulario de contacto 
class formulario_contacto(forms.Form):
    correo  = forms.EmailField()
    asunto  = forms.CharField(max_length=100)
    mensaje = forms.CharField()
