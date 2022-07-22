from django.contrib import admin

# Register your models here.
from applications.cart.models import Order

admin.site.register(Order)
