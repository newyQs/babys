from django.contrib import admin
from .models import *


# admin.site.register(CartInfo)
# admin.site.register(order_info)

@admin.register(CartInfo)
class CartInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'quantity']


@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'created', 'state']
    list_filter = ['state']
    date_hierarchy = 'created'
