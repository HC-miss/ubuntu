from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from .form import *


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        # 如果输入信息有效且同意协议
        if form.is_valid() and request.POST.get('allow'):
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('passwrod2')
            # 使用内置User自带create_user方法创建用户，不需要使用save()
            user = User.objects.create_user(username=username, email=email, password=password)
            UserProfile.objects.create(user=user)
            # 注册成功跳转到登录页面
            return redirect('/account/login/')
        else:
            return render(request, 'register1.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'register1.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if request.POST.get('allow') != 'on' and request.session.get('rmbps'):
            del request.session['rmbps']
        if form.is_valid():
            # 此处传入的用户全是经过表单筛选的已存于数据库的
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # allow = form.cleaned_data.get('allow')
            # 当密码不对时会返回None
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                # 记住密码
                if request.POST.get('allow'):
                    request.session['rmbps'] = username+'/'+password
                # 登录成功跳转到主页
                # return HttpResponse("<a href='{% url 'account:loginout' %}'>退出登录</a>")
                return redirect('goods:index')
        return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        value = None
        # 如果记住了密码 那么就将session缓存的账号密码切片 并传给模板
        if request.session.get('rmbps'):
            value = request.session.get('rmbps').split('/')
    return render(request, 'login.html', {'form': form, 'value': value})


def loginout(request):
    auth.logout(request)
    return redirect("/account/login/")


def resetps(request):
    return None


def userinfo(request):
    return render(request, 'user_center_info.html')