from django.urls import path

from course import views

urlpatterns = [
    path("category/", views.CourseCategoryAPIView.as_view()),
    path("list/", views.CourseAPIView.as_view()),
]