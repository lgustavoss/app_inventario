from ..models import Colaborador


def cadastrar_colaborador(colaborador):
    Colaborador.objects.create(nome=colaborador.nome, cpf=colaborador.cpf, status=colaborador.status)


def listar_colaboradores():
    return Colaborador.objects.all().order_by("nome")


def listar_colaborador_id(id):
    return Colaborador.objects.get(id=id)


def editar_colaborador(colaborador, colaborador_novo):
    colaborador.nome = colaborador_novo.nome
    colaborador.cpf = colaborador_novo.cpf
    colaborador.save(force_update=True)
