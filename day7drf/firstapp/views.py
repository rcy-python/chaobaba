from django.http import JsonResponse
from django.shortcuts import render

from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from firstapp.models import User


@method_decorator(csrf_exempt,name="dispatch")
class Userview(View):
    def get(self,request,*args,**kwargs):
        print(111111111111)
        user_id = kwargs.get('id')
        if user_id:
            user=User.objects.filter(id=user_id).values("name","salary").first()
            print(user)
            if user:
                return JsonResponse({
                    "status":200,
                    "message":"查询单个用户成功",
                    "result":user
                })
            else:
                return  JsonResponse({
                    "status":400,
                    "message":"查询失败"
                })
        else:
            user= User.objects.all().values("username","salary")
            if user:
                return JsonResponse({
                    "status": 200,
                    "message": "查询所有用户成功",
                    "result": user
                })
            else:
                return  JsonResponse({
                    "status":400,
                    "message":"查询失败"
                })
    def post(self,request,*args):
        username = request.POST.get('username')
        salary = request.POST.get('salary')
        try:
            user_obj=User.objects.create(id="5",name=username,salary=salary)
            return JsonResponse({
                "status": 200,
                "message": "新增单个用户成功",
                "results": {"username": user_obj.name, "salary": user_obj.salary}
            })
        except:
            return JsonResponse({
                "status": 400,
                "message": "新增单个用户失败",
            })
    def delete(self,request,*args,**kwargs):
        user_id = kwargs.get('id')
        print(user_id)
        if user_id:
            try:
                user = User.objects.get(id=user_id)
                user.delete()
                return JsonResponse({
                    "status": 200,
                    "message": "删除成功"
                })
            except:
                return JsonResponse({
                    "status":400,
                    "message":"删除失败"
                })
        else:
            return JsonResponse({
                "status": 400,
                "message": "删除失败"
            })


