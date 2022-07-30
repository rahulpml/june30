from django.contrib import admin
from .models import Fueltype, Fuel, Machine, Tanker , FuelService , Supplier ,Customer , Item ,Order, OrderItem ,ShippingAddress

# Register your models here.
admin.site.register(Fueltype)
admin.site.register(Fuel)
admin.site.register(Machine)
admin.site.register(Tanker)
admin.site.register(FuelService)
admin.site.register(Supplier)
admin.site.register(Customer)

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)