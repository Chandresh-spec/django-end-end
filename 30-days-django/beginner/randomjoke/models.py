from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=30,null=False)
    image=models.ImageField(upload_to='media/',null=True,blank=False)
    book_name=models.CharField(max_length=20,null=False)
    rate=models.IntegerField(blank=False)
    published_date=models.DateField(default=2)
































