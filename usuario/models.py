from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from .manager import UsuarioManager


# Criando o cadastro de usuários
class Usuario(AbstractBaseUser):
    objects = UsuarioManager()

    TIPO_USUARIO_CHOICES = (
        (1, 'Basico'),
        (2, 'Intermediário'),
        (3, 'Administrador')
    )

    nome = models.CharField(max_length=60, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    tipo = models.IntegerField(choices=TIPO_USUARIO_CHOICES, null=False, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS: ['nome', 'tipo']

    def __str__(self):
        return self.email