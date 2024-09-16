
from django.urls import path

from userprofile.views import logout, signup, custom_login, dashboard

app_name = 'userprofile'

urlpatterns = [
    path('logout/', logout, name="logout"),
    path('signup/', signup, name='signup'),
    path('login/', custom_login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
]
