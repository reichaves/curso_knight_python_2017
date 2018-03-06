import requests
from bs4 import BeautifulSoup
import raspa_livraria1
import raspa_livraria2

def livraria2(nome_livro):
    url = 'https://novatec.com.br/busca.php'
    r = raspa_livraria2.post_http(url, nome_livro)
    lista_produto = []
    if r:
        lista_produto = raspa_livraria2.parse_html(r.text)
    return lista_produto

def livraria1(nome_livro):
    url = 'https://busca.saraiva.com.br/busca'
    r = raspa_livraria1.get_http(url, nome_livro)
    lista_produtos = []
    lista = []
    if r:
        lista_produtos = raspa_livraria1.get_produtos(r.text)
        lista = raspa_livraria1.get_page_produto(lista_produtos)
    return lista

def main(nome_livro):
    d_produtos = {}
    lista_produtos = livraria2(nome_livro)
    d_produtos.update({'novatec': lista_produtos})
    lista_produtos = livraria1(nome_livro)
    d_produtos.update({'saraiva': lista_produtos})
    return d_produtos

if __name__ == '__main__':
    nome_livro = input("Digite o nome/assunto do livro: ")
    resultado = main(nome_livro)
    print(resultado)
