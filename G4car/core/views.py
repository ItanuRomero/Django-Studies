from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'core/index.html')


@login_required
def cadastro_cliente(request):
    return render(request, 'core/cadastro_cliente.html')


@login_required
def listagem_clientes(request):
    return render(request, 'core/listagem_clientes.html')


@login_required
def cadastro_veiculo(request):
    return render(request, 'core/cadastro_veiculo.html')

@login_required
def listagem_veiculos(request):
    return render(request, 'core/listagem_veiculos.html')