from django.urls import path
from .views import colaborador_views

urlpatterns = [
    path('cadastrar', colaborador_views.cadastrar_colaboradores,
         name='cadastrar_colaborador'),
    path('listar', colaborador_views.listar_colaboradores,
         name='listar_colaboradores'),
    path('editar/<int:id>', colaborador_views.editar_colaborador,
         name='editar_colaborador'),
]
