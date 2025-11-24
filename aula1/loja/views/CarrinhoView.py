from django.shortcuts import render, get_object_or_404, redirect
from loja.models import Produto, Carrinho, CarrinhoItem, Usuario
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Função para adicionar um item ao carrinho
def create_carrinhoitem_view(request, produto_id=None):
    print('create_carrinhoitem_view')
    produto = get_object_or_404(Produto, pk=produto_id)

    if produto:
        print('produto: ' + str(produto.id))

    # Tenta pegar o carrinho da sessão
    carrinho_id = request.session.get('carrinho_id')
    print('carrinho: ' + str(carrinho_id))
    carrinho = None

    if carrinho_id:
        carrinho = Carrinho.objects.filter(id=carrinho_id).first()
        print(carrinho)
        print('carrinho1: ' + str(carrinho.id))

        hoje = datetime.today().date()
        if carrinho.criado_em.date() != hoje:
            carrinho = Carrinho.objects.create()
            request.session['carrinho_id'] = carrinho.id
            print('novo carrinho: ' + str(carrinho.id))

    else:
        carrinho = Carrinho.objects.create()
        request.session['carrinho_id'] = carrinho.id
        print('carrinho2: ' + str(carrinho.id))

    # Verifica se o produto já está no carrinho
    carrinho_item = CarrinhoItem.objects.filter(carrinho=carrinho, produto=produto).first()
    if carrinho_item:
        carrinho_item.quantidade += 1
        print('item de carrinho: Acrescentou 1 item do produto ' + str(carrinho_item.id))
    else:
        carrinho_item = CarrinhoItem.objects.create(
            carrinho=carrinho,
            produto=produto,
            quantidade=1,
            preco=produto.preco
        )
        print('item de carrinho: Acrescentou o produto ' + str(carrinho_item.id))

    carrinho_item.save()
    print('item de carrinho salvo: ' + str(carrinho_item.id))

    return redirect('/carrinho')


# Função para listar itens do carrinho
def list_carrinho_view(request):
    print('list_carrinho_view')
    carrinho_id = request.session.get('carrinho_id')
    carrinho = None

    if carrinho_id:
        print('carrinho: ' + str(carrinho_id))
        carrinho = Carrinho.objects.filter(id=carrinho_id).first()
        print('Data do carrinho ' + str(carrinho.criado_em))

        itens = CarrinhoItem.objects.filter(carrinho_id=carrinho_id)

        if itens:
            print('itens de carrinho encontrado: ' + str(itens))

        context = {
            'carrinho': carrinho,
            'itens': itens
        }
        return render(request, 'carrinho/carrinho-listar.html', context=context)


# Função para confirmar a compra
@login_required
def confirmar_carrinho_view(request):
    print('confirmar_carrinho_view')
    carrinho_id = request.session.get('carrinho_id')
    carrinho = None

    if carrinho_id:
        carrinho = Carrinho.objects.filter(id=carrinho_id).first()
        usuario = get_object_or_404(Usuario, user=request.user)
        print('Usuario: ' + str(usuario))

        if usuario:
            carrinho.user_id = usuario.id
            carrinho.situacao = 1
            carrinho.confirmado_em = timezone.make_aware(datetime.today())
            carrinho.save()
            print('carrinho salvo')

            return render(request, 'carrinho/carrinho-confirmado.html', {'carrinho': carrinho})


# Remover item do carrinho
def remover_item_view(request, item_id):
    item = get_object_or_404(CarrinhoItem, id=item_id)
    carrinho_id = request.session.get('carrinho_id')

    if carrinho_id == item.carrinho.id:
        item.delete()

    return redirect('/carrinho')
