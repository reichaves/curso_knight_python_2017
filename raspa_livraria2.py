import requests
from bs4 import BeautifulSoup

# Procurar metodo POST em Inspecionar Elemento-Network
# Ver parametros passados em uma busca

def post_http(url, nome_livro):
    #payload = {'enviar': 'Buscar',
    #       'palavra': 'redes+de+computadores'}

    payload = {'enviar': 'Buscar',
           'palavra': nome_livro}

    try:
        return requests.post(url, data=payload)
    except(requests.exceptions.HTTPError, requests.exceptions.RequestException, requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
        print(str(e))
        pass
    except Exception as e:
        raise
    return None

def parse_html(content):
    soup = BeautifulSoup(content, 'lxml')
    produtos = soup.find_all('table')[10].find_all('td')
#    f = open('td.html', 'w', encoding = 'utf-8')
#    for produto in produtos:
#        f.write(str(produto))
#        f.write('\n\n\n')
#    f.close()
    lista_auxiliar = []
    lista_produto = []
    url = 'https://novatec.com.br/'
    url_capa = ''
    url_produto = ''

    for produto in produtos:
        tag_a = produto.find('a')
        if tag_a:
            if tag_a.next_element.next_element.name == 'img':
                #url_capa = "{0}{1}".format(url, tag_a.img.get('src'))
                url_capa = tag_a.img.get('src')
                url_produto = "{0}{1}".format(url, tag_a.get('href'))
                #print(url_produto)

        for string in produto.stripped_strings:
            if (string == 'Esgotado'):
                continue
            lista_auxiliar.append(string)

#        print(lista_auxiliar)
#        del lista_auxiliar[:]

        if (len(lista_auxiliar) > 6):
            lista_auxiliar.append(url_capa)
            lista_auxiliar.append(url_produto)
            lista_produto.append(tratar_dados(lista_auxiliar, url_produto))
        del lista_auxiliar[:]
#    print(lista_produto)
    if (len(lista_produto) > 0):
        del lista_produto[0]
    return lista_produto


def tratar_dados(lista_auxiliar, url_produto):
    preco = lista_auxiliar[7].replace('Preço: ', '')
    d = {'titulo': lista_auxiliar[0],
        'url_capa': lista_auxiliar[9],
        'url_produto': url_produto,
        'preco': preco}
    return d


if __name__ == '__main__':
    url = 'https://novatec.com.br/busca.php'
    nome_livro = input("Digite o nome do livro: ")
    r = post_http(url, nome_livro)
#    with open('result.html', 'w', encoding = 'utf-8') as f:
#        f.write(r.text)
    lista_produto = []
    if r:
        lista_produto = parse_html(r.text)
    print(lista_produto)
