from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.




class CustomUser(AbstractUser):
    phone_number=models.CharField(max_length=11,null=True,blank=True)
    role=models.CharField(max_length=100,null=True,blank=True)