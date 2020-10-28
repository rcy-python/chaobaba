from django.contrib import admin
from django.urls import path, include

from firstapp import views

urlpatterns = [
    path('user/',views.teacherAPIView.as_view()),
    path('user/<str:id>/',views.teacherAPIView.as_view())
]