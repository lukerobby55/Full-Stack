from django.shortcuts import render, redirect, get_object_or_404
from .models import Pizza, Order, CustomUser
from .forms import PizzaForm, OrderForm, SignupForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

def home(request):
    return render(request, 'orders/home.html')

@login_required
def create_pizza(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save()
            return redirect('order_details', pizza_id=pizza.id)
    else:
        form = PizzaForm()
    return render(request, 'orders/create_pizza.html', {'form': form})

@login_required
def order_details(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.pizza = pizza
            order.user = request.user
            order.save()
            return redirect('order_complete', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'orders/order_details.html', {'form': form, 'pizza': pizza})

@login_required
def order_complete(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    order_time = order.timestamp
    current_minute = order_time.minute

    if current_minute <= 15:
        delivery_start = order_time.replace(minute=45, second=0, microsecond=0)
        delivery_end = delivery_start + timedelta(minutes=15)
    else:
        delivery_start = order_time + timedelta(hours=1)
        delivery_start = delivery_start.replace(minute=0, second=0, microsecond=0)
        delivery_end = delivery_start + timedelta(minutes=45)

    if delivery_end.hour >= 24:
        delivery_end = delivery_end.replace(hour=0)

    delivery_window = f"{delivery_start.strftime('%I:%M %p')} - {delivery_end.strftime('%I:%M %p')}"

    return render(request, 'orders/order_complete.html', {'order': order, 'delivery_window': delivery_window})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-id')
    return render(request, 'orders/order_history.html', {'orders': orders})

@login_required
def order_again(request, order_id):
    previous_order = get_object_or_404(Order, id=order_id, user=request.user)

    new_pizza = Pizza.objects.create(
        size=previous_order.pizza.size,
        sauce=previous_order.pizza.sauce,
        cheese=previous_order.pizza.cheese,
        crust=previous_order.pizza.crust,
    )
    new_pizza.toppings.set(previous_order.pizza.toppings.all())
    new_pizza.save()

    return redirect('order_details', pizza_id=new_pizza.id)

def signup(request):
    if request.user.is_authenticated:
        return redirect('order_history')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('order_history')
    else:
        form = SignupForm()

    return render(request, 'orders/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username") 
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()

    return render(request, "orders/login.html", {"form": form})
