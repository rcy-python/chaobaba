from django.contrib import admin
from django.urls import path, include

import drf
from drf import views

urlpatterns = [
    path("book/",views.BookAPIView.as_view()),
    path("book/<str:id>/",views.BookAPIView.as_view())
]