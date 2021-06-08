from django.contrib import admin
from django.urls import path
from products.views import ProductListView
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('usuarios/login', views.login_view, name='login'),
    path('usuarios/logout', views.logout_view, name='logout'),
    path('usuarios/registro', views.register, name='register'),
    path('admin/', admin.site.urls),
    path('productos/', include('products.urls')) #productos/id_producto
]

if settings.DEBUG: #condicion para mostrar imágenes en los templates
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
