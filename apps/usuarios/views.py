from django.shortcuts import get_object_or_404, redirect, render
from django.urls.conf import path
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita


def cadastro(request):
    """
    Realiza o cadastro das pessoas ao sistema
    """
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request, 'O campo email não pode ficar em branco')
            return redirect('cadastro')
        if password != password2:
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado!')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Este nome de usuário já existe!')
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=password)
        user.save()
        messages.success(request, 'Usuário criado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    """
    Realiza o login de uma pessoa no sistema
    """
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['senha']
        if email.strip() == '' or password.strip() == '':
            messages.error(request, "Os campos 'e-mail' e 'senha' não podem ficar em branco!")
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Senha incorreta!')
                return redirect('login')
        else:
            messages.error(request, 'Este e-mail não existe!')
            return redirect('login')
    return render(request, 'usuarios/login.html')

def logout(request):
    """
    Realiza o logout do usuário do sistema
    """
    auth.logout(request)
    return redirect('homepage')

def dashboard(request):
    """
    Mostra a página de receitas do usuário logado
    """
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id)
        
        context = {
            'receitas': receitas
        }

        return render(request, 'usuarios/dashboard.html', context)
    else:
        return redirect('homepage')

def campo_vazio(campo):
    return not campo.strip()
