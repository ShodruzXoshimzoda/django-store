from django.shortcuts import render, HttpResponseRedirect,reverse
from django.contrib import auth,messages       # Используем для того чтобы понять существует ли такой пользователь
# messages исполльзуется для сообщениё пользователью
from .models import  User
from users.forms import UserLoginForm, UserRegistrationForm,UserPofileForm

def login(request):
    """   Авторизации пользователей """
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
                return HttpResponseRedirect(reverse("users:profile"))
    else:
        form = UserLoginForm()
    context = {"forms":form}
    return render(request,'users/login.html',context)

def registration(request):
    '''   Регистрации пользователей      '''
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем вы успешно зарегистрировались! ')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form':form}
    return render(request,'users/registration.html',context)

def profile(request):
    '''  Профиль пользователья   '''
    if request.method == "POST":
        form = UserPofileForm(instance=request.user,data=request.POST,files=request.FILES)
        ''' instance=request.user - обновляет форму для текущего плзователья '''
        if form.is_valid():
            form.save()
            # messages.success(request,'Ваши страничка была обновлене')
            return HttpResponseRedirect(reverse("users:profile"))
    else:
        form = UserPofileForm(instance=request.user)    # instance request.user - мы получаем объект пользователья
    context = {"title":"Store-Профиль",'form':form} # Форма будет заполнена данными о пользователе
    return render(request, 'users/profile.html',context)

def logout(request):
    """ Выход из системы  """
    auth.logout(request)  # выходим изсистемы
    return HttpResponseRedirect(reverse('index'))