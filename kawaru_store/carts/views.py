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
    cart.products.add(product) #Agregar el producto al carrito (relación muchos a muchos)
    
    return render(request, 'carts/add.html', {
        'product': product #enviar el producto al template
    }) 
    
def remove(request):
    get_object_or_404
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    
    cart.products.remove(product)
    
    return redirect('carts:cart')