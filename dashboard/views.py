from http.client import HTTPResponse
from itertools import count
from django.shortcuts import render
from equipamento.models import Equipamento
from empresa.models import Empresa
from colaborador.models import Colaborador
from tipo_equipamento.models import TipoEquipamento
from django.http import JsonResponse
from django.db.models import Sum, Count

# Create your views here.
def home(request):
    return render(request, 'dashboard.html')


#Função que retorna a quantidade de equipamentos cadastrados
def retorna_total_equipamentos(request):
    total = Equipamento.objects.all().aggregate(Count('status'))['status__count']
    totalAtivo = Equipamento.objects.all().aggregate(Sum('status'))['status__sum']
    totalInativo = total - totalAtivo

    data = [totalAtivo, totalInativo]
    labels = ['Ativo', 'Inativo']

    data_json = {'data': data, 'labels': labels}
    return JsonResponse(data_json)


#Função que retorna a quantidade de empresas cadastradas
def retorna_total_empresas(request):
    total = Empresa.objects.all().aggregate(Count('status'))['status__count']
    totalAtivo = Empresa.objects.all().aggregate(Sum('status'))['status__sum']
    totalInativo = total - totalAtivo

    data = [totalAtivo, totalInativo]
    labels = ['Ativo', 'Inativo']

    data_json = {'data': data, 'labels': labels}
    return JsonResponse(data_json)


#Função que retorna a quantidade de colaboradores cadastradas
def retorna_total_colaboradores(request):
    total = Colaborador.objects.all().aggregate(Count('status'))['status__count']
    totalAtivo = Colaborador.objects.all().aggregate(Sum('status'))['status__sum']
    totalInativo = total - totalAtivo

    data = [totalAtivo, totalInativo]
    labels = ['Ativo', 'Inativo']

    data_json = {'data': data, 'labels': labels}
    return JsonResponse(data_json)


#Função que retorna a quantidade de equipamentpos por empresa
def retorna_equipamento_empresa(request):
    equipamentos = Equipamento.objects.filter(status=True)
    emp = Empresa.objects.filter(status=True)

    labels = []
    data = []
    
    for empresa in emp:
        labels.append(empresa.nome)
        x = sum([equip.status for equip in equipamentos if equip.empresa_id == empresa.id])
        
        data.append(x)    
        
    data_json = {'labels': labels, 'data': data}

    return JsonResponse(data_json)



#Função que retorna a quantidade de equipamentpos por tipo
def retorna_equipamento_tipo(request):
    equipamentos = Equipamento.objects.filter(status=True)
    tipo = TipoEquipamento.objects.filter(status=True)

    labels = []
    data = []
    
    for tipoEquipamento in tipo:
        labels.append(tipoEquipamento.tipo)
        x = sum([equip.status for equip in equipamentos if equip.tipo_equipamento_id == tipoEquipamento.id])
        
        data.append(x)    
        
    data_json = {'labels': labels, 'data': data}

    return JsonResponse(data_json)

