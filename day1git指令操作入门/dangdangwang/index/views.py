from django.core.paginator import Paginator
from django.db import models
from django.shortcuts import render
from user.myMiddleware import myMiddleware
from user.models import TUser,TBook

from user.models import TCates,TBook


def index(request,user):
    cates1 = TCates.objects.filter(cate_level=1)
    cates2 = TCates.objects.filter(cate_level=2)
    new_book = TBook.objects.all().order_by('shelves')[0:8]
    hot_new_book=TBook.objects.exclude(shelves__lte="2019-5-22 12:12:12").order_by('-shelves')[0:5]
    book_price = TBook.objects.all().order_by("-shelves")
    content = {'cates1':cates1,'cates2':cates2,'new_book':new_book,"hot_new_book":hot_new_book,'book_price':book_price,"user":user}
    return render(request,'index.html',content)
# Create your views here.
def book(request,user):
    id = request.GET.get('id')
    book = TBook.objects.get(book_id=id)
    a=TCates.objects.get(cate_id=book.cate_id)
    b=TCates.objects.get(cate_id=a.parent_id)

    content = {'book':book,'a':b,'b':a,"user":user}
    return render(request,'Book details.html',content)
def booklist(request,user):
    level= request.GET.get('level')
    id = request.GET.get('id')
    num = request.GET.get('num')
    if id==None:
        id="1"
    if level==None:
        level="1"
    if num==None:
        num='1'
    if level == '1':
        a=TCates.objects.get(cate_id=id)
        b=None
        books = TBook.objects.filter(cate__parent_id=id)
    else:
        a=TCates.objects.get(cate_id=id)
        b=TCates.objects.get(cate_id=a.parent_id)
        books = TBook.objects.filter(cate_id=id)
    pagtor = Paginator(books,per_page=2)
    page = pagtor.page(num)
    cates1 = TCates.objects.filter(cate_level=1)
    cates2 = TCates.objects.filter(cate_level=2)
    content = {'cates1': cates1, "cates2": cates2, "books": page,"id":id,"level":level,"a":a,"b":b,"user":user}
    return render(request, 'booklist.html', content)


        # res = TBook.objects.filter(cate_id=父标签为传过来的id的分类)