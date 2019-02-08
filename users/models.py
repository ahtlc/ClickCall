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
    function = models.CharField(max_length=50, default='Colaborador')
    phone = models.CharField(max_length=15)
    ramal = models.CharField(max_legth=15)
    sector = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.username + " (" + self.email + ") "
