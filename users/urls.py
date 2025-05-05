from django.contrib.auth.decorators import login_required  # Декоратр доступа

from django.urls import path
from users.views import login,UserRegistrationView,UserProfileView,logout

app_name = "users"

urlpatterns = [
    path("login/",login, name='login'),
    path("registration/",UserRegistrationView.as_view(), name='registration'),
    path("profile/<int:pk>/",login_required(UserProfileView.as_view()), name='profile'),
    path("logout/",logout, name='logout'),  # Выход из системы
]

