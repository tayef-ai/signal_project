from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.


class MyUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()
    
class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='profile', blank=True, null=True)
    

