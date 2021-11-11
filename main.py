#Os arquivos com os Dados foram baixados separadamente e renomeados para 'questao1' e 'questao2', respectivamente de acordo com a ordem das tabelas dadas.

#Importando a Biblioteca Pandas

pip install pandas

#Note: you may need to restart the kernel to use updated packages.

from pandas import Series, DataFrame

import pandas as pd

import numpy as np

#Tratamento de Dados

#Leitura de Arquivos

df_dados1 = pd.read_csv('questao1.csv', sep = ',', skiprows = 0, encoding = 'utf-8')

df_dados2 = pd.read_csv('questao2.csv', sep = ',', skiprows = 0, encoding = 'utf-8')

#Renomeando colunas

df_dados1.rename(columns = {'num_compra':'num_compra', 'usuario':'usuario', 'Tipo de Mercadoria': 'tipo_mercadoria', 'Filial':'filial','data_compra':'data_compra', 'valor_compra':'valor_compra', 'Imposto':'imposto', 'CPF NA NOTA?':'cpf_nota', 'Produto Devolvido':'produto_devolvido'})

df_dados2.columns = ['cod_loja', 'data_compra', 'inicio', 'termino', 'loja', 'cod_produto', 'produto', 'ean', 'valorunitario_semimposto', 'quantidade', 'valor_total', 'impostos', 'dinheiro_devolta']

#Deletando colunas para deixar somente as que serão usadas para a análise

df_dados1 = df_dados1.drop(['num_compra', 'nome', 'filial', 'data_compra', 'valor_compra'], axis = 'columns')

df_dados2 = df_dados2.drop(['cod_loja', 'data_compra', 'inicio', 'termino', 'loja', 'cod_produto', 'ean', 'valorunitario_semiproduto', 'quantidade', 'valor_total', 'impostos'], axis = 'columns')

#Verificando tipos de colunas

df_dados1.dtypes

df_dados2.dtypes

#Após o Tratamento de dados segue abaixo as respostas para as perguntas do Teste

#Unidade mais vendida - df_dados1 = Questão1

df_dados1 = df_dados1['tipo_mercadoria'].value_counts(dropna=False, normalize=True)

#% De CPF na Nota - df_dados1 = Questão1

df_dados1 = df_dados1['cpf_nota'].count()

#% De imposto - df_dados1 = Questão1

df_dados1 = df_dados1['imposto'].sum()

#% De Devolução - df_dados1 = Questão1

df_dados1 = df_dados1['produto_devolvido'].value_counts(dropna=False, normalize=True)

#Quatidade rendida em dinheiro devolvido - df_dados2 = Questão2

df_dados2 = df_dados2['dinheiro_devolta'].sum()

#Produto mais vendido - df_dados2 = Questão2

df_dados2 = df_dados2['produto'].value_counts(dropna=False, normalize=True)

#Análise de Dados com a Pandas concluída.
