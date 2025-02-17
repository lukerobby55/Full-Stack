from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('create_pizza/', views.create_pizza, name='create_pizza'),
    path('order/<int:pizza_id>/', views.order_details, name='order_details'),
    path('order_complete/<int:order_id>/', views.order_complete, name='order_complete'),
    path('order_history/', views.order_history, name='order_history'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('order_again/<int:order_id>/', views.order_again, name='order_again'),
]
