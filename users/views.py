from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth         # Используем для того чтобы понять существует ли такой пользователь

from .models import  User
from users.forms import UserLoginForm

def login(request):
    """   Функция для регистрации пользователей  """
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            # Провряем форму на валидность
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username,password=password)   # Проверяем на подлинность
            if user:
                """Если есть такой пользователь в базе то авторизуем его """
                auth.login(request,user)
                return HttpResponseRedirect('/')
    else:
        form = UserLoginForm()
    context = {"forms":form}
    return render(request,'users/login.html',context)

def registration(request):
    return render(request,'users/registration.html')

