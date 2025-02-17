from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings


# Custom manager for handling user creation
class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a regular user with the given email and password."""
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        extra_fields.setdefault("is_active", True)  # Default to active user
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Creates and saves a superuser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


# Custom user model with email as the unique identifier
class CustomUser(AbstractUser):
    username = None  # Remove username field
    email = models.EmailField(unique=True)  # Use email as the unique identifier

    USERNAME_FIELD = 'email'  # Login using email instead of username
    REQUIRED_FIELDS = []  # No extra required fields

    objects = CustomUserManager()  # Use the custom user manager

    def __str__(self):
        return self.email  # Return email as string representation


# Models for pizza components
class PizzaSize(models.Model):
    name = models.CharField(max_length=20)  # Pizza size name (Small, Medium, Large)

    def __str__(self):
        return self.name


class PizzaCrust(models.Model):
    name = models.CharField(max_length=20)  # Crust type (Thin, Thick, Stuffed)

    def __str__(self):
        return self.name


class PizzaSauce(models.Model):
    name = models.CharField(max_length=20)  # Sauce type (Tomato, BBQ, Alfredo)

    def __str__(self):
        return self.name


class PizzaCheese(models.Model):
    name = models.CharField(max_length=20)  # Cheese type (Mozzarella, Cheddar, Vegan)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=20)  # Topping name (Pepperoni, Mushrooms, Olives)

    def __str__(self):
        return self.name


# Model for creating custom pizzas
class Pizza(models.Model):
    size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE)  # Link to size
    crust = models.ForeignKey(PizzaCrust, on_delete=models.CASCADE)  # Link to crust
    sauce = models.ForeignKey(PizzaSauce, on_delete=models.CASCADE)  # Link to sauce
    cheese = models.ForeignKey(PizzaCheese, on_delete=models.CASCADE)  # Link to cheese
    toppings = models.ManyToManyField(Topping)  # Many toppings per pizza

    def __str__(self):
        return f"{self.size.name} Pizza with {self.cheese.name} Cheese"


# Model for customer orders
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Link to user
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)  # Ordered pizza
    name = models.CharField(max_length=100)  # Customer name
    address = models.TextField()  # Delivery address
    card_number = models.CharField(max_length=16)  # Payment card number
    card_expiry = models.CharField(max_length=7)  # Expiry date (MM/YYYY)
    card_cvv = models.CharField(max_length=3)  # Security code
    timestamp = models.DateTimeField(auto_now_add=True)  # Order time

    def __str__(self):
        return f"Order {self.id} by {self.user.email}"  # Order representation

