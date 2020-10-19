from django.contrib import admin
from django.urls import path, include

from index import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('bookdetial/',views.book,name='book'),
    path('booklist/',views.booklist,name='booklist')
]