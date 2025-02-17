# Importing the necessary modules from Django
from django.urls import path  # path function is used to define URL patterns
from . import views  # Import views from the current app

# Define URL patterns for the pizza ordering system
urlpatterns = [
    path('', views.home, name='home'),  # Homepage route

    path('signup/', views.signup, name='signup'),  # User registration page

    path('create_pizza/', views.create_pizza, name='create_pizza'),  # Page to create a new pizza order

    path('order/<int:pizza_id>/', views.order_details, name='order_details'),  
    # View details of a specific pizza order, identified by its ID

    path('order_complete/<int:order_id>/', views.order_complete, name='order_complete'),  
    # Mark an order as complete, identified by its order ID

    path('order_history/', views.order_history, name='order_history'),  
    # View the history of all past orders for the user

    path('login/', views.login_view, name='login'),  # User login page

    path('logout/', views.logout_view, name='logout'),  # User logout function

    path('order_again/<int:order_id>/', views.order_again, name='order_again'),  
    # Reorder a previously completed order using its order ID
]

