from os import stat
from django.shortcuts import render, redirect

from ..forms.empresa_forms import EmpresaForm
from ..entidades.empresa import Empresa
from ..services import empresa_service
from equipamento.services import equipamento_service


# Listagem de empresas
def listar_empresas(request):
    empresas = empresa_service.listar_empresas()
    return render(request, 'list_empresa.html', {'empresas': empresas})


# Listando empresa e seus equipamentos
def listar_empresa_id(request, id):
    empresa = empresa_service.listar_empresa_id(id)
    equipamentos = equipamento_service.listar_equipamento_empresa(id)
    return render(request, 'equip_empresa.html', {'empresa': empresa, 'equipamentos': equipamentos})


# erro
def erro_inativar(request):
    return render(request, 'erro_empresa.html')



# Cadastro de empresas
def cadastrar_empresas(request):
    if request.method == "POST":
        form_empresa = EmpresaForm(request.POST)
        if form_empresa.is_valid():
            nome = form_empresa.cleaned_data["nome"]
            cnpj = form_empresa.cleaned_data["cnpj"]
            status = form_empresa.cleaned_data["status"]
            empresa_novo = Empresa(nome=nome, cnpj=cnpj, status=status)
            empresa_service.cadastrar_empresa(empresa_novo)
            return redirect('listar_empresas')
    else:
        form_empresa = EmpresaForm()
    return render(request, 'cad_empresa.html', {'form_empresa': form_empresa})


# Editando empresas
def editar_empresa(request, id):
    empresa_editar = empresa_service.listar_empresa_id(id)
    equipamentos = equipamento_service.listar_equipamento_empresa(id)
    form_empresa = EmpresaForm(request.POST or None, instance=empresa_editar)
    if form_empresa.is_valid():
        nome = form_empresa.cleaned_data["nome"]
        cnpj = form_empresa.cleaned_data["cnpj"]
        status = form_empresa.cleaned_data["status"]
        if status == True:
            empresa_novo = Empresa(nome=nome, cnpj=cnpj, status=status)
            empresa_service.editar_empresa(empresa_editar, empresa_novo)
            return redirect('listar_empresas')
        else:
            if len(equipamentos) == 0 or status == True:
                empresa_novo2 = Empresa(nome=nome, cnpj=cnpj, status=status)
                empresa_service.editar_empresa(empresa_editar, empresa_novo2)
                return redirect('listar_empresas')
            else:
                empresa = empresa_service.listar_empresa_id(id)
                equipamentos = equipamento_service.listar_equipamento_empresa(id)
                return render(request, 'erro_empresa.html', {'empresa': empresa, 'equipamentos': equipamentos})
    return render(request, 'cad_empresa.html', {'form_empresa': form_empresa})
