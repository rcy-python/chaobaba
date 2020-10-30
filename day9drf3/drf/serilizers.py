
from rest_framework import serializers

from drf.models import Press, Book


class PressModelSlizer(serializers.ModelSerializer):
    class Meta:
        model = Press
        fields = ('press_name',"pic","address")
class BookModelSerializer(serializers.ModelSerializer):

    publish = PressModelSlizer()
    class Meta:
        model = Book
        fields = ("book_name","price","pic","publish")

class BookDeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("book_name","price","publish","authors")

        extra_kwarges = {
            "book_name":{
                "required":True,
                "min_length":2,
                "error_messages":{
                    "required":"图书名必须提供",
                    "min_length":"书名必须打鱼两个字"
                }

            }
        }
class BookModekSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('book_name',"price","publish","authors","pic")

        extra_kwargs = {
            "book_name":{
                "required":True,
                "min_length":2,
                "error_messages":{
                    "required":"图书名必须停工",
                    "min_length":"图书名不能少于两个字符"
                }
            },
            "pic":{
                "read_only":True
            },

            "publish":{
                "write_only":True
            }
        }
