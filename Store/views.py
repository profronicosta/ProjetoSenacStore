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

def departamentos(request):
    depto = Departamento.objects.all()
    context = {'departamentos': depto}
    return render(request, 'departamentos.html', context)


def categorias(request, id):
    lista_categorias = Categoria.objects.filter(departamento_id = id)
    depto = Departamento.objects.get(id = id)
    context = {
                'categorias': lista_categorias, 
                'departamento': depto
            }
    return render(request, 'categorias.html', context)


def produtos(request, id):
    lista_produtos = Produto.objects.filter(categoria_id = id)
    categoria = Categoria.objects.get(id = id)
    context = {
                'produtos' : lista_produtos,
                'categoria' : categoria
            }
    return render(request, 'produtos.html', context)

def produto_detalhe(request, id):
    produto = Produto.objects.get(id = id)
    context = {
                'produto': produto
              }
    return render(request, 'produto_detalhe.html', context)