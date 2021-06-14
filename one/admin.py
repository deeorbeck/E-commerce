from django.contrib import admin
from .models import Category, product,incart
# Register your models here.
admin.site.register(Category)
admin.site.register(product)
admin.site.register(incart)