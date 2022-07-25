from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('retorna_total_equipamentos', views.retorna_total_equipamentos,
         name="retorna_total_equipamentos"),
    path('retorna_total_empresas', views.retorna_total_empresas,
         name="retorna_total_empresas"),
    path('retorna_total_colaboradores', views.retorna_total_colaboradores,
         name="retorna_total_colaboradores"),
    path('retorna_equipamento_empresa', views.retorna_equipamento_empresa,
         name="retorna_equipamento_empresa"),
    path('retorna_equipamento_tipo', views.retorna_equipamento_tipo,
         name="retorna_equipamento_tipo"),
]
