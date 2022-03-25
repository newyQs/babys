from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginModelForm(forms.ModelForm):
    """登录表单"""

    class Meta:
        model = User
        fields = ("username", "password")

        labels = {
            "username": "请您输入手机号",
            "password": "请您输入密码"
        }

        error_messages = {
            "__all__": {
                "required": "请输入内容",
                "invalid": "请检查输入内容"
            }
        }
        widgets = {
            "username": forms.widgets.TextInput(
                attrs={
                    "class": "layui-input",
                    "placeholder": "请您输入手机号",
                    "lay-verify": "required|phone",
                    "id": "username"
                }
            ),
            "password": forms.widgets.PasswordInput(
                attrs={
                    "class": "layui-input",
                    "placeholder": "请您输入密码",
                    "lay-verify": "required|password",
                    "id": "password"
                }
            )
        }

    def clean_username(self):
        if len(self.cleaned_data["username"]) == 11:
            return self.cleaned_data["username"]
        else:
            raise ValidationError("用户名为手机号")
