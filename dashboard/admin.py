from django.contrib import admin
from .models import Product, Order

admin.site.site_header = 'Admin Panel'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'staff')


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
