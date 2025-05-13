from django.shortcuts import render, HttpResponseRedirect,reverse
from django.contrib import auth,messages       # Используем для того чтобы понять существует ли такой пользователь
# messages исполльзуется для сообщениё пользователью
from django.contrib.auth.decorators import login_required  # Декоратр доступа
from .models import  User
from users.forms import UserLoginForm, UserRegistrationForm,UserPofileForm
from products.models import Basket
from django.views.generic.edit import CreateView,UpdateView
from django.urls import reverse,reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
# def login(request):
#     """   Авторизации пользователей """
#     if request.method == "POST":
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             # Провряем форму на валидность
#             username = request.POST['username']
#             password = request.POST['password']

#             user = auth.authenticate(username=username,password=password)   # Проверяем на подлинность
#             if user:
#                 """Если есть такой пользователь в базе то авторизуем его """
#                 auth.login(request,user)
#                 return HttpResponseRedirect(reverse("index"))
#     else:
#         form = UserLoginForm()
#     context = {"forms":form}
#     return render(request,'users/login.html',context)

# def registration(request):
#     '''   Регистрации пользователей      '''
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Поздравляем вы успешно зарегистрировались! ')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegistrationForm()
#     context = {'form':form}
#     return render(request,'users/registration.html',context)

# @login_required
# def profile(request):
#     '''  Профиль пользователья   '''
#     if request.method == "POST":
#         form = UserPofileForm(instance=request.user,data=request.POST,files=request.FILES)
#         ''' instance=request.user - обновляет форму для текущего плзователья '''
#         if form.is_valid():
#             form.save()
#             # messages.success(request,'Ваши страничка была обновлене')
#             return HttpResponseRedirect(reverse("users:profile"))
#     else:
#         form = UserPofileForm(instance=request.user)    # instance request.user - мы получаем объект пользователья
#     context = {"title":"Store-Профиль",
#                'form':form,                               # Форма будет заполнена данными о пользователе
#                'baskets':Basket.objects.filter(user=request.user)              # Берём в корзину те товары которые принадлежать ему
#                }
#     return render(request, 'users/profile.html',context)

# def logout(request):
#     """ Выход из системы  """
#     auth.logout(request)  # выходим из системы
#     return HttpResponseRedirect(reverse('index'))


'''Классовеое представление'''

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm


class UserRegistrationView(SuccessMessageMixin,CreateView):
    ''' Классовое представление для странички регистрации'''
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Поздравляем вы успешно зарегистрировались! '

    def get_context_data(self, **kwargs):
        context = super(UserRegistrationView,self).get_context_data()
        context['title'] = 'Store - страничка Регистраци'
        
        return context
    

class UserProfileView(UpdateView):
    '''Классвое представдение для личного кабинета'''
    model = User
    form_class = UserPofileForm
    template_name =  'users/profile.html'

    def get_success_url(self):
        # Для обновлеления 
        return reverse_lazy('users:profile',args = (self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView,self).get_context_data()
        context['title'] = 'Store - Личный кабинет'
        context['baskets'] = Basket.objects.filter(user=self.request.user)    
        
        return context


