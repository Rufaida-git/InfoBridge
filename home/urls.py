from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.base, name='home'),
    path("base", views.base, name='base'),
    path("login", views.login_view, name="login"),
]