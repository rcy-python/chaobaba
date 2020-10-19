from django.db.models import Max
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from user.models import TCar,TUser,TAddress,TOrder,TBookOrder
import time
from datetime import datetime
# Create your views here.
def address(request,user):
    userid = TUser.objects.get(user_name=user)
    cars = TCar.objects.filter(user_id=userid)
    addresses = TAddress.objects.filter(user_id=userid)
    content = {"user": user,"cars":cars,"addresses":addresses}
    return render(request,"indent.html",content)
def default(u):
    if isinstance(u,TAddress):
        return {'id':u.id,"name":u.name,"detail":u.detail,"post_code":u.post_code,"phone":u.phone,"user_id":u.user_id,"cellphone":u.cellphone}
def ads_select(request,user):
    id = request.POST.get('id')
    ads = TAddress.objects.get(id=id)
    return JsonResponse(ads,safe=False,json_dumps_params={"default":default})
def create_ads(request,user):
    userid = TUser.objects.get(user_name=user)
    userid = userid.id
    name = request.POST.get('name')
    post_code=request.POST.get('post_code')
    detail =request.POST.get("address")
    phone = request.POST.get('phone')
    cellphone = request.POST.get('cellphone')
    TAddress.objects.create(name=name,post_code=post_code,detail=detail,cellphone=cellphone,user_id=userid,phone=phone)
    ads = TAddress.objects.filter().last()
    return HttpResponse(ads.id)
def get_new(request,user):
    userid = TUser.objects.get(user_name=user)
    user_id = userid.id
    cars = TCar.objects.filter(user_id=user_id)
    id = str(time.time()).replace(".","")[-9:]
    order_id = int(id)
    order_time = datetime.now()
    address_id = request.POST.get('ads_id')
    all_price = request.POST.get('all_price')
    name = TAddress.objects.get(id=address_id)
    name = name.name
    order = TOrder.objects.create(user_id=user_id,order_id=order_id,order_time=order_time,address_id=address_id)
    car_all = 0
    for car in cars:
        car_all += int(car.product_number)
        TBookOrder.objects.create(book_id=car.book_id,order_id=order.order_id,book_numbers=car.product_number)
    cars.delete()
    request.session['order']={"name":name,"car_all":car_all,"order_id":order_id,"all_price":all_price}
    return HttpResponse("true")
def indentok(request,user):
    order = request.session.get('order')
    name=order.get('name')
    car_all = order.get('car_all')
    order_id = order.get('order_id')
    all_price = order.get("all_price")
    content = {"name":name,"car_all":car_all,"order_id":order_id,"user":user,"all_price":all_price}
    return render(request,'indent ok.html',content)
def out(requesst):
    return (requesst)

