from django.contrib.auth import authenticate, logout, login

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from blog.forms import LoginForm, RegForm, CommentForm
from blog.models import *


def page(request, obj, num):
    p = Paginator(obj, num)
    page = request.GET.get('page')
    list = p.get_page(page)
    return list


def index(request):
    article = Article.objects.all()
    # 每页条数
    limit = 10
    article_list = page(request, article, limit)
    # 总数
    count = len(article)
    title = '首页'
    return render(request, 'blog/index.html', locals())


def art(request, id):

    art = Article.objects.get(pk=id)
    com = Comment.objects.filter(article=id).all()[:5]
    title = '{}'.format(art.title)
    if request.method == 'POST':

        com_form = CommentForm(request.POST)

        if com_form.is_valid():
            com_title = com_form.cleaned_data['com_title']
            com_body = com_form.cleaned_data['com_body']
            if request.user.is_authenticated:
                user = request.user
                # 获取当前用户
                print(request.user)
                comm = Comment(title=com_title,body=com_title,article=art,username=user)
                comm.save()

                return render(request,'blog/article.html',locals())
            else:
                error = '请登录'
                return render(request,'blog/article.html',locals())
        else:
            return render(request,'blog/article.html',locals())

    return render(request, 'blog/article.html', locals())


def post(request):
    article = Article.objects.all()
    return render(request, 'blog/index.html')


def log_in_demo(request):
    if request.method == 'GET':
        return render(request, 'auth/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # authenticate  密码加密才能用,不能使用明文密码
        print(user)
        if user and user.is_active:
            login(request, user=user)
            return redirect('index')
        else:
            return render(request, 'auth/login.html')


def log_in(request):
    if request.user.is_authenticated:
        return redirect('blog:index')

    else:
        title = '登录'
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                name = login_form.cleaned_data['username']
                pwd = login_form.cleaned_data['password']
                print(name, pwd)
                try:
                    user = authenticate(request, username=name, password=pwd)
                    print(user)
                    if user is not None:
                        login(request, user)
                        return redirect('blog:index')
                    else:
                        user = User.objects.get(username=name)
                        print(user)
                        if name == user.username and pwd == user.password:
                            return redirect('blog:index')
                        else:
                            error = '用户名或密码错误'
                            return render(request, 'auth/login.html', locals())
                except Exception as e:
                    print(e)
                    user = User.objects.get(username=name)

                    if name == user.username and pwd == user.password:
                        return redirect('blog:index')
                    else:
                        return render(request, 'auth/login.html')
            else:
                error = '提交错误'
                return render(request, 'auth/login.html', locals())

        return render(request, 'auth/login.html')


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('blog:index')
    else:
        return redirect('blog:login')


def reg(request):
    if request.user.is_authenticated:
        return redirect('blog:index')
    else:
        title= '注册'
        if request.method == 'POST':
            reg_form = RegForm(request.POST)

            if reg_form.is_valid():
                username = reg_form.cleaned_data['username']
                first_name = reg_form.cleaned_data['first_name']
                last_name = reg_form.cleaned_data['last_name']
                email = reg_form.cleaned_data['email']
                phone = reg_form.cleaned_data['phone']
                wechat = reg_form.cleaned_data['wechat']
                password = reg_form.cleaned_data['password']
                user = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email,
                                           phone=phone, wechat=wechat, password=password)
                user.save()
                return redirect('blog:login')
            else:

                error = '请检查表单,全部填写'
                return render(request, 'auth/reg.html', locals())
        return render(request, 'auth/reg.html', locals())


