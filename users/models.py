from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom model to users of clickcall
    """

    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=50,
                                default='Undefined')
    avatar = models.ImageField(blank=True, default='default.avatar.png')
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
