from django.db import models
from products.models import Product

class Category(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    products = models.ManyToManyField(Product, blank=True)
    creado_en = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.nombre