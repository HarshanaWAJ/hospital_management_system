from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.make_appointment, name = "create_appointment"),
    path('my_appointments/', views.user_view_appointments, name="my_appointments"),
    path('doctor_view_appointments/', views.doctor_view_pending_appointments, name="doctor_view_appointments"),
]
