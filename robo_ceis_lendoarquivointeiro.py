# -*- coding: utf-8
# @paidatocandeira
# Acessa arquivo do CADASTRO NACIONAL DE EMPRESAS INIDÔNEAS E SUSPENSAS (CEIS) que está no portal da Transparência
#

import pandas as pd

# Parte 2 - pode rodar no Jupyter para ver resultados
# Método lendo direto o arquivo disponível para download (http://www.portaltransparencia.gov.br/downloads/snapshot.asp?c=CEIS#get)
ceis_arquivo = pd.read_csv("20180225_CEIS.csv",sep=';',encoding = 'latin_1', converters={'CPF ou CNPJ do Sancionado': lambda x: str(x)})
# É um arquivo CSV comum, pode abrir em outros programas também
ceis_arquivo.reset_index()
# Exemplo de busca - de SP
ceis_arquivo.info() # mostra nomes de todas colunas
ceis_sp = ceis_arquivo[(ceis_arquivo['UF Órgão Sancionador'] == 'SP')]
ceis_sp.to_csv('ceis_sp.csv') # Salva como CSV só o grupo de SP
