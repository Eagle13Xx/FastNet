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
            return redirect('loginuser')
        else:
            messages.error(request, 'Erro ao cadastrar usuário. Verifique os dados.')
        return render(request, 'usuario/cadusuario.html', {'form': form})

class LoginUsuarioView(View):
    def get(self, request):
        return render(request, 'usuario/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('/')
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos.')
            return render(request, 'usuario/login.html')

class LogoutUsuarioView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Você saiu da sua conta.')
        return redirect('home')