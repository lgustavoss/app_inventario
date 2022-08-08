from django.urls import path
from .views.usuario_views import *


urlpatterns = [
    path('cadastrar', cadastrar_usuario, name='cadastrar_usuario'),
    path('', logar_usuario, name='login'),
    path('logout', deslogar_usuario, name='logout'),
    path('alterar_senha', alterar_senha, name='alterar_senha'),
]
