from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom model to users of clickcall
    """

    created = models.DateTimeField(auto_now_add=True,)
    updated = models.DateTimeField(auto_now=True)

    email = models.EmailField(unique=True)

    name = models.CharField(max_length=256,
                            verbose_name="Login")
    avatar = models.ImageField(blank=True, default='default.avatar.png')

    function = models.CharField(max_length=50, default='Colaborador',
                                verbose_name="Função")
    phone = models.CharField(max_length=15, verbose_name="Telefone")

    ramal = models.CharField(max_length=15, verbose_name="Ramal")

    sector = models.CharField(max_length=50, verbose_name="Área")

    is_staff = models.BooleanField(default=False)

    COLABORATOR = 'CO'
    SUPERVISOR = 'SU'

    FUNCTION_CHOICES = (
        (COLABORATOR, 'Colaborador'),
        (SUPERVISOR, 'Supervisor'),
    )

    function = models.CharField(
        max_length=2,
        choices=FUNCTION_CHOICES,
        default=COLABORATOR,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.email + "("+self.phone+" r "+self.ramal+")"
