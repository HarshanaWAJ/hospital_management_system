from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home" ),
    path('login/', views.login, name = "login"),
    path('register/', views.register, name = "register"),
    path('admin-message/', views.admin_message, name = "admin_message"),
]