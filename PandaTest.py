import pandas as pd
from pathlib import Path

#criando um pequeno conjunto de dados
dados = {
    "Nome": ["Ana", "Bruno", "Carlos"],
    "Idade": [25, 47, 32]
}
df = pd.DataFrame(dados)

print(df)

print("\n")

#criando uma série de dados
s = pd.Series([10, 20, 30])
#print(s)

#caminho da tabela de dados .csv
path = Path("C:/Users/Paulo/Desktop/Python/PandaTest/dadosTest.csv")

#recolher dados da tabela
df1 = pd.read_csv(path, sep=";")

#Exibir as primeira 4 linhas da tabela
#print(df1.head())
dfhead = df1.head()
print(dfhead)

#exibir as últimas 4 linhas da tabela
#print(df1.tail())
dftail = df1.tail()
print(dftail)

#Buscar colunas específicas
dfColumns = df1[['cod', "NOME"]]
print(dfColumns)

#Exibir todos os dados
print(df1)
