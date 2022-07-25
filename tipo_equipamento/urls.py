from django.urls import path
from .views import tipo_equipamento_views

urlpatterns = [
    path('cadastrar', tipo_equipamento_views.cadastrar_tipoEquipamentos,
         name='cadastrar_tipo_equipamento'),
    path('listar', tipo_equipamento_views.listar_tipoEquipamentos,
         name='listar_tipos_equipamentos'),
    path('editar/<int:id>',
         tipo_equipamento_views.editar_tipoEquipamento, name='editar_tipo_equipamento'),
]
