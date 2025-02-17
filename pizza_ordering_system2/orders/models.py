from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        extra_fields.setdefault("is_active", True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)  

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  

    objects = CustomUserManager()  

    def __str__(self):
        return self.email  


class PizzaSize(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class PizzaCrust(models.Model):
    name = models.CharField(max_length=20) 

    def __str__(self):
        return self.name


class PizzaSauce(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class PizzaCheese(models.Model):
    name = models.CharField(max_length=20)  

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=20)  

    def __str__(self):
        return self.name


class Pizza(models.Model):
    size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE)
    crust = models.ForeignKey(PizzaCrust, on_delete=models.CASCADE)
    sauce = models.ForeignKey(PizzaSauce, on_delete=models.CASCADE)
    cheese = models.ForeignKey(PizzaCheese, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return f"{self.size.name} Pizza with {self.cheese.name} Cheese"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    card_number = models.CharField(max_length=16)
    card_expiry = models.CharField(max_length=7)
    card_cvv = models.CharField(max_length=3)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.email}"
