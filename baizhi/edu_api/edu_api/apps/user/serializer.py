import re

from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django_redis import get_redis_connection
from rest_framework_jwt.settings import api_settings

from user.models import UserInfo
from user.utils import get_user_by_account

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserModelSerializer(ModelSerializer):
    token = serializers.CharField(max_length=1024, read_only=True, help_text="用户token")
    code = serializers.CharField(write_only=True, help_text="手机验证码")

    class Meta:
        model = UserInfo
        fields = ("phone", "password", "id", "username", "token", "code")

        extra_kwargs = {
            "phone": {
                "write_only": True
            },
            "password": {
                "write_only": True
            },
            "username": {
                "read_only": True
            },
            "id": {
                "read_only": True
            }
        }

    def validate(self, attrs):

        phone = attrs.get("phone")
        # password = attrs.get("password")
        sms_code = attrs.get('code')  # 手机验证码

        # 验证手机号格式
        if not re.match(r'^1[3-9]\d{9}$', phone):
            raise serializers.ValidationError("手机号格式错误")

        # 验证手机号格式
        try:
            user = get_user_by_account(phone)
        except UserInfo.DoesNotExist:
            user = None

        if user:
            raise serializers.ValidationError("当前手机号已经被注册")

        # TODO 检验密码的格式

        # TODO 校验验证码是否一致
        redis_connection = get_redis_connection("sms_code")
        mobile_code = redis_connection.get("mobile_%s" % phone)
        if mobile_code.decode() != sms_code:
            # 代表验证码有误
            # 为了防止暴力破解  可以设置一个手机号只能验证n次  累加
            raise serializers.ValidationError("验证码不一致")

        # 验证通过后将redis的验证码的删除

        return attrs

    def create(self, validated_data):

        password = validated_data.get("password")
        hash_password = make_password(password)

        username = validated_data.get('phone')

        user = UserInfo.objects.create(
            phone=username,
            username=username,
            password=hash_password
        )

        from rest_framework_jwt.settings import api_settings
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        user.token = jwt_encode_handler(payload)

        return user


class UserModelSerializer2(ModelSerializer):
    token = serializers.CharField(max_length=1024, read_only=True, help_text="用户token")
    code = serializers.CharField(write_only=True, help_text="手机验证码")

    class Meta:
        model = UserInfo
        fields = ("phone", "id", "token", "code")

        extra_kwargs = {
            "phone": {
                "write_only": True
            },

            "id": {
                "read_only": True
            }
        }

    def validate(self, attrs):
        print(attrs)
        phone = attrs.get("phone")
        sms_code = attrs.get("code")

        if not re.match(r'^1[3-9]\d{9}$', phone):
            raise serializers.ValidationError("手机号格式错误")

        try:
            user = get_user_by_account(phone)
        except UserInfo.DoesNotExist:
            raise serializers.ValidationError("当前手机号不存在")

        # TODO 检验密码的格式

        # TODO 校验验证码是否一致
        redis_connection = get_redis_connection("sms_code")
        mobile_code = redis_connection.get("mobile_%s" % phone)
        if mobile_code.decode() != sms_code:
            # 代表验证码有误
            # 为了防止暴力破解  可以设置一个手机号只能验证n次  累加
            raise serializers.ValidationError("验证码不一致")

        # 验证通过后将redis的验证码的删除
        else:
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            self.obj = user
            self.token = token
            return {
                'token': self.obj,
                'user': self.token
            }
