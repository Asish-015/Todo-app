from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('todo/',views.todo,name="todo"),
]