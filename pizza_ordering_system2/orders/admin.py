from django.contrib import admin
from .models import PizzaSize, PizzaCrust, PizzaSauce, PizzaCheese, Topping, Pizza, Order

admin.site.register(PizzaSize)
admin.site.register(PizzaCrust)
admin.site.register(PizzaSauce)
admin.site.register(PizzaCheese)
admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Order)
