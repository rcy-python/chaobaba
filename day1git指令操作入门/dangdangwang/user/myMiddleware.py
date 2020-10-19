from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from user.models import TUser

class myMiddleware(MiddlewareMixin):
    def process_request(self,request):
        a = ['order']
        for foo in a:
            if foo in request.path:
               user = request.session.get('login')
               if user:
                    pass
               else:
                    url= request.get_full_path()
                    return redirect('/user/login/?url='+url)

        return

    def process_view(self, request, view_func, view_args, view_kwargs):
        a = ["index",'book','car','address','order']
        for foo in a:
            if foo in request.path:
                user = request.session.get('login')
                user = TUser.objects.filter(id=user)
                if user:
                    user = user[0].user_name
                else:
                    user = None
                print(user, '中间件生效')
                return view_func(request,user,*view_args,**view_kwargs)
