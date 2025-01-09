from django.contrib import admin

from .models import Supplier, Stock
# Register your models here.
admin.site.register(Supplier)
admin.site.register(Stock)