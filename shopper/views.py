from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import reverse
import time

from commodity.models import *
from .models import *
from .form import *
from .pays_new import get_pay


def loginView(request):
    title = '用户登录'
    classContent = 'logins'

    if request.method == 'POST':
        infos = LoginModelForm(data=request.POST)
        data = infos.data
        username = data['username']
        password = data['password']
        if User.objects.filter(username=username):
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('shopper:shopper'))
        else:
            state = '注册成功'
            d = dict(username=username, password=password, is_staff=1, is_active=1)
            user = User.objects.create_user(**d)
            user.save()
    else:
        infos = LoginModelForm()
    return render(request, 'login.html', locals())


@login_required(login_url='/shopper/login.html')
def shopperView(request):
    title = '个人中心'
    classContent = 'informations'

    p = request.GET.get('p', 1)
    # 处理已支付的订单
    t = request.GET.get('t', '')

    payTime = request.session.get('payTime', '')
    if t and payTime and t == payTime:
        payInfo = request.session.get('payInfo', '')
        OrderInfo.objects.create(**payInfo)
        del request.session['payTime']
        del request.session['payInfo']

    # 根据当前用户查询用户订单信息
    orderInfos = OrderInfo.objects.filter(user_id=request.user.id).order_by('-created')
    # 分页功能
    paginator = Paginator(orderInfos, 7)
    try:
        pages = paginator.page(p)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    return render(request, 'shopper.html', locals())


def logoutView(request):
    # 使用内置函数logout退出用户登录状态
    logout(request)
    # 网页自动跳转到首页
    return redirect(reverse('index:index'))


@login_required(login_url='/shopper/login.html')
def shopcartView(request):
    title = '我的购物车'
    classContent = 'shopcarts'
    id = request.GET.get('id', '')
    quantity = request.GET.get('quantity', 1)
    userID = request.user.id
    if id:
        CartInfo.objects.update_or_create(commodityInfos_id=id, user_id=userID, quantity=quantity)
        return redirect('shopper:shopcart')
    getUserId = CartInfo.objects.filter(user_id=userID)
    commodityDcit = {x.commodityInfos_id: x.quantity for x in getUserId}
    commodityInfos = CommodityInfo.objects.filter(id__in=commodityDcit.keys())
    return render(request, 'shopcart.html', locals())


def deleteAPI(request):
    result = {'state': 'success'}
    userId = request.GET.get('userId', '')
    commodityId = request.GET.get('commodityId', '')
    if userId:
        CartInfo.objects.filter(user_id=userId).delete()
    elif commodityId:
        CartInfo.objects.filter(commodityInfos_id=commodityId).delete()
    else:
        result = {'state': 'fail'}
    return JsonResponse(result)


def paysView(request):
    total = request.GET.get('total', 0)
    total = float(str(total).replace('￥', ''))
    if total:
        out_trade_no = str(int(time.time()))
        payInfo = dict(price=total, user_id=request.user.id, state='已支付')
        request.session['payInfo'] = payInfo
        request.session['payTime'] = out_trade_no
        return_url = 'http://' + request.get_host() + '/shopper.html'
        url = get_pay(out_trade_no, total, return_url)
        return redirect(url)
    else:
        return redirect('shopper:shopcart')


def loginView1(request):
    title = "用户登录"
    class_content = "logins"

    # 处理POST请求
    if request.method == "POST":
        infos = LoginForm(data=request.POST)

        # 验证表单字段的数据是否正确
        if infos.is_valid():
            username = infos.cleaned_data.get("username")
            password = infos.cleaned_data.get("password")

            if User.objects.filter(username=username):
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    return redirect(reverse("shopper:shopper"))
            else:
                state = "注册成功"
                d = dict(
                    username=username,
                    password=password,
                    is_staff=1,
                    is_active=1
                )
                # 创建用户账号数据
                user = User.objects.create_user(**d)
                user.save()
        else:
            error_msg = infos.errors.as_json()
            print(error_msg)
    # 处理GET请求
    else:
        infos = LoginForm()

    return render(request, "login.html", locals())


def loginView2(request):
    title = "用户登录"
    class_content = "logins"

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        # 查询username的数据是否在内置模型User
        if User.objects.filter(username=username):
            # 验证账号密码是否和内置User账号密码一致
            user = authenticate(username=username, password=password)

            # 验证成功，跳转登录
            if user:
                login(request, user)
                return redirect(reverse("shopper:shopper"))
        # 否则username数据不在内置模型User里
        else:
            state = "注册成功"
            d = dict(
                username=username,
                password=password,
                is_staff=1,
                is_active=1
            )
            # 创建用户账号数据
            user = User.objects.create_user(**d)
            user.save()

    return render(request, "login.html", locals())


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=11,
        label="请您输入手机号",
        widget=forms.widgets.TextInput(
            attrs={
                "class": "layui-input",
                "placeholder": "请您输入手机号",
                "lay-verify": "required|phone",
                "id": "username"
            }
        ))
    password = forms.CharField(
        max_length=20,
        label="请您输入密码",
        widget=forms.widgets.PasswordInput(
            attrs={
                "class": "layui-input",
                "placeholder": "请您输入密码",
                "lay-verify": "required|password",
                "id": "password"
            }
        ))

    def clean_username(self):
        if len(self.cleaned_data["username"]) == 11:
            return self.cleaned_data["username"]
        else:
            raise ValidationError("用户名为手机号")
