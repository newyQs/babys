from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, reverse, redirect
from django.contrib.auth import login, authenticate
from django.core.exceptions import ValidationError


def loginView(request):
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


def _loginView(request):
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
