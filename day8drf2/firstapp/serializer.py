from rest_framework import  serializers

from day8drf2 import settings
from firstapp.models import Teacher


class TeacherSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    gender = serializers.IntegerField()
    phone = serializers.CharField()
    pic = serializers.SerializerMethodField()
    def get_pic(self,obj):
        return"%s%s%s" % ("http://127.0.0.1:8000/",settings.MEDIA_URL,str(obj.pic))

class TeacherDeSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=3,
        min_length=2,
        error_messages={
            "max_length":"太长",
            "min_length":"太短"
        }
    )
    age = serializers.IntegerField()
    gender = serializers.IntegerField()
    phone = serializers.CharField()
    def create(self,validated_data):
        return Teacher.objects.create(**validated_data)
