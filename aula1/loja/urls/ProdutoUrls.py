from django.urls import path
from loja.views.ProdutoView import list_produto_view
from loja.views.ProdutoView import edit_produto_view
urlpatterns = [
path("", list_produto_view, name= 'produto'),
path("<int:id>", list_produto_view, name= 'produtos'),
path("edit/<int:id>", edit_produto_view, name= 'edit_produto'),
]