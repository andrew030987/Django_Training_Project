from django.contrib import admin
from .models import Order, OrderStatus, OrderComment

class OrderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(OrderComment)
