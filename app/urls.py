from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('todo/',views.todo,name="todo"),
    path('edit/<int:sno>/',views.edit,name="edit"),
    path('delete/<int:sno>/',views.delete,name="delete"),
    path('signout',views.signout)
]