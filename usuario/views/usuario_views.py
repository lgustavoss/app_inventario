from multiprocessing import AuthenticationError
from turtle import update
from django.shortcuts import render, redirect
from ..forms.usuario_forms import UsuarioForm
from ..forms.login_forms import LoginForm
from ..entidades.usuario import Usuario
from ..services import usuario_service
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UsuarioForm(data=request.POST)
        if form_usuario.is_valid():
            nome = form_usuario.cleaned_data["nome"]
            email = form_usuario.cleaned_data["email"]
            tipo = form_usuario.cleaned_data["tipo"]
            password1 = form_usuario.cleaned_data["password1"]
            usuario_novo = Usuario(nome=nome, email=email, tipo=tipo, password=password1)
            usuario_service.cadastrar_usuario(usuario_novo)
            return redirect('home')
    else:
            form_usuario = UsuarioForm()
    return render(request, 'cad_usuario.html', {'form_usuario': form_usuario})


def logar_usuario(request):
    if request.method == "POST":
        form_login = LoginForm(data=request.POST)
        if form_login.is_valid():
            username = form_login.cleaned_data["username"]
            password = form_login.cleaned_data["password"]
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                form_login = LoginForm()
    else:
        form_login = LoginForm()
    return render(request, 'login.html', {'form_login': form_login})


#Realizando logout de usuaro
def deslogar_usuario(request):
    logout(request)
    return redirect('login')


#Realizando login de usuário
@login_required()
def alterar_senha(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('home')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'alterar_senha.html', {'form_senha': form_senha})


#Listando usuários
def listar_usuarios(request):
    if request.user.is_authenticated and request.user.tipo == 3:
        usuarios = usuario_service.listar_usuario()
        return render(request, 'list_usuario.html', {'usuarios': usuarios})
