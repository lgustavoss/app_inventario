from ..models import TipoEquipamento


def cadastrar_tipoEquipamento(tipoEquipamento):
    TipoEquipamento.objects.create(tipo=tipoEquipamento.tipo, status=tipoEquipamento.status)


def listar_tipoEquipamentos():
    return TipoEquipamento.objects.all().order_by("tipo")


def listar_tipoEquipamento_id(id):
    return TipoEquipamento.objects.get(id=id)


def listar_tipoEquipamento_ativo():
    return TipoEquipamento.objects.filter(status=True)


def listar_tipoEquipamento_inativo():
    return TipoEquipamento.objects.filter(status=False)


def editar_tipoEquipamento(tipoEquipamento, tipoEquipamento_novo):
    tipoEquipamento.tipo = tipoEquipamento_novo.tipo
    tipoEquipamento.save(force_update=True)
