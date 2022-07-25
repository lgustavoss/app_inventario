from ..models import Empresa


def cadastrar_empresa(empresa):
    Empresa.objects.create(nome=empresa.nome, cnpj=empresa.cnpj, status=empresa.status)


def listar_empresas():
    return Empresa.objects.all().order_by("nome")


def listar_empresa_id(id):
    return Empresa.objects.get(id=id)



def editar_empresa(empresa, empresa_novo):
    empresa.nome = empresa_novo.nome
    empresa.cnpj = empresa_novo.cnpj
    empresa.status = empresa_novo.status
    empresa.save(force_update=True)
