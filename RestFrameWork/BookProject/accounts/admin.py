from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

# Register your models here.



class CustomUserAdmin(UserAdmin):
    model=CustomUser
    fieldsets=UserAdmin.fieldsets+(
        ('additional info',{'fields':('phone_number','role')}),
    )



admin.site.register(CustomUser,CustomUserAdmin)