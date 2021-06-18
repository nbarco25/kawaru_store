from .models import Cart
def get_or_create_cart(request):
    user = request.user if request.user.is_authenticated else None
        
    #Tratamos de obtener el carrito filrtando por su id_cart
    
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.filter(cart_id=cart_id).first() #si el carrito no está, esto retorna None
    
    if cart is None: #si el carrito no existe entonces lo creamos
        cart = Cart.objects.create(user=user)
    
    if user and cart.user is None:
        #Si el usuario si existe Y el carrito creado NO tiene usuario asignado entonces
        #asignamos ese usario al usuario del carrito
        #Guardamos en la bd
        cart.user = user 
        cart.save()
    
      #Aquí obtengo el usuario autenticado si lo está
    #cart_id = request.session.get('cart_id')
    #if cart_id: #si la sesion 'cart_id' está en la petición
        #Obtenemos el carrito
        #cart = Cart.objects.get(cart_id=cart_id)
    #else: #si no
        #Creamos un nuevo carrito que puede o no pertenecerle a un usuario según nuestro modelo
        #cart = Cart.objects.create(user=user)
    request.session['cart_id']=cart.cart_id
    return cart