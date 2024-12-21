from django.urls import path
from . import views 

urlpatterns = [
    path('admin_register/', views.register_admin, name="admin_reg"), 
]
