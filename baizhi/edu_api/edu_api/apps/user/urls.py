from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from user import views

urlpatterns = [
    path("login/", obtain_jwt_token),
    path("login2/",views.Msg_login.as_view()),
    path("captcha/", views.CaptchaAPIView.as_view()),
    path("register/",views.UserAPIView.as_view()),
    path("phone/", views.MobileCheckAPIView.as_view()),
    path("phone2/", views.MobieCheckAPIView2.as_view()),
    path("send/", views.SendMessageAPIView.as_view()),
]