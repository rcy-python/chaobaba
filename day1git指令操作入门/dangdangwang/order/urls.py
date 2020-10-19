from django.urls import path, include

from order import views
app_name='order'
urlpatterns = [
    path('address/', views.address, name='address'),
    path('ads_select/',views.ads_select,name="ads_select"),
    path('create_ads/',views.create_ads,name="create_ads"),
    path('get_new/',views.get_new,name="get_new"),
    path('indentok/',views.indentok,name="indentok"),
]