from django.db import models

# Create your models here.
class Teacher(models.Model):
    gender_choices=(
        (0,'male'),
        (1,'female'),
        (2,'other'),
    )
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=4)
    gender = models.SmallIntegerField(max_length=11,choices=gender_choices,null=True,blank=True)
    phone = models.CharField(max_length=11,null=True,blank=True)
    pic = models.ImageField(upload_to="pic/",default="pic/1.jpg")
    class Meta:
        db_table = "tb_teacher"
        verbose_name = "老师"
        verbose_name_plural = verbose_name