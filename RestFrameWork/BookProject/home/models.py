from django.db import models

# Create your models here.
class Books(models.Model):
    book_name=models.CharField(max_length=50,blank=True)
    book_author=models.CharField(max_length=400,blank=True)
    book_price=models.CharField(max_length=100,null=True,blank=True)