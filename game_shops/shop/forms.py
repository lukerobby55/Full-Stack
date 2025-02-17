from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    """
    A form for adding or editing Game instances.
    Uses Django's ModelForm to automatically generate fields based on the Game model.
    """

    class Meta:
        model = Game  # Specifies the model associated with the form
        fields = ['name', 'description', 'platform', 'genre', 'price', 'stock']  
        # Specifies which fields from the Game model should be included in the form
