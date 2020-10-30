from rest_framework.response import Response
from rest_framework.views import APIView

from drf.models import Book
from drf.serilizers import BookModelSerializer, BookDeModelSerializer


# Create your views here.
class BookAPIView(APIView):
    def get(self,request,*args,**kwargs):
        book_id = kwargs.get("id")

        if book_id:
            book = Book.objects.get(pk=book_id)
            data = BookModelSerializer(book).data
            return Response({
                "STATUS":1,
                "MESSAGE":"查询单表陈宫",
                "data":data
            })

    def post(self,request,*args,**kwargs):
        request_data = request.data
        serializer = BookDeModelSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        book = serializer.save()
        return Response({
            "status":1,
            "message":"天价图书成功",
            "results":BookModelSerializer(book).data
        })

class BookAPIViewV2(APIView):
    def get(self,request,*args,**kwargs):
        book_Id = kwargs.get("id")
        if book_Id:
            book = Book.objects.get(pk = book_Id,is_delete=False)

            data = BookAPIViewV2