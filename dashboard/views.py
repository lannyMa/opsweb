from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    def get(self, request):
        return render(request, "public/index.html")


def login_view(request):
    if request.method == 'GET':
        return render(request, 'user/login.html', {'title': '运维平台'})
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        # 验证用户名和密码
        user = authenticate(username=username, password=password)
        ret = {'status': 0}
        if user is not None:
            if user.is_active:
                login(request=request, user=user)  # 写入cookie  session
                ret['next_url'] = "/"
            else:
                ret['status'] = 1
                ret['errmsg'] = "用户被禁用"
        else:
            ret['status'] = 2
            ret['errmsg'] = '用户名或密码错误'
        return JsonResponse(ret, safe=True)


def logout_view(request):
    print(request.user)
    logout(request)
    return HttpResponse('用户成功退出')
