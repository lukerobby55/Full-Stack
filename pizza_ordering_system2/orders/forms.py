from django import forms
from .models import Order, Pizza, CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import re

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['size', 'crust', 'sauce', 'cheese', 'toppings']
        widgets = {
            'toppings': forms.CheckboxSelectMultiple(),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'address', 'card_number', 'card_expiry', 'card_cvv']
        widgets = {
            'card_expiry': forms.TextInput(attrs={'placeholder': 'MM/YY', 'class': 'form-control'}),
        }

    def clean_card_expiry(self):
        card_expiry = self.cleaned_data.get('card_expiry')
        if not re.match(r'^(0[1-9]|1[0-2])/\d{2}$', card_expiry):
            raise forms.ValidationError("Expiry date must be in MM/YY format.")
        return card_expiry

class SignupForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, 
        required=True, 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email
    
class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
