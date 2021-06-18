import uuid
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save


class Product(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0) #decimal_places (cuantos dígitos despues de la , voy a usar)
    imagen = models.ImageField(upload_to='products/', null=False, blank=False)
    slug = models.SlugField(null=False, blank=False, unique=True)
    creado_en = models.DateTimeField(auto_now_add=True) #para que se tome la fecha y hora exacta de creación desde el sist
    
    #def save(self, *args, **kwargs):
    #    self.slug = slugify(self.nombre)
    #    super(Product, self).save(*args, **kwargs)
    
    def __str__(self): #para mostrar el nombre del producto y no el objeto
        return self.nombre
    
def set_slug(sender, instance, *args, **kwargs): #callback
    if instance.nombre and not instance.slug:
        slug = slugify(instance.nombre)

        while Product.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.nombre, str(uuid.uuid4())[:4])
            )
        instance.slug = slug
                
pre_save.connect(set_slug, sender=Product)
    
    
