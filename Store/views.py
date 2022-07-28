from django.shortcuts import render
from django.http import HttpResponse
from Store.models import Departamento
from Store.models import Categoria
from Store.models import Produto

# Create your views here.
def index(request):
    meu_nome = 'Beltrano da Costa'
    sexo = 'M'
    context = {
        'nome': meu_nome, 
        'artigo': 'o' if sexo == 'M' else 'a'
        }
    return render(request, 'index.html', context)

def teste(request):
    # depto = ['Casa', 'Informática', 'Telefonia', 'Games']
    depto = Departamento.objects.all()
    context = {'departamentos': depto}
    return render(request, 'teste.html', context)

def departamentos(request):
    depto = Departamento.objects.all()
    context = {'departamentos': depto}
    return render(request, 'departamentos.html', context)

def categorias(request)    :
    lista_categorias = Categoria.objects.all()
    context = {'categorias': lista_categorias}
    return render(request, 'categorias.html', context)

def produtos (request):
    lista_produtos = Produto.objects.all()
    context = {'produtos' : lista_produtos}
    return render(request, 'produtos.html', context)