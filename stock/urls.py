from django.urls import path
from . import views

urlpatterns = [
    path('stock_dashboard/', views.view_stock_dashboard, name='stock_dashboard'),
]