from django.shortcuts import get_object_or_404, redirect, render
from .models import Cart
from .utils import get_or_create_cart
from products.models import Product

# Create your views here.

def cart(request):
    cart = get_or_create_cart(request) #obtenemos el carrito pasando la petición como paràmetro a la funcion en utils
    return render(request, 'carts/cart.html', {
        'cart': cart #enviar el carrito al template
    })
    
def add(request):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id')) #obtener el producto del formulario
    #obtener la cantidad 'cantidad' es el name que le pusimos al input en el snippet add.hmtl
    cantidad = request.POST.get('cantidad', 1) #si la llave no existe el valor por default es 1
    
    cart.products.add(product, through_defaults={
            'cantidad': cantidad #'atributo': valor
        }) #Agregar el producto al carrito (relación muchos a muchos)
    
    return render(request, 'carts/add.html', {
        'product': product #enviar el producto al template
    }) 
    
def remove(request):
    get_object_or_404
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    
    cart.products.remove(product)
    
    return redirect('carts:cart')