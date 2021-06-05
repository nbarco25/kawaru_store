from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html',{
        'titulo': 'Kawaru',
        'message': 'Listado de productos',
        'entero': 23,
        'booleano': True,
        'lista': [1,2,3,3,5,3],
        
        'productos': [
            {'titulo': 'Televisor', 'Precio': 2000000, 'stock': True}, #producto
            {'titulo': 'Carro', 'Precio': 12000000, 'stock': True },
            {'titulo': 'Computador', 'Precio': 800000, 'stock': False}
        ]
    })