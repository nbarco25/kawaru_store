from django.db import models

class Product(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0.0) #decimal_places (cuantos dígitos despues de la , voy a usar)
    creado_en = models.DateTimeField(auto_now_add=True) #para que se tome la fecha y hora exacta de creación desde el sist
    