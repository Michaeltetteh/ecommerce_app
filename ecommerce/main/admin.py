from django.contrib import admin
from .models import Product, ProductImage, ProductTag

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductTag)
