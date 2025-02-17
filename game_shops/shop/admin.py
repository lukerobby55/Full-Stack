from django.contrib import admin
from .models import Game

@admin.register(Game)  # Registers the Game model with the Django admin panel
class GameAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Game model.
    """

    list_display = ('name', 'platform', 'genre', 'price', 'stock')  
    # Displays these fields as columns in the admin list view

    search_fields = ('name', 'platform', 'genre')  
    # Enables search functionality for name, platform, and genre fields
