from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=10,blank=True)
    gmail=models.EmailField(null=False,blank=True)
    uucms_num=models.CharField(max_length=15,blank=False,null=False)
    rno=models.IntegerField(null=False)
    photo=models.ImageField(upload_to='studentphoto/',null=True)

    def __str__(self):
        return f"{self.name} -{self.rno}"