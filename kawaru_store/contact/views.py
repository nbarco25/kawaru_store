# from django.forms.widgets import EmailInput
# from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import html
from .forms import *
from django.core.mail import EmailMessage

# Create your views here.
def send_email(email):
    pass

def ContactViews(request):
    informacion_valida = False
    if request.method == 'POST':
        formulario = formulario_contacto(request.POST)       
        if formulario.is_valid():
            informacion_valida = True
            asunto = formulario.cleaned_data['asunto']
            mensaje = formulario.cleaned_data['mensaje']
            correo = formulario.cleaned_data['correo']
            corre = EmailMessage(subject=asunto,body=mensaje,cc=[correo])
            corre.send()
            # return HttpResponseRedirect('/contacto')
    else:
        formulario = formulario_contacto()
    return render(request,'contact.html',locals())
