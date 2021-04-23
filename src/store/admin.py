from django.contrib import admin

# Register your models here.
from .models import Product, Cathegory, SubCathegory, Attribute

admin.site.register(Product)
admin.site.register(Cathegory)
admin.site.register(SubCathegory)
admin.site.register(Attribute)