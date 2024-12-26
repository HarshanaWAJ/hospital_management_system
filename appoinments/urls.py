from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.make_appointment, name = "create_appointment"),
    path('my_appointments/', views.user_view_appointments, name="my_appointments"),
    path('doctor_view_appointments/', views.doctor_view_pending_appointments, name="doctor_view_appointments"),
    path('delete_appointment/<int:id>/', views.delete_appointment, name='delete_appointment'),
    path('accept_reject_appointment/<int:id>/<str:action>/', views.accept_reject_appointment, name='accept_reject_appointment'),
]
