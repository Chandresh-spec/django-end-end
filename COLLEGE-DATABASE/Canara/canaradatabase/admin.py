from django.contrib import admin
from .models import student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=('name','rno','gmail')
    ordering=('rno',)
    search_fields=('rno','name')






admin.site.register(student,StudentAdmin)
