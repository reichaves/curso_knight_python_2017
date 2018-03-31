import tabula
import pandas as pd

# Rotina para converter um PDF que tem uma grande planilha em todas páginas em um arquivo CSV

dfs = [] # Cria lista vazia que vai armazenar as listas de cada grupo de páginas

# PDF tem 4.659 páginas, então uso um range em etapas, de 300 em 300 páginas, para economizar memória do java
for i in range(1,4659, 300):
    i2 = i + 299 # delimita página final do bloco

    if i2 > 4659: # no último for impõe um limite de página
        i2 = 4659

    print(i)
    print(i2)

    try:
        df = tabula.read_pdf("Aposentados_Fevereiro_2018.pdf", encoding='latin-1', spreadsheet=True, pages=(str(i)+'-'+str(i2)), header=None)
        dfs.append(df)
        print('Page ', len(df), ' parsed.')
    except:
        print('Error on page: ', i, i2)

output = pd.concat(dfs)
output.to_csv('servidores_rj_aposentados_fev_18.csv', encoding='utf-8', index=False)
