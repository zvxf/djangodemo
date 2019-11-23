from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=16)
    password = forms.CharField(max_length=32)


class RegForm(forms.Form):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField()
    wechat = forms.CharField()
    password = forms.CharField()


class CommentForm(forms.Form):
    com_title = forms.CharField(min_length=4,max_length=16)
    com_body = forms.CharField(min_length=12,max_length=120)
