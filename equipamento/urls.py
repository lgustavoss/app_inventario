from django.urls import path
from .views import equipamento_views

urlpatterns = [
    path('cadastrar', equipamento_views.cadastrar_equipamento,
         name='cadastrar_equipamento'),
    path('listar', equipamento_views.listar_equipamentos,
         name='listar_equipamentos'),
    path('editar/<int:id>',
         equipamento_views.editar_equipamento, name='editar_equipamento'),
]
