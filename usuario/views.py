from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from .forms import UsuarioForm

class CadastroUsuarioView(View):
    success_url = reverse_lazy('loginuser')
    def get(self, request):
        form = UsuarioForm()
        return render(request, 'usuario/cadusuario.html', {'form': form})


    def post(self, request):
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('loginuser')  # Alterar para a rota do login
        else:
            messages.error(request, 'Erro ao cadastrar usuário. Verifique os dados.')
        return render(request, 'usuario/cadusuario.html', {'form': form})

class LoginUsuarioView(View):
    def get(self, request):
        # Renderiza o formulário de login
        return render(request, 'usuario/login.html')

    def post(self, request):
        # Coleta os dados do formulário
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autentica o usuário
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login bem-sucedido
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('/')  # Altere para a rota desejada após login
        else:
            # Login falhou
            messages.error(request, 'Nome de usuário ou senha inválidos.')
            return render(request, 'usuario/login.html')

class LogoutUsuarioView(View):
    def get(self, request):
        # Faz o logout do usuário
        logout(request)
        messages.success(request, 'Você saiu da sua conta.')
        return redirect('home')