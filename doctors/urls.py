from django.urls import path
from . import views

urlpatterns = [
    path('doctor_register/', views.register_doctor, name = "doctor_reg" ),
]