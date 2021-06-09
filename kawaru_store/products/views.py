from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product
from django.views.generic.detail import DetailView
from django.db.models import Q #aplicar consulta con dif filtros

class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['message'] = 'Lista de productos'
        print(context) 
        #context['productos'] = context['product_list']
        return context

class ProductDetailView(DetailView): #Busqueda por id que es la pk
    #La clase DetailView obtiene un objeto a partir de un identificador unico por default del pk
    #el id lo obtiene a partir de path('<pk>', views.ProductDetailView.as_view(), name='product') en urls.py de #products
    model = Product
    template_name = 'products/product.html' #envía el objeto al template
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        print(context) #aqui encontraremos la llave product que vamos a usar en el template
        return context
    
class ProductSearchListView(ListView):
    template_name = 'products/search.html'
    
    def get_queryset(self):
        
        filters = Q(nombre__icontains=self.query()) | Q(category__nombre__icontains=self.query())
        #SELECT * FROM products WHERE nombre like 'lo_que_escriban'
        return Product.objects.filter(filters) #Consulta para buscar el producto 
    
    def query(self):
        return self.request.GET.get('q')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['query'] = self.query()
        context['count'] = context['product_list'].count()
        print(context) #aqui encontraremos la llave product que vamos a usar en el template
        return context
    
