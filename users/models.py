from django.db import models
from django.contrib.auth.models import AbstractUser  # угследуемся от существующего класса для работы с пользовательями

class User(AbstractUser):
    ''' Расширяем существующий класс '''
    image = models.ImageField(upload_to="users_images",null=True, blank=True)

