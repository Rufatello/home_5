from django.db import models
from django.contrib.auth.models import AbstractUser
from catalog.models import NO


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    avatar = models.ImageField(upload_to='users_photo/', verbose_name='Аватар', **NO)
    country = models.CharField(max_length=150, verbose_name='Страна', **NO)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NO)
    is_active = models.BooleanField(default=False, verbose_name='Активность')
    code = models.CharField(max_length=15, verbose_name='код', **NO)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
