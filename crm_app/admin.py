from django.contrib import admin
from .models import Order, OrderStatus, OrderComment

admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(OrderComment)
