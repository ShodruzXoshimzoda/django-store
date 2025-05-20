from django.db import models
from django.contrib.auth.models import AbstractUser  # угследуемся от существующего класса для работы с пользовательями
from django.core.mail import send_mail

class User(AbstractUser):
    ''' Расширяем существующий класс '''
    image = models.ImageField(upload_to="users_images",null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)       # Подтвердил ли пользователь email

class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)    # Уникальный идентификатор для польлзователья
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField() # Время окончания ссылки

    def __str__(self):
        return f'Email verifaction for {self.user.email}'
    
    def send_email_verification(self):
        send_mail(
            'Subject here',
            'Test verification email',
            'from@example.com',
            [self.user.email],
            fail_silently=False
            )

    
