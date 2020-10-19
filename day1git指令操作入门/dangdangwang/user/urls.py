from django.contrib import admin
from django.urls import path
from user import views
app_name='user'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('register/',views.register,name='register'),
    path('ajax_vcode/',views.ajax_vcode,name='ajax_vcode'),
    path('get_captcha/',views.get_captcha,name='captcha'),
    path('ajax_name/',views.ajax_name,name='ajax_name'),
    path('register_result/',views.register_result,name='register_result'),
    path('registerok/',views.registerok,name='registerok'),
    path('login/',views.login,name='login'),
    path('login_result/',views.login_result,name='login_result'),
    path('login_out/',views.login_out,name='login_out'),
]