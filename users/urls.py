from django.contrib.auth.decorators import login_required  # Декоратр доступа

from django.urls import path
from users.views import UserLoginView,UserRegistrationView,UserProfileView,EmailVerificationView
from django.contrib.auth.views import LogoutView

app_name = "users"

urlpatterns = [
    path("login/",UserLoginView.as_view(), name='login'),
    path("registration/",UserRegistrationView.as_view(), name='registration'),
    path("profile/<int:pk>/",login_required(UserProfileView.as_view()), name='profile'),
    path("logout/",LogoutView.as_view(), name='logout'),  # Выход из системы
    path("verify/<str:email>/<uuid:code>/",EmailVerificationView.as_view(), name='email_verification'),  # Выход из системы

]

