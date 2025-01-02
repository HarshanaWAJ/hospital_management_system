
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('appointments/', include('appoinments.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),

    #Doctor
    path('doctor/', include('doctors.urls')),
    path('admins/', include('admins.urls')),
    path('staff/', include('staff.urls')),
    path('appointments/', include('appoinments.urls')),

    path('patients/', include('patient.urls')),
]
