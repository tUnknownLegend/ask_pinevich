from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ask/', views.ask, name="ask"),
    path('question/<int:i>', views.question, name="question"),
    path('hot/', views.hot, name="hot"),
    path('tag/<str:s>', views.tag, name="tag"),
    path('login/', views.logIn, name="log-in"),
    path('signup/', views.signUp, name="sign-up"),
    path('settings/', views.settings, name="settings")
]
