from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from car.car import Car,Book
from user.models import TUser, TCar
def carlist(request,user):
    car = request.session.get('car')
    if user:
        t_user = TUser.objects.get(user_name=user)
        t_user = t_user.id
        if car:
            books = TCar.objects.filter(user_id=t_user)
            for i in books:  # 将之前session中的图书与该账号之中的图书进行去重
                for j in car.book_List:
                    if int(i.book_id) == int(j.id):
                        i.product_number = int(i.product_number) + int(j.count)
                        i.save()
                        car.book_List.remove(j)
            for m in car.book_List:
                TCar.objects.create(book_id=m.id, user_id=t_user, product_number=m.count)
            del request.session['car']
            book2 = TCar.objects.filter(user_id=t_user)
            content = {"user": user, "book2": book2}
            return render(request, 'car.html', content)
        else:
            book2 = TCar.objects.filter(user_id=t_user)
            content = {"user": user, "book2": book2}
            return render(request, 'car.html', content)
    else:
        books = request.session.get("car")
        content = {"user": user,"book":books}
        return render(request,'car.html',content)
def add_car(request,user):
    id = request.POST.get('id')
    count = request.POST.get('count1')
    car = request.session.get('car')
    if user:
        t_user = TUser.objects.filter(user_name=user)
        if t_user:
            t_user = t_user[0].id
        book = TCar.objects.filter(book_id=id, user_id=t_user)
        if book:  # 还在登录状态(且这本书添加过了)
            book[0].product_number = int(count) + int(book[0].product_number)
            book[0].save()
            return HttpResponse("登录中更改旧书")
        else:  # 一直在登录状态(添加新书)
            TCar.objects.create(book_id=id, user_id=t_user, product_number=count)
            return HttpResponse("登录中添加新书")
    else:
        if car:
            car.add_book(id,count)
            request.session['car'] = car
            return HttpResponse('未登录添加书')
        else:
            car = Car()
            car.add_book(id,count)
            request.session['car'] = car
            return HttpResponse("未登录添加新购物车")
def rem_car(request,user):
    id = request.POST.get('id')
    car = request.session.get('car')
    if user:
         t_user = TUser.objects.filter(user_name=user)
         t_user = t_user[0].id
         car = TCar.objects.get(user_id=t_user,book_id=id)
         car.delete()
         user_car = TCar.objects.filter(user_id=t_user)
         if user_car:
            return HttpResponse("从数据库删除成功")
         else:
            return HttpResponse("删光了")
    else:
        car.remove_book(id)
        request.session['car'] = car
        if car:
            return HttpResponse("从session删除成功")
        else:
            return HttpResponse('删光了')
def update_car(request,user):
    id = request.POST.get('id')
    count = request.POST.get('count1')
    car = request.session.get('car')
    if user:
        t_user = TUser.objects.filter(user_name=user)
        t_user = t_user[0].id
        car = TCar.objects.get(user_id=t_user, book_id=id)
        car.product_number = count
        car.save()
        return HttpResponse("从数据库更改成功")
    else:
        car.update_book(id,count)
        request.session['car'] = car
        return HttpResponse("从session更改成功")
def delete_all(request,user):
    if user:
        t_user = TUser.objects.filter(user_name=user)
        t_user = t_user[0].id
        car = TCar.objects.filter(user_id=t_user)
        car.delete()
        return HttpResponse('从数据库删除所有数据')
    else:
        del request.session['car']
        return HttpResponse('删除session所有数据')
