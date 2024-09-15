
from django.urls import path

from userprofile.views import logout, signup, custom_login, dashboard

app_name = 'userprofile'

urlpatterns = [
    path('log-out/', logout, name="logout"),
    path('sign-up/', signup, name='signup'),
    path('log-in/', custom_login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
]
