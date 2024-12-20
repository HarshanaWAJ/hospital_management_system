from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name = "home" ),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('admin-message/', views.admin_message, name = "admin_message"),
    path('delete-message/<int:message_id>/', views.delete_message, name='delete_message'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
