import email
from ..models import Usuario


def cadastrar_usuario(usuario):
    usuario = Usuario.objects.create_user(
        nome=usuario.nome, email=usuario.email, tipo=usuario.tipo, password=usuario.password)
    usuario.save()


def listar_usuarios():
    return Usuario.objects.all().order_by("Nome")