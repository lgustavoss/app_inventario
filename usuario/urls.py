from django.urls import path
from .views import usuario_views

urlpatterns = [
    path('cadastrar', usuario_views.cadastrar_usuario,
         name='cadastrar_usuario'),
]
