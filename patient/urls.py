from django.urls import path
from . import views

urlpatterns = [
    path('opd_patient_reg/', views.register_opd_patient, name = "opd_patient_reg" ),
]