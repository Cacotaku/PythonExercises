import pandas as pd
from pathlib import Path
import os

dados = {
    "Nome": ["Ana", "Bruno", "Breno", "Carla", "Daniel", "Elizabeth"],
    "Idade": [35, 29, 18, 45, 37, 50],
    "Cidade": ["Rio de Janeiro", "Pindamonhamgaba", "Belo Horizonte", "New Jersey", "Caracas", "Bali"], 
    "Salário": [3200.00, 4500.50, 2800.75, 5200.00, 6100.25, None]
}

def __apagarTela():
    os.system('cls' if os.name == 'nt' else 'clear')
    pass

df = pd.DataFrame(dados)
#print("Dados\n",df, "\n")

Series = pd.Series([15,25,30,60,45])
#print("Serie de dados\n", Series)

path = Path("C:/Users/paulo.oliveira/desktop/Python/PandaTest/DataRecords.csv")
planilhaServico = pd.read_csv(path, sep = ";")

#print(planilhaServico.head(), "\n")

colunasSelecionadas = planilhaServico[["Número do Protocolo:", "Escolha o serviço:", "Data da Solicitação:", "Status da solicitação:"]]
#print(colunasSelecionadas, "\n")

__apagarTela()

#print(colunasSelecionadas[colunasSelecionadas["Data da Solicitação:"] < "2025-01-01"]) Não funcionou corretamente

#protocolo1 = colunasSelecionadas["Número do Protocolo:"] = "18130445/151225" It didn't work correctly
#protocolo2 = colunasSelecionadas["Número do Protocolo:"] = "96102723/121225" It didn't work correctly
#colunasSelecionadas[protocolo1 & protocolo2] It didn't work correctly

filtroMaiorQue30 = df["Idade"] > 30
filtroMenorQue40 = df["Idade"] < 40
filtroDeCidade = df["Cidade"] == "Caracas"

print(df[filtroMaiorQue30 & filtroMenorQue40 & filtroDeCidade], "\n") #Filtrar por idade maior que 30, menor que 40 e cidade igual a Caracas

df["Idade após 10 anos"] = df["Idade"] + 10 #Adicionar uma nova coluna com idade mais 10 anos
print(df, "\n")

df = df.drop("Idade após 10 anos", axis=1) #Remover a coluna adicionada
print(df, "\n")

print(df.describe(), "\n") #describe DataFrame

print(df["Idade"].mean(), "\n") #mean of Idade column

print(df.dropna(), "\n") #remove NaN (null values) values

print(df.dropna(subset = "Idade"), "\n") #remove NaN (null values) values in Idade column only

salariominimo = 1528.00
df["Salário"] = df["Salário"].fillna(salariominimo).astype(float) #fill NaN values with minimum wage]
print(df, "\n")

print(colunasSelecionadas["Status da solicitação:"].value_counts()) #count unique values in Status da Solicitação column