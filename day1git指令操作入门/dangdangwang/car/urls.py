from django.urls import path, include

from car import views
app_name='car'
urlpatterns = [
    path('carlist/', views.carlist, name='carlist'),
    path('add_car/', views.add_car, name='add_car'),
    path('rem_car/', views.rem_car, name='rem_car'),
    path('update_car/', views.update_car, name='update_car'),
    path('delete_all/',views.delete_all,name="delete_all"),
]