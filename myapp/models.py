from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
COUNTRY=(('COL','Colombia'),('CA',"Canada"),('USA','Estados unidos'),('BRA','Brasil'))
ROLES=(('ADM','Admin'),('PRO','Professional'),('CST','Customer'))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(null=True,blank=True)
    country= models.CharField(max_length=10, choices=COUNTRY, default='COL')
    birthday = models.DateField(null=True,blank=True)
    profession = models.CharField(max_length=64,null=True,blank=True)
    mobile = models.CharField(max_length=64, null=True,blank=True)
    url = models.URLField(null=True,blank=True)
    role = models.CharField(max_length=10, choices=ROLES, default='CST')
    
"""
class User(models.Model):
    name = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    birthday = models.DateField()
    userName = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64) 
    email = models.EmailField(max_length=64, unique=True)
    date_joined = models.DateField(auto_now_add=True)  

    def __str__(self):
        return ( self.name  ,  self.userName , self.email)

  """  
