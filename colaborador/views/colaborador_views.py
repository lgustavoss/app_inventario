from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms.colaborador_forms import ColaboradorForm
from ..entidades import colaborador
from ..services import colaborador_service


# Listagem de colaboradores
def listar_colaboradores(request):
    colaboradores = colaborador_service.listar_colaboradores()
    return render(request, 'list_colaborador.html', {'colaboradores': colaboradores})


# Cadastro de colaboradores
def cadastrar_colaboradores(request):
    if request.method == "POST":
        form_colaborador = ColaboradorForm(request.POST or None)
        if form_colaborador.is_valid():
            nome = form_colaborador.cleaned_data["nome"]
            cpf = form_colaborador.cleaned_data["cpf"]
            status = form_colaborador.cleaned_data["status"]
            colaborador_novo = colaborador.Colaborador(
                nome=nome, cpf=cpf, status=status)
            colaborador_service.cadastrar_colaborador(colaborador_novo)
            return redirect('listar_colaboradores')
        else:
            print(form_colaborador.errors)
            return render(request, 'cad_colaborador.html', {'form_colaborador': form_colaborador})
    else:
        form_colaborador = ColaboradorForm()
    return render(request, 'cad_colaborador.html', {'form_colaborador': form_colaborador})


# Editando colaboradores
def editar_colaborador(request, id):
    colaborador_editar = colaborador_service.listar_colaborador_id(id)
    form_colaborador = ColaboradorForm(
        request.POST or None, instance=colaborador_editar)
    if form_colaborador.is_valid():
        nome = form_colaborador.cleaned_data["nome"]
        cpf = form_colaborador.cleaned_data["cpf"]
        status = form_colaborador.cleaned_data["status"]
        colaborador_novo = colaborador.Colaborador(nome=nome, cpf=cpf, status=status)
        colaborador_service.editar_colaborador(colaborador_editar, colaborador_novo)
        return redirect('listar_colaboradores')
    return render(request, 'cad_colaborador.html', {'form_colaborador': form_colaborador})
