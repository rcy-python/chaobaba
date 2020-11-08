import random
import re


from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status as http_status
from django_redis import get_redis_connection
from edu_api.libs.geetest import GeetestLib
from edu_api.utils.send_msg import Message
from user.models import UserInfo
from user.utils import get_user_by_account
from user.serializer import UserModelSerializer
from edu_api.utils import contastnt
pc_geetest_id = "1ea3ed8b35299a931b6a3883ec4a05be"
pc_geetest_key = "9a13879615c1ae2500e356417cd5bcf9"


class CaptchaAPIView(APIView):
    """滑块验证码"""

    user_id = 0
    status = False

    # pc端获取验证码的方法
    def get(self, request, *args, **kwargs):

        username = request.query_params.get("username")

        user = get_user_by_account(username)

        if user is None:
            return Response({"message": "用户不存在"}, status=http_status.HTTP_400_BAD_REQUEST)

        self.user_id = user.id

        # 验证码的实例化对象
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        self.status = gt.pre_process(self.user_id)

        response_str = gt.get_response_str()
        return Response(response_str)

    # pc端基于前后端分离校验验证码
    def post(self, request, *args, **kwargs):
        """验证验证码"""
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        challenge = request.POST.get(gt.FN_CHALLENGE, '')
        validate = request.POST.get(gt.FN_VALIDATE, '')
        seccode = request.POST.get(gt.FN_SECCODE, '')
        if self.user_id:
            result = gt.success_validate(challenge, validate, seccode, self.user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        result = {"status": "success"} if result else {"status": "fail"}
        return Response(result)

class UserAPIView(CreateAPIView):

    queryset = UserInfo.objects.all()
    serializer_class = UserModelSerializer

class MobileCheckAPIView(APIView):

    def get(self,request):
        phone = request.query_params.get("phone")
        if not re.match(r'^1[3-9]\d{9}$',phone):
            return Response({"message":"手机号格式不正确"},
                            status=http_status.HTTP_400_BAD_REQUEST)
        user = get_user_by_account(phone)

        if user is not None:
            return Response({"message":"手机号已经被注册"},status=http_status.HTTP_400_BAD_REQUEST)

        return Response({"message":"Ok"})


class SendMessageAPIView(APIView):
    def get(self,request,*args,**kwargs):

        phone = request.query_params.get("phone")
        redis_connection = get_redis_connection("sms_code")

        mobie_code = redis_connection.get('sms_%s' % phone)

        if mobie_code is not None:
            return Response({"message":"您已经在60s内发送过短信了"},status=http_status.HTTP_400_BAD_REQUEST)

        code = "%06d" % random.randint(0, 999999)

        redis_connection.setex("sms_%s" % phone, contastnt.SMS_EXPIRE_TIME, code)  # 验证码间隔时间
        redis_connection.setex("mobile_%s" % phone, contastnt.CODE_EXPIRE_TIME, code)  # 验证码有效期

        try:
            message = Message(contastnt.API_KEY)
            message.send_message(phone, code)
        except:
            return Response({"message": "验证码发送失败"},
                            status=http_status.HTTP_500_INTERNAL_SERVER_ERROR)

            # TODO 5.将发送的结果响应回去
        return Response({"message": "短信发送成功"},
                        status=http_status.HTTP_200_OK)

# Create your views here.
#手机号登录时验证手机号是否注册
class MobieCheckAPIView2(APIView):
    def get(self, request):
        phone = request.query_params.get("phone")
        if not re.match(r'^1[3-9]\d{9}$', phone):
            return Response({"message": "手机号格式不正确"},
                            status=http_status.HTTP_400_BAD_REQUEST)
        user = get_user_by_account(phone)

        if user is None:
            return Response({"message": "手机号未注册"}, status=http_status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Ok"})

#通过短信进行登录:

