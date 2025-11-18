from django.contrib import admin
from .models import CustomerInfo
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    ordering=('cus_name',)
    list_filter=('table_num',)
    search_fields=('cus_name','table_num')


admin.site.register(CustomerInfo,CustomerAdmin)