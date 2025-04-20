from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django import forms

class UserLoginForm(AuthenticationForm):
    """Класс формы для авторизации пользователей"""
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control py-4','placeholder':'Введите имя пользователя'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control py-4','placeholder':'Введите пароль'
    }))
    class Meta:
        model = User  # будем работать с полем User
        fields = ('username','password')  # Поля в форме

