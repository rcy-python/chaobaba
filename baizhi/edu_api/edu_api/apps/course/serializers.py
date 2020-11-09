from rest_framework.serializers import ModelSerializer

from course.models import CourseCategory, Courses, Teachers


class CourseCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ("id", "name")


class TeacherModelSerializer(ModelSerializer):
    class Meta:
        model = Teachers
        fields = ["id", "name", "title", "signature"]


class CourseModelSerializer(ModelSerializer):
    teacher = TeacherModelSerializer()

    class Meta:
        model = Courses
        fields = ("id", "name", "course_img", "students", "lessons", "pub_lessons", "price",
                  "teacher", "lesson_list")

class CourseDetailModelSerializer(ModelSerializer):
    """提供课程详情所需的信息"""
    pass
