from django.urls import path
from . import views

urlpatterns = [
    path('<pk>', views.ProductDetailView.as_view(), name='product') #id = pk ruta para definir una ruta /id de algun producto
]