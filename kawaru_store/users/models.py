from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(User):
    proxy = True
    
    def get_products(self):
        return []
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #cascade para decir que cuando eliminemos un registro de algun usuario, también se elimine profile
    perfil = models.TextField()