from django.urls import include, path, re_path
from .views import LoginOrRegister

urlpatterns = [
    path('login/or/register/',
         LoginOrRegister.as_view(), name='login_or_register')
]
