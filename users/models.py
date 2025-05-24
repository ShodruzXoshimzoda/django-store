from django.db import models
from django.contrib.auth.models import AbstractUser  # угследуемся от существующего класса для работы с пользовательями
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.utils.timezone import now


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
        link = reverse('users:email_verification',kwargs={'email':self.user.email,'code':self.code})
        verification_link = f'{settings.DOMAIN_NAME }{link}'
        subject = f'Подтверждение учётной записи для {self.user.username}'
        message = 'Для подтверждения учётной записи для {} перейдите по ссылке: {}'.format(self.user.email,verification_link)



        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False
            )
    def is_expired(self):
        return True if now() >= self.expiration else False


    
