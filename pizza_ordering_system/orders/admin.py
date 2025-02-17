from django.contrib import admin
from .models import PizzaSize, PizzaCrust, PizzaSauce, PizzaCheese, Topping, Pizza, Order

# Registering models to make them accessible in the Django admin panel
admin.site.register(PizzaSize)  # Register the PizzaSize model
admin.site.register(PizzaCrust)  # Register the PizzaCrust model
admin.site.register(PizzaSauce)  # Register the PizzaSauce model
admin.site.register(PizzaCheese)  # Register the PizzaCheese model
admin.site.register(Topping)  # Register the Topping model
admin.site.register(Pizza)  # Register the Pizza model, which combines the ingredients
admin.site.register(Order)  # Register the Order model, which tracks customer orders

