from django.urls import path
from .views import empresa_views

urlpatterns = [
    path('cadastrar', empresa_views.cadastrar_empresas,
         name='cadastrar_empresa'),
    path('listar', empresa_views.listar_empresas,
         name='listar_empresas'),
    path('editar/<int:id>', empresa_views.editar_empresa,
         name='editar_empresa'),
    path('listar_empresa/<int:id>',
         empresa_views.listar_empresa_id, name='listar_empresa_id'),
    path('erro_empresa',
         empresa_views.erro_inativar, name='erro_empresa'),
]
