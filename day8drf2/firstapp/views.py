from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from firstapp.models import Teacher
from firstapp.serializer import TeacherSerializer,TeacherDeSerializer


class teacherAPIView(APIView):
    def get(self,request,*args,**kwargs):
        teacher_id = kwargs.get("id")
        if teacher_id:
            res = Teacher.objects.get(id=teacher_id)
            teacher_data = TeacherSerializer(res).data
            return Response({
                "status":200,
                "message":"查询教师信息成功",
                "result": teacher_data
            })
        else:
            res = Teacher.objects.all()
            teacher_data = TeacherSerializer(res,many=True).data
            return Response({
                'status':200,
                'message':"查询所有教师成功",
                "result":teacher_data
            })
    def post(self,request,*args,**kwargs):
        teacher_data = request.data
        if not isinstance(teacher_data,dict) or teacher_data == {}:
            return Response({
                "STATUS":400,
                "message":"参数错误或者未收到参数",
            })
        serializer = TeacherDeSerializer(data=teacher_data)
        if serializer.is_valid():
            teacher = serializer.save()
            return Response({
                "status":200,
                "message":"教师添加成功",
                "data":TeacherSerializer(teacher).data
            })
        else:

            return Response({
                "status": 400,
                "message":"教师添加失败",
                "results": serializer.errors
            })