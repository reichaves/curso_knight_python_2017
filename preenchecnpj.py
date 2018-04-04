# Exemplo de programa que preenche zeros à esquerda de CNPJs

import pandas as pd

def compara(linha):
    if len(linha['CNPJ']) < 14:
        conta = 14 - (len(linha['CNPJ']))
        zero = '0'
        zeros = zero * conta
        alterado = zeros + linha['CNPJ']
    else:
        alterado = linha['CNPJ']
    return alterado


lista_pf = pd.read_csv('empresas_seg_br_mar18_pf.csv', sep=',',encoding = 'utf-8', converters={'CNPJ': lambda x: str(x)} )

nova = lista_pf.apply(compara, axis=1) #lê dataframe e chama a função

lista_pf['cnpj_inteiro'] = nova # adiciona coluna com os resultados ao dataframe

lista_pf.reset_index().head()
