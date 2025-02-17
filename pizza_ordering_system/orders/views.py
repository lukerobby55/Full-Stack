from django.shortcuts import render, redirect, get_object_or_404
from .models import Pizza, Order, CustomUser
from .forms import PizzaForm, OrderForm, SignupForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

# Home page view
def home(request):
    return render(request, 'orders/home.html')

# View to create a pizza (only accessible if logged in)
@login_required
def create_pizza(request):
    if request.method == 'POST':  # If form is submitted
        form = PizzaForm(request.POST)
        if form.is_valid():  # Validate form data
            pizza = form.save()  # Save pizza instance
            return redirect('order_details', pizza_id=pizza.id)  # Redirect to order details
    else:
        form = PizzaForm()  # Render empty form
    return render(request, 'orders/create_pizza.html', {'form': form})

# View to create an order for a specific pizza
@login_required
def order_details(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)  # Retrieve pizza or return 404
    if request.method == 'POST':  # If form is submitted
        form = OrderForm(request.POST)
        if form.is_valid():  # Validate form data
            order = form.save(commit=False)  # Create order instance but don’t save yet
            order.pizza = pizza  # Link order to pizza
            order.user = request.user  # Assign order to logged-in user
            order.save()  # Save order
            return redirect('order_complete', order_id=order.id)  # Redirect to order complete page
    else:
        form = OrderForm()  # Render empty form
    return render(request, 'orders/order_details.html', {'form': form, 'pizza': pizza})

# View to show order completion details
@login_required
def order_complete(request, order_id):
    order = get_object_or_404(Order, id=order_id)  # Retrieve order or return 404
    
    order_time = order.timestamp  # Get the timestamp of the order
    current_minute = order_time.minute  # Get the minutes part of the timestamp

    # Determine estimated delivery time
    if current_minute <= 15:
        delivery_start = order_time.replace(minute=45, second=0, microsecond=0)
        delivery_end = delivery_start + timedelta(minutes=15)
    else:
        delivery_start = order_time + timedelta(hours=1)
        delivery_start = delivery_start.replace(minute=0, second=0, microsecond=0)
        delivery_end = delivery_start + timedelta(minutes=45)

    # Ensure delivery time doesn’t go past midnight
    if delivery_end.hour >= 24:
        delivery_end = delivery_end.replace(hour=0)

    # Format delivery window as a readable string
    delivery_window = f"{delivery_start.strftime('%I:%M %p')} - {delivery_end.strftime('%I:%M %p')}"

    return render(request, 'orders/order_complete.html', {'order': order, 'delivery_window': delivery_window})

# View to display the order history of a logged-in user
@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-id')  # Get all orders for the user
    return render(request, 'orders/order_history.html', {'orders': orders})

# View to reorder a previous order
@login_required
def order_again(request, order_id):
    previous_order = get_object_or_404(Order, id=order_id, user=request.user)  # Retrieve previous order

    # Create a new pizza with the same attributes as the previous order
    new_pizza = Pizza.objects.create(
        size=previous_order.pizza.size,
        sauce=previous_order.pizza.sauce,
        cheese=previous_order.pizza.cheese,
        crust=previous_order.pizza.crust,
    )
    new_pizza.toppings.set(previous_order.pizza.toppings.all())  # Copy toppings
    new_pizza.save()  # Save the new pizza

    return redirect('order_details', pizza_id=new_pizza.id)  # Redirect to order details

# User signup view
def signup(request):
    if request.user.is_authenticated:
        return redirect('order_history')  # Redirect authenticated users to order history

    if request.method == 'POST':  # If form is submitted
        form = SignupForm(request.POST)
        if form.is_valid():  # Validate form data
            user = form.save(commit=False)
            user.save()  # Save new user
            login(request, user)  # Log the user in
            return redirect('order_history')  # Redirect to order history
    else:
        form = SignupForm()  # Render empty form

    return render(request, 'orders/signup.html', {'form': form})

# User logout view
def logout_view(request):
    logout(request)  # Log out the user
    return redirect('home')  # Redirect to home page

# User login view
def login_view(request):
    if request.method == "POST":  # If form is submitted
        form = LoginForm(request, data=request.POST)
        if form.is_valid():  # Validate form data
            email = form.cleaned_data.get("username")  # Get email from form
            password = form.cleaned_data.get("password")  # Get password from form
            user = authenticate(request, email=email, password=password)  # Authenticate user
            if user is not None:
                login(request, user)  # Log the user in
                return redirect("home")  # Redirect to home page
    else:
        form = LoginForm()  # Render empty form

    return render(request, "orders/login.html", {"form": form})
