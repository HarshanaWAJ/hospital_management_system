from django.urls import path
from . import views

urlpatterns = [
    path('staff_register/', views.register_staff, name = "staff_reg" ),
]