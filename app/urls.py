from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ask/', views.ask, name="ask"),
    path('question/<int:i>', views.question, name="question"),
    path('question/<int:i>/up', views.question_rating_up, name="question_rating_up"),
    path('question/<int:i>/down', views.question_rating_down, name="question_rating_down"),
    path('answer/<int:i>/up', views.answer_rating_up, name="answer_rating_up"),
    path('answer/<int:i>/down', views.answer_rating_down, name="answer_rating_down"),
    path('hot/', views.hot, name="hot"),
    path('tag/<str:s>', views.tag, name="tag"),
    path('login/', views.log_in, name="log-in"),
    path('signup/', views.sign_up, name="sign-up"),
    path('profile/edit/', views.settings, name="settings")
]
