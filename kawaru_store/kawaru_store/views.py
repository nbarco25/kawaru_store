from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout #para generar la sesión
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User
from products.models import Product

def base(request):
    return render(request,"base.html")


def index(request):
    
    lista_productos = Product.objects.all().order_by('-id') #obtengo la lista de productos ordenados del mas reciente al más antiguo, luego lo muestro en el template  index.html
    
    return render(request,'index.html',{
        'titulo': 'Kawaru',
        'message': 'Listado de productos',
        'productos': lista_productos #variable donde guardo la lista de los productos obtenidos y con la que voy a trabajar en el template index.html
    })
    
def login_view(request):
    print(request.method) #Visualizar en consola el método por el cual se está haciendo la petición
    #Condicional para obtener la información que se envía en el login a través del método POST
    
    if request.user.is_authenticated: #validamos que si el usuario ya está logueado no pueda acceder al login desde la url
        return redirect('index')
        
    
    if request.method == 'POST':
        username = request.POST.get('username') #diccionario
        password = request.POST.get('password') #El método get del diccionario si no encuentra nada retorna None
        
        #Autenticar a un usuario
        
        user = authenticate(username=username, password=password) #busca en la bd al usuario que tenga este usuario y contrasenia, si el usuario existe, retornará un objeto de tipo usuario, si no, retornará None
        
        if user:
            #Generar nueva sesión
            #Dos parámetros petición y usuario
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index') #funcion para redirigir al usuario despues de autenticarse (en este caso a index)
        else:
            messages.error(request, 'Usuario o contraseña no válidos')
        
        
        print(username)
        print(password)
        
    return render(request, 'users/login.html', {
        
    })
    
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente!')
    return redirect('login')

def register(request):
    
    if request.user.is_authenticated:
        return redirect('index') #validamos que no se pueda acceder al formulario registro desde la url si ya es un usuario logueado        
    
    form = RegisterForm(request.POST or None) #con los datos que el cliente envia o campos vacíos
    
    if request.method == 'POST' and form.is_valid(): #Si la petición es por método post y el formulario es válido
        #username = form.cleaned_data.get('username') #diccionario cleaned_data con el que podemos obtener el valor de los atributos del formulario
        #email = form.cleaned_data.get('email')
        #password = form.cleaned_data.get('password')
        
        #user = User.objects.create_user(username, email, password); #create user se encarga de encriptar el password!!!
        
        user = form.save();
        
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente!');
            return redirect('index')
    
    return render(request, 'users/register.html', {
        'form': form
    })