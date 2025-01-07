from django.urls import path
from . import views

urlpatterns = [
    path('add_record/', views.add_record, name = "add_record"),    
    path('view_record/', views.view_record, name = "view_record"),
]