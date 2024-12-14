from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.make_appoinment, name = "create_appoinment"),
]
