from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product
from django.views.generic.detail import DetailView
from django.db.models import Q #aplicar consulta con dif filtros
from django.views.generic.edit import CreateView #Crear un nuevo producto
from django.urls import reverse_lazy

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
        
        filters = (Q(nombre__contains=self.query()) | Q(category__nombre__contains=self.query()))
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

# def product_add_view (request):
	# u = User.objects.get(id = request.user.id)
    # p = None
	# if request.method == 'POST':
		# form = product_add_for(request.POST, request.FILES)
		# if form.is_valid():
			# p = form.save(commit=False)
			# p.usuario = u
			# p.save()
			# messages.success(request, 'Muestra agregada satisfactoriamente')	
	# form = product_add_form()
	# return render (request, 'product_add.html', locals())


class ProductCreateView(CreateView):
    model  =  Product
    fields = ['nombre','descripcion','precio','imagen','cantidad','estado','usuario']
    success_url = reverse_lazy('index')
    
# 
# 
    # def get_initial(self, request, *args, **kwargs):
        # 
        # u = User.objects.get(id  =request.user.id)
        # initial = super(ProductCreateView, self).get_initial(**kwargs)
        # initial['usuario'] = u
        # return initial
