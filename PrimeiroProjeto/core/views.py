from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    resposta = 'Pagina principal do sistema'
    return HttpResponse(resposta)


def first_page(request):
    return render(request, 'index.html')


def levando_dados(request):
    from random import randint
    a = 10
    b = 20
    nome = 'Itanu'
    lista = list()
    contador = 0
    while True:
        numero = randint(0, 20)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador == 10:
            break
    contexto = {
        'valor1': a,
        'valor2': b,
        'nome': nome,
        'lista': lista
    }

    return render(request, 'index.html', contexto)


def simulador_loteria(request):
    from random import randint
    lista2 = list()
    contador2 = 0
    retorno = list()
    repeticoes = []
    if request.POST:
        quantidade = int(request.POST['numero_usuario'])
        for cont in range(0, quantidade):
            while True:
                numero = randint(1, 25)
                if numero not in lista2:
                    lista2.append(numero)
                    contador2 += 1
                if contador2 == 15:
                    break
            contador2 = 0
            retorno.append(sorted(lista2.copy()))
            lista2.clear()

        for analise in range(1, 26):
            count = 0
            for lista in retorno:
                if analise in lista:
                    count += 1
            repeticoes.append(count)

    contexto = {
        'listas': retorno,
        'repeticoes': repeticoes
    }
    return render(request, 'simulador.html', contexto)
