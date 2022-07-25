from django.shortcuts import render, redirect

from ..forms import equipamento_forms
from ..services import equipamento_service
from ..entidades import equipamento



# Listagem de equipamentos
def listar_equipamentos(request):
    equipamentos = equipamento_service.listar_equipamentos()
    equipamentosAtivos = equipamento_service.listar_equipamento_ativo()
    equipamentosInativos = equipamento_service.listar_equipamento_inativo()
    return render(request, 'list_equipamento.html', {
        'equipamentos': equipamentos,
        'equipamentosAtivos': equipamentosAtivos, 
        'equipamentosInativos': equipamentosInativos})


# Listando equipamento e seus detalhes
def listar_equipamento_id(request, id):
    equipamentos = equipamento_service.listar_equipamento_id(id)
    return render(request, 'list_equipamento.html', {'equipamento': equipamentos})


# Cadastro de Equipamentos
def cadastrar_equipamento(request):
    if request.method == "POST":
        form_equipamento = equipamento_forms.EquipamentoForm(request.POST)
        if form_equipamento.is_valid():
            tag_patrimonio = form_equipamento.cleaned_data["tag_patrimonio"]
            tipo_equipamento = form_equipamento.cleaned_data["tipo_equipamento"]
            pedido = form_equipamento.cleaned_data["pedido"]
            data = form_equipamento.cleaned_data["data"]
            situacao = form_equipamento.cleaned_data["situacao"]
            empresa = form_equipamento.cleaned_data["empresa"]
            colaborador = form_equipamento.cleaned_data["colaborador"]
            marca = form_equipamento.cleaned_data["marca"]
            modelo = form_equipamento.cleaned_data["modelo"]
            especificacoes = form_equipamento.cleaned_data["especificacoes"]
            acesso_remoto = form_equipamento.cleaned_data["acesso_remoto"]
            acesso_id = form_equipamento.cleaned_data["acesso_id"]
            acesso_senha = form_equipamento.cleaned_data["acesso_senha"]
            observacao = form_equipamento.cleaned_data["observacao"]
            status = form_equipamento.cleaned_data["status"]
            equipamento_novo = equipamento.Equipamento(tag_patrimonio=tag_patrimonio,
                                                    tipo_equipamento=tipo_equipamento,
                                                    pedido=pedido, data=data,
                                                    situacao=situacao, empresa=empresa,
                                                    colaborador=colaborador, marca=marca,
                                                    modelo=modelo, especificacoes=especificacoes,
                                                    acesso_remoto=acesso_remoto, acesso_id=acesso_id,
                                                    acesso_senha=acesso_senha, observacao=observacao,
                                                    status=status)
            equipamento_service.cadastrar_equipamento(equipamento_novo)
            return redirect('listar_equipamentos')
    else:
        form_equipamento = equipamento_forms.EquipamentoForm()
    return render(request, 'cad_equipamento.html', {'form_equipamento': form_equipamento})


# Editando os equipamentos
def editar_equipamento(request, id):
    equipamento_editar = equipamento_service.listar_equipamento_id(id)
    if equipamento_editar.data is not None:
        equipamento_editar.data = equipamento_editar.data.strftime('%Y-%m-%d')
    form_equipamento = equipamento_forms.EquipamentoForm(
        request.POST or None, instance=equipamento_editar)
    if form_equipamento.is_valid():
        tag_patrimonio = form_equipamento.cleaned_data["tag_patrimonio"]
        tipo_equipamento = form_equipamento.cleaned_data["tipo_equipamento"]
        pedido = form_equipamento.cleaned_data["pedido"]
        data = form_equipamento.cleaned_data["data"]
        situacao = form_equipamento.cleaned_data["situacao"]
        empresa = form_equipamento.cleaned_data["empresa"]
        colaborador = form_equipamento.cleaned_data["colaborador"]
        marca = form_equipamento.cleaned_data["marca"]
        modelo = form_equipamento.cleaned_data["modelo"]
        especificacoes = form_equipamento.cleaned_data["especificacoes"]
        acesso_remoto = form_equipamento.cleaned_data["acesso_remoto"]
        acesso_id = form_equipamento.cleaned_data["acesso_id"]
        acesso_senha = form_equipamento.cleaned_data["acesso_senha"]
        observacao = form_equipamento.cleaned_data["observacao"]
        status = form_equipamento.cleaned_data["status"]
        equipamento_novo = equipamento.Equipamento(tag_patrimonio=tag_patrimonio,
                                                   tipo_equipamento=tipo_equipamento,
                                                   pedido=pedido, data=data,
                                                   situacao=situacao, empresa=empresa,
                                                   colaborador=colaborador, marca=marca,
                                                   modelo=modelo, especificacoes=especificacoes,
                                                   acesso_remoto=acesso_remoto, acesso_id=acesso_id,
                                                   acesso_senha=acesso_senha, observacao=observacao,
                                                   status=status)
        equipamento_service.editar_equipamento(equipamento_editar, equipamento_novo)
        return redirect('listar_equipamentos')
    return render(request, 'cad_equipamento.html', {'form_equipamento': form_equipamento})
