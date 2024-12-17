from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.make_appointment, name = "create_appoinment"),
]
