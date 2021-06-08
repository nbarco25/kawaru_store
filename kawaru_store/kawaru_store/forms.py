from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(required=True, 
                               min_length=4, max_length=50,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'id': 'username',
                                   'placeholder': 'nombre de usuario'
                               }))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'id': 'email',
                                 'placeholder': 'example@gmail.com' 
                             }))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'id': 'password',
                                   'placeholder': 'contraseña'
                               }))
    password2 = forms.CharField(label='Confirmar contraseña',
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'id': 'password',
                                }))
    
    def clean_username(self):
        username = self.cleaned_data.get('username') #obtenemos la información del input
        
        if User.objects.filter(username=username).exists(): #validamos si ya existe el valor del campo ingresado
            raise forms.ValidationError('El nombre de usuario ya se encuentra en uso') #Si existe, enviamos un error y mostramos en el template
        return username #si no existe error retornamos el valor del campo
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya se encuentra en uso')
        return email
    
    def clean(self): #método para válidar campos que dependan de ser iguales a otros
        cleaned_data = super().clean() #obtener la información del formulario con el metodo clean de la clase padre 
        
        if cleaned_data.get('password') != cleaned_data.get('password2'):
            self.add_error('password2', 'Las contraseñas no coinciden!')
        
    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password')
        )
    
    
    