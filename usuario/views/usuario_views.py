from django.shortcuts import render, redirect
from ..forms.usuario_forms import UsuarioForm
from ..entidades.usuario import Usuario
from ..services import usuario_service


# Create your views here.
def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UsuarioForm(data=request.POST)
        if form_usuario.is_valid():
            nome = form_usuario.cleaned_data["nome"]
            email = form_usuario.cleaned_data["email"]
            password1 = form_usuario.cleaned_data["password1"]
            usuario_novo = Usuario(nome=nome, email=email, password=password1)
            usuario_service.cadastrar_usuario(usuario_novo)
            return redirect('home')
    else:
        form_usuario = UsuarioForm()
    return render(request, 'form_usuario.html', {'form_usuario': form_usuario})
