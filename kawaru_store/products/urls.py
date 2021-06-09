from django.urls import path
from . import views

app_name = 'products' #Todas las rutas definidas aqui van a ser de la aplicación products para evitar conflictos entre nombre de rutas

urlpatterns = [
    path('search', views.ProductSearchListView.as_view(), name='search'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product'), #Definimos la ruta en la que va a buscar por el campo slug que será de tipo slug en la url

    #path('<pk>', views.ProductDetailView.as_view(), name='product') #id = pk ruta para definir una ruta /id de algun producto
]