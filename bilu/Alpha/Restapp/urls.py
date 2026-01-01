from django.contrib import admin
from django.urls import path
from .views import profile, userprofile

urlpatterns = [
    path('ser/', userprofile.as_view()),
    path('ser/<int:pk>/',profile.as_view())
]