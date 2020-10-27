

from django.urls import path, include

from firstapp import views

urlpatterns = [
    path("user_view/",views.Userview.as_view()),
    path("user_view/<str:id>/",views.Userview.as_view()),
]
