from django.contrib.auth.forms import AuthenticationForm, UserCreationForm # формы для авторизации и создании пользователей
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

class UserRegistrationForm(UserCreationForm):
    """Класс формы для создание пользовавтелей"""
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите фамилию'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'
    }))
    password1= forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control py-4','placeholder':'Введите пароль'
    }))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control py-4','placeholder':'Подьвердите пароль'
    }))
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')