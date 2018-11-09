from django import forms
from .models import UserInfo


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    email = forms.EmailField(label='Email', )
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) < 6:
            raise forms.ValidationError("用户名必须大于6位.")
        elif len(username) > 20:
            raise forms.ValidationError("用户名太长了.")
        else:
            filter_result = UserInfo.objects.filter(username__exact=username)
        if len(filter_result) > 0:
            raise forms.ValidationError("用户名已经存在.")

        return username

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #
    #     if email_check(email):
    #         filter_result = User.objects.filter(email__exact=email)
    #     if len(filter_result) > 0:
    #         raise forms.ValidationError("Your email already exists.")
    #     else:
    #         raise forms.ValidationError("Please enter a valid email.")
    #
    #     return email

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 6:
            raise forms.ValidationError("密码必须大于6位.")
        elif len(password) > 20:
            raise forms.ValidationError("你的密码太长了.")

        return password


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean_username(self):

        username = self.cleaned_data.get('username')
        filter_result = UserInfo.objects.filter(username__exact=username)
        if not filter_result:
            raise forms.ValidationError("此用户名不存在。请先注册.")

        return username
