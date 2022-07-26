from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from .manager import UsuarioManager


# Criando o cadastro de usuários
class Usuario(AbstractBaseUser):
    objects = UsuarioManager()

    nome = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS: 'nome'
