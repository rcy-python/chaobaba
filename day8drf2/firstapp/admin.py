from django.contrib import admin
from firstapp import models
class Teacher(admin.ModelAdmin):
    list_display = ("name","age",'gender','phone','pic')
admin.site.register(models.Teacher,Teacher)
# Register your models here.
