import re
from django import forms
from django.contrib.auth.models import User


def email_check(email):
    pattern = re.compile(r"[a-zA-Z0-9_-]+@\w+\.\w+")
    # pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
    return re.match(pattern, email)


class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20)
    email = forms.CharField(label='邮箱',)
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput)

    def clean_username(self):
        # 此处验证注册用户名 1.验证账号长度 2.验证用户名是否已经存在
        # 没有对用户名进行类型限制
        username = self.cleaned_data.get('username')
        if len(username) < 5 or len(username) > 20:
            raise forms.ValidationError("请输入5-20个字符的用户名")
        else:
            filter_result = User.objects.filter(username=username)
            if filter_result:
                raise forms.ValidationError('用户名已存在')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email_check(email):
            filter_result = User.objects.filter(email=email)
            if filter_result:
                raise forms.ValidationError('当前邮箱已使用')
        else:
            raise forms.ValidationError('你输入的邮箱格式不正确')
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8 or len(password1) > 20:
            raise forms.ValidationError("密码最少8位，最长20位")
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2 and password2 and password1:
            raise forms.ValidationError("两次密码不匹配")
        return password2


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=50, widget=forms.TextInput(attrs={'class': 'name_input', 'placeholder': '请输入用户名'}))
    password = forms.CharField(label='密码',widget=forms.PasswordInput(attrs={'class': 'pass_input', 'placeholder': '请输入密码'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if email_check(username):
            filter_result = User.objects.filter(email=username)
            if not filter_result:
                raise forms.ValidationError('当前邮箱不存在')
        else:
            filter_result = User.objects.filter(username=username)
            if not filter_result:
                raise forms.ValidationError('当前用户不存在')
        return username
