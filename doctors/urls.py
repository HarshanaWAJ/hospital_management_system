from django.urls import path
from . import views

urlpatterns = [
    path('doctor_register/', views.register_doctor, name = "doctor_reg" ),
    path('doctor_management/', views.doctor_management, name = "doctor_management" ),
    path('delete_doctor/<int:id>/', views.delete_doctor, name = "delete_doctor" ),
]