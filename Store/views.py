from django.shortcuts import render
from django.http import HttpResponse
from Store.models import Departamento
from Store.models import Categoria
from Store.models import Produto
from django.core.mail import send_mail

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

def institucional(request):
    return render(request, 'institucional.html')

def contato(request):
    return render(request, 'contato.html')

def enviar_email(request):
    nome = request.POST['nome']
    telefone = request.POST['telefone']
    assunto = request.POST['assunto']
    mensagem = request.POST['mensagem']
    remetente = request.POST['email']
    destinatario = ['profronicosta@gmail.com']
    corpo = f"Nome: {nome} \nTelefone: {telefone}  \nMensagem: {mensagem}"
    
    try:
        send_mail(assunto, corpo, remetente, destinatario )
        context = {'msg': 'E-mail enviado com sucesso!'}
    except:
        context = {'msg': 'Erro ao enviar e-mail!'}
   
    return render(request, 'contato.html', context)