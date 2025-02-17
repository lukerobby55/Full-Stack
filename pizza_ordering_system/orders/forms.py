from django import forms
from .models import Order, Pizza, CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import re

# Form for selecting pizza options
class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza  # Uses the Pizza model
        fields = ['size', 'crust', 'sauce', 'cheese', 'toppings']  # Fields for pizza customization
        widgets = {
            'toppings': forms.CheckboxSelectMultiple(),  # Allows multiple toppings selection via checkboxes
        }

# Form for placing an order
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order  # Uses the Order model
        fields = ['name', 'address', 'card_number', 'card_expiry', 'card_cvv']  # Fields for order details
        widgets = {
            'card_expiry': forms.TextInput(attrs={'placeholder': 'MM/YY', 'class': 'form-control'}),  # Formatting for card expiry field
        }

    def clean_card_expiry(self):
        """ Validates the expiry date format as MM/YY """
        card_expiry = self.cleaned_data.get('card_expiry')
        if not re.match(r'^(0[1-9]|1[0-2])/\d{2}$', card_expiry):
            raise forms.ValidationError("Expiry date must be in MM/YY format.")
        return card_expiry

# Form for user registration
class SignupForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, 
        required=True, 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )

    class Meta:
        model = CustomUser  # Uses the CustomUser model
        fields = ['email', 'password1', 'password2']  # Fields for signup

    def clean_email(self):
        """ Validates that the email is unique """
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email
    
# Form for user login
class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
