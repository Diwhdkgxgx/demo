from django.shortcuts import render, redirect
from django.http import HttpResponse

User = {'sxy1': '123', 'sxy2': '456'}


def main(request):
    return render(request, 'main.html')


def login(requset):
    if requset.method == 'GET':
        return render(requset, 'login.html')
    elif requset.method == 'POST':
        username1 = requset.POST.get('username1')
        password1 = requset.POST.get('password1')
        if username1 in User and password1 == User[username1]:
            response = redirect("../main/")
            return response
        elif username1 not in User:
            error = {'error': '用户不存在，请注册！'}
            return render(requset, 'login.html', error)
        elif username1 in User and password1 != User[username1]:
            error = {'error': '密码输入错误，请重新输入！'}
            return render(requset, 'login.html', error)


def regisiter(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username2 = request.POST.get('username2')
        password2 = request.POST.get('password2')
        password3 = request.POST.get('password3')
        if len(username2) == 0:
            errorn = {'errorn': '用户名不得为空！'}
            return render(request, 'register.html', errorn)
        elif len(password2) == 0:
            errorn = {'errorn': '密码不得为空！'}
            return render(request, 'register.html', errorn)
        elif password2 != password3:
            errorn = {'errorn': '两次输入的密码不一致，请重试！'}
            return render(request, 'register.html', errorn)
        else:
            if username2 in User:
                error = {'error': '用户名已存在，点击前往登陆'}
                return render(request, 'register.html', error)
            elif len(username2) > 10:
                errorn = {'errorn': '用户名长度不得超过10位！'}
                return render(request, 'register.html', errorn)
            elif len(password2) > 10:
                errorn = {'errorn': '密码长度不得超过10位！'}
                return render(request, 'register.html', errorn)
            elif islegal(password2) == 0:
                errorn = {'errorn': '密码有不合法字符，请重试！'}
                return render(request, 'register.html', errorn)
            else:
                User[username2] = password2
                success = {'success': '注册成功，点击返回登陆'}
                return render(request, "register.html", success)

def islegal(password):
    legal = "0123456789abcdefghijklmnopqrstivwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_+-=[]{}\|:';:,.<>?/"
    for i in password:
        if i not in legal:
            return 0

