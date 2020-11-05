from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path("banner/", views.BannerListAPIView.as_view()),
    path("header/",views.HeaderListAPIview.as_view()),
    path("footer/",views.FooterListAPIview.as_view()),
]