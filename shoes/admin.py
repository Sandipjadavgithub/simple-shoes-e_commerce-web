from django.contrib import admin
from .models import Shoes



class ShoesAdmin(admin.ModelAdmin):
    list_display=("name","price","quantity","image")



admin.site.register(Shoes,ShoesAdmin)