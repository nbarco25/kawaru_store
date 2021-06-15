import uuid
from django.db import models
from users.models import User
from products.models import Product
from django.db.models.signals import pre_save, m2m_changed
import decimal

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    #un usuario puede tener muchos carritos, pero un carrito puede o no pertenecer a un usuario 
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    #Un producto puede encontrarse en muchos carritos y un carrito de compras puede tener muchos productos
    products = models.ManyToManyField(Product, through='CartProducts') #con through hago la relacion entre productos y carrito de compras, a través del modelo CartProducts
    subtotal = models.DecimalField(default=0.0, max_digits=10, decimal_places=2) #suma de todos los precios de los productos
    total = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    creado_em = models.DateTimeField(auto_now_add=True)
    
    COMISION = 0.05 #0.5%
    
    def __str__(self):
        return self.cart_id
    
    def actualizar_total_subtotal(self):
        self.actualizar_subtotal()
        self.actualizar_total()
        
    def actualizar_subtotal(self):
        #El subtotal es la suma del precio de todos los productos
        self.subtotal = sum([product.precio for product in self.products.all()])
        self.save()
        
    def actualizar_total(self):
        self.total = self.subtotal + (self.subtotal * decimal.Decimal(Cart.COMISION))
        self.save()
    
    def productos_relacionados(self):
        return self.cartproducts_set.select_related('products') #Con esta linea estamos obteniendo todos los objetos cartproduct y también todos los objetos product
    
class CartProducts(models.Model):
    #definimos la relacion entre un producto y un carrito
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE) #un carrito puede tener muchos cart products
    products = models.ForeignKey(Product, on_delete=models.CASCADE) #un producto puede tener muchos cart products
    cantidad = models.IntegerField(default=1)
    creado_en = models.DateTimeField(auto_now_add=True)
           
def set_cart_id(sender, instance, *args, **kwargs): #callback
    if not instance.cart_id: #Si el carrito no posee un id unico
        instance.cart_id = str(uuid.uuid4())

def actualizar_total_subtotal(sender, instance, action, *args, **kwargs):
    #postadd despues de que un producto se agrega al carrito de compras
    #postremove después de que un producto se elimina del carrito de compras
    #postclear después de que el carrito de compras se limpia
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        instance.actualizar_total_subtotal() #calcular total y subtotal
        
    


pre_save.connect(set_cart_id, sender=Cart)    
m2m_changed.connect(actualizar_total_subtotal,sender=Cart.products.through) #callback para mostrar la cantidad de un sólo producto agregado a un carrito.