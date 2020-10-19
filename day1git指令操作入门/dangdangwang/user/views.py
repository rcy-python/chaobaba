from django.shortcuts import render, redirect
from captcha.image import ImageCaptcha
import random,string
from django.http import HttpResponse, JsonResponse
from user.models import TUser
def register(request):
    url = request.GET.get("url")
    return render(request,'register.html',{"url":url})
def ajax_vcode(request):
    code = request.POST.get('code')
    code1 = request.session.get('code')
    if code.lower() == code1.lower():
        return HttpResponse('true')
    else:
        return HttpResponse('farse')
def ajax_name(request):
    name = request.POST.get('name')
    AS = TUser.objects.filter(user_name=name)
    if AS:
        return HttpResponse('false')
    else :
        return HttpResponse('true')
def register_result(request):
    if request.method=='POST':
        name = request.POST.get('name')
        pswd = request.POST.get('password')
        TUser.objects.create(user_name=name,user_password=pswd)
        res = TUser.objects.filter(user_name=name,user_password=pswd)
        if res:
            request.session['login'] = res[0].id
            return HttpResponse('true')
        else:
            return HttpResponse('false')
    else:
        return HttpResponse('')

def registerok(request):
    url=request.session.get('url')
    a = request.GET.get('url')
    print(url)
    name = request.GET.get("name")
    return render(request,'register ok.html',{"name":name,"url":url})
def login(request):
    url = request.GET.get('url')
    request.session['url']=url
    return render(request,'login.html',{"url":url})
def login_result(request):
    name = request.POST.get('name')
    password = request.POST.get('password')
    vcode = request.POST.get('vcode')
    code = request.session.get('code')
    auto = request.POST.get('auto')
    if code.lower() != vcode.lower():
        print('验证码错误')
        return HttpResponse('code_error')
    else:
        res = TUser.objects.filter(user_name=name,user_password=password)
        if res:
            if auto=="1":
                request.session['login'] = res[0].id
            elif auto=="0":
                request.session['login'] = res[0].id
                request.session.set_expiry(0)
            return HttpResponse('true')
        else:
            return HttpResponse('password_error')
def login_out(request):
    request.session['login'] = None
    return HttpResponse('ok')

def get_captcha(request):
    code_list = random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits,4)
    code = ''.join(code_list)
    request.session['code'] = code
    print(code)
    img = ImageCaptcha()
    data = img.generate(code)
    return HttpResponse(data, 'image/png')
#
# Create your views here.
