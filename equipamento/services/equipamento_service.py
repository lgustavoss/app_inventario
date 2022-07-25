from multiprocessing import Event
from ..models import Equipamento


def cadastrar_equipamento(equipamento):
    equipamento_bd = Equipamento.objects.create(tag_patrimonio=equipamento.tag_patrimonio,
                                                tipo_equipamento=equipamento.tipo_equipamento,
                                                pedido=equipamento.pedido, data=equipamento.data,
                                                situacao=equipamento.situacao, empresa=equipamento.empresa,
                                                colaborador=equipamento.colaborador, marca=equipamento.marca,
                                                modelo=equipamento.modelo, especificacoes=equipamento.especificacoes,
                                                acesso_remoto=equipamento.acesso_remoto, acesso_id=equipamento.acesso_id,
                                                acesso_senha=equipamento.acesso_senha, observacao=equipamento.observacao,
                                                status=equipamento.status)
    equipamento_bd.save()


def listar_equipamentos():
    return Equipamento.objects.all()


def listar_equipamento_id(id):
    return Equipamento.objects.get(id=id)


def listar_equipamento_ativo():
    return Equipamento.objects.filter(status=True)


def listar_equipamento_inativo():
    return Equipamento.objects.filter(status=False)


def listar_equipamento_empresa(id):
    equipamentos = Equipamento.objects.filter(empresa=id).all()
    return equipamentos


def listar_equipamento_colaborador(id):
    equipamentos = Equipamento.objects.filter(colaborador=id).all()
    return equipamentos


def editar_equipamento(equipamento, equipamento_novo):
    equipamento.tag_patrimonio = equipamento_novo.tag_patrimonio
    equipamento.tipo_equipamento = equipamento_novo.tipo_equipamento
    equipamento.pedido = equipamento_novo.pedido
    equipamento.data = equipamento_novo.data
    equipamento.situacao = equipamento_novo.situacao
    equipamento.empresa = equipamento_novo.empresa
    equipamento.colaborador = equipamento_novo.colaborador
    equipamento.marca = equipamento_novo.marca
    equipamento.modelo = equipamento_novo.modelo
    equipamento.especificacoes = equipamento_novo.especificacoes
    equipamento.acesso_remoto = equipamento_novo.acesso_remoto
    equipamento.acesso_id = equipamento_novo.acesso_id
    equipamento.acesso_senha = equipamento_novo.acesso_senha
    equipamento.observacao = equipamento_novo.observacao
    equipamento.status = equipamento_novo.status
    equipamento.save(force_update=True)
