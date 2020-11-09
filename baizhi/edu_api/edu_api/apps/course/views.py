from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from course import models
from course.serializers import CourseCategoryModelSerializer, CourseModelSerializer
from course.pagination import MyPagination

class CourseCategoryAPIView(ListAPIView):
    """课程分类详细查询"""
    queryset = models.CourseCategory.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = CourseCategoryModelSerializer


class CourseAPIView(ListAPIView):
    queryset = models.Courses.objects.filter(is_show=True,is_delete=False).order_by("orders")
    serializer_class = CourseModelSerializer
    # 根据不同的分类id来展示查询对应的课程
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # 指定查询的字段
    filter_fields = ("course_category",)

    # 指定课程可以排序的条件
    ordering_fields = ("id", "students", "price")

    # 指定分页的类
    pagination_class = MyPagination
