from django.db import models

# Create your models here.
class CustomerInfo(models.Model):
    cus_name=models.CharField(max_length=100,null=True,blank=True)
    cus_mobile=models.CharField(max_length=12,null=True,blank=True)
    order=models.CharField(max_length=100,null=True,blank=True)
    table_num=models.IntegerField()



    def __str__(self):
        return f"{self.cus_name} | {self.table_num}"
