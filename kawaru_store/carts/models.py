import uuid
from django.db import models
from users.models import User
from products.models import Product
from django.db.models.signals import pre_save, m2m_changed

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    #un usuario puede tener muchos carritos, pero un carrito puede o no pertenecer a un usuario 
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    #Un producto puede encontrarse en muchos carritos y un carrito de compras puede tener muchos productos
    products = models.ManyToManyField(Product)
    subtotal = models.DecimalField(default=0.0, max_digits=10, decimal_places=2) #suma de todos los precios de los productos
    total = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    creado_em = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.cart_id
    
def set_cart_id(sender, instance, *args, **kwargs): #callback
    if not instance.cart_id: #Si el carrito no posee un id unico
        instance.cart_id = str(uuid.uuid4())

def actualizar_total(sender, instance, action, *args, **kwargs):
    

pre_save.connect(set_cart_id, sender=Cart)    
    