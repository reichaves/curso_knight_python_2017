# -*- coding: utf-8
# @paidatocandeira
# Raspa CADASTRO NACIONAL DE EMPRESAS INIDÔNEAS E SUSPENSAS (CEIS)
#

from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep
import random

# Parte 1 - pode executar como .py essa parte direto na linha de comando - roda mais rápido
def faz_sopa(link):
    response = requests.get(link)
    sopa = BeautifulSoup(response.content, "html.parser")
    return sopa

if __name__ == '__main__':
    data = []
    for i in range(1,820):
        link = "http://www.portaltransparencia.gov.br/ceis?pagina="
        link = link + str(i)
        print(link)
        sopa = faz_sopa(link)
        sleep(random.uniform(0.2, 10)) # Cria pausas para site não barrar raspagem
        for tr in sopa.find_all('tr'): # A tag <tr> é a tabela
            col = 0
            for td in tr.find_all('td'): # Dentro da <tr> estão as linhas de dados <td>
                td_text = td.get_text().strip()
                if col == 0: # Cada número é uma coluna em cada linha
                    cnpj_cpf = td_text
                    cnpj_cpf_link = 'http://www.portaltransparencia.gov.br{}'
                    cnpj_cpf_link = cnpj_cpf_link.format(td.find('a').get('href'))
                if col == 1:
                    nome = td_text
                if col == 2:
                    tipo = td_text
                if col == 3:
                    data_final = td_text
                if col == 4:
                    nome_do_orgao = td_text
                if col == 5:
                    uf = td_text
                    data.append({
                            'cnpj_cpf' : cnpj_cpf,
                            'cnpj_cpf_link' : cnpj_cpf_link,
                            'nome' : nome,
                            'tipo' : tipo,
                            'data_final' : data_final,
                            'nome_do_orgao' : nome_do_orgao,
                            'uf' : uf
                                })
                col += 1
    df_ceis = pd.DataFrame(data, columns = ['cnpj_cpf', 'cnpj_cpf_link', 'nome', 'tipo', 'data_final', 'nome_do_orgao', 'uf']) # Cria dataframe
    df_ceis.to_csv('ceis.csv') # Salva como CSV
