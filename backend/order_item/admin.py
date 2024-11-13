from django.contrib import admin
from .models import OrderItem

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'subtotal', 'product', 'order')