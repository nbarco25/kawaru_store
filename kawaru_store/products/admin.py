from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    fields = ('nombre', 'descripcion', 'precio', 'imagen') #campos que voy a mostrar en el formulario para crear productos en admin (slug no lo muestro porque lo voy a generar automáticamente a partir del nombre del producto con slugify)
    list_display = ('__str__','slug','creado_en') #con este atributo controlamos qué vemos en la página admin
admin.site.register(Product, ProductAdmin)