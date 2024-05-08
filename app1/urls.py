from django.urls import path
from app1 import views

urlpatterns = [
    path("",views.fun1),
    path("signUp/",views.Signup),
    path("login/",views.login)
]
