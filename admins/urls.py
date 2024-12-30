from django.urls import path
from . import views

urlpatterns = [
    path('admin_register/', views.register_admin, name="admin_reg"), 
    path('admin_management/', views.admin_management, name="admin_management"),
    path('admin_delete/<int:id>/', views.delete_admin, name="admin_delete"),
    path('get_admin/<int:admin_id>/', views.get_admin_data, name='get_admin_data'),
    path('update-admin/', views.update_admin, name='update_admin'),  # URL for updating admin
]
