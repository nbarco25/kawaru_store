from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout #para generar la sesión
from django.contrib import messages
from .forms import RegisterForm

def index(request):
 
    return render(request,'index.html',{
        'titulo': 'Kawaru',
        'message': 'Listado de productos',
        'entero': 23,
        'booleano': True,
        'lista': [1,2,3,3,5,3],
        
        'productos': [
            {'titulo': 'Televisor', 'Precio': 2000000, 'stock': True}, #producto
            {'titulo': 'Carro', 'Precio': 12000000, 'stock': True },
            {'titulo': 'Computador', 'Precio': 800000, 'stock': False}
        ]
    })
    
def login_view(request):
    print(request.method) #Visualizar en consola el método por el cual se está haciendo la petición
    #Condicional para obtener la información que se envía en el login a través del método POST
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
    form = RegisterForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username') #diccionario
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        
        print(username)
        print(email)
        print(password)
    
    return render(request, 'users/register.html', {
        'form': form
    })