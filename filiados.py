# Baixa os arquivos .zip dos filiados em partidos políticos no Brasil
# http://www.tse.jus.br/partidos/filiacao-partidaria/relacao-de-filiados
# @paidatocandeira

from urllib.request import urlopen
import urllib.request, urllib.parse, urllib.error
import pandas as pd

lista = ['dem', 'avante', 'psdc', 'pmdb', 'novo', 'pen', 'pc_do_b', 'pcb', 'pco', 'pdt', 'phs', 'pmb', 'pmn', 'pode', 'pp', 'ppl', 'pps', 'pr', 'prb', 'pros', 'prp', 'prtb', 'psb', 'psc', 'psb', 'psdb', 'psl', 'psol', 'pstu', 'pt', 'ptb', 'ptc', 'pv', 'rede', 'sd']
partidos = pd.DataFrame(lista, columns = ['partido'])

lista = ['ac', 'al', 'am', 'ap', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mg', 'ms', 'mt', 'pa', 'pb', 'pe', 'pi', 'pr', 'rj', 'rn', 'ro', 'rr', 'rs', 'sc', 'se', 'sp', 'to']
estados = pd.DataFrame(lista, columns = ['estado'])

def baixa_arquivo(nome, url):
	try:
		urllib.request.urlretrieve(url, arquivo)
	except Exception:
		print (Exception)
		print('Erro em: ' + url)


for linha, row in partidos.iterrows():
	nome = (row['partido'])
	print(nome)
	for vez, row2 in estados.iterrows():
		local = (row2['estado'])
		print(local)
		url = 'http://agencia.tse.jus.br/estatistica/sead/eleitorado/filiados/uf/filiados_'+nome+'_'+local+'.zip'
		arquivo = "filiados_"+nome+"_"+local
		baixa_arquivo(arquivo, url)
