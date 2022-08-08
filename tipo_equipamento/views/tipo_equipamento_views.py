from django.shortcuts import render, redirect
from ..forms.tipo_equipamentos_forms import TipoEquipamentoForm
from ..entidades import tipo_equipamento
from ..services import tipo_equipamento_service
from django.contrib.auth.decorators import login_required


# Listagem de tipos de Equipamentos

def listar_tipoEquipamentos(request):
    tipoEquipamentos = tipo_equipamento_service.listar_tipoEquipamentos()
    tipoEquipamentosAtivos = tipo_equipamento_service.listar_tipoEquipamento_ativo()
    tipoEquipamentosInativos = tipo_equipamento_service.listar_tipoEquipamento_inativo()
    return render(request, 'list_tipo.html', {
        'tipoEquipamentos': tipoEquipamentos,
        'tipoEquipamentosAtivos': tipoEquipamentosAtivos,
        'tipoEquipamentosInativos': tipoEquipamentosInativos})


# Cadastro de Tipos de Equipamentos

def cadastrar_tipoEquipamentos(request):
    if request.user.is_authenticated and request.user.tipo != 1:
        if request.method == "POST":
            form_tipoEquipamento = TipoEquipamentoForm(request.POST or None)
            if form_tipoEquipamento.is_valid():
                tipo = form_tipoEquipamento.cleaned_data["tipo"]
                status = form_tipoEquipamento.cleaned_data["status"]
                tipoEquipamento_novo = tipo_equipamento.TipoEquipamento(
                    tipo=tipo, status=status)
                tipo_equipamento_service.cadastrar_tipoEquipamento(
                    tipoEquipamento_novo)
                return redirect('listar_tipos_equipamentos')
        else:
            form_tipoEquipamento = TipoEquipamentoForm()
        return render(request, 'cad_tipo.html', {'form_tipoEquipamento': form_tipoEquipamento})


# Editando os tipos de Equipamentos

def editar_tipoEquipamento(request, id):
    if request.user.is_authenticated and request.user.tipo != 1:
        tipoEquipamento_editar = tipo_equipamento_service.listar_tipoEquipamento_id(
            id)
        form_tipoEquipamento = TipoEquipamentoForm(
            request.POST or None, instance=tipoEquipamento_editar)
        if form_tipoEquipamento.is_valid():
            tipo = form_tipoEquipamento.cleaned_data["tipo"]
            status = form_tipoEquipamento.cleaned_data["status"]
            tipoEquipamento_novo = tipo_equipamento.TipoEquipamento(
                tipo=tipo, status=status)
            tipo_equipamento_service.editar_tipoEquipamento(
                tipoEquipamento_editar, tipoEquipamento_novo)
            return redirect('listar_tipos_equipamentos')
        return render(request, 'cad_tipo.html', {'form_tipoEquipamento': form_tipoEquipamento})
