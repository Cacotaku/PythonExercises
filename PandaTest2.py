#Video tutorial https://www.youtube.com/watch?v=1JpYOqvDJNU

import pandas as pd
from pathlib import Path
import os

dados = {
    "Nome": ["Ana", "Bruno", "Breno", "Carla", "Daniel", "Elizabeth"],
    "Idade": [35, 29, 18, 45, 37, 50],
    "Cidade": ["Rio de Janeiro", "Pindamonhamgaba", "Belo Horizonte", "New Jersey", "Caracas", "Bali"], 
    "Salário": [3200.00, 4500.50, 2800.75, 5200.00, 6100.25, None],
    "ID Departamento": [101, 102, 101, 103, 102, 101]
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

colunasSelecionadas = planilhaServico[["Número do Protocolo:", "Escolha o serviço:", "Data da Solicitação:", "Status da solicitação:", "Logradouro:"]]
#print(colunasSelecionadas, "\n")

__apagarTela()

#print(colunasSelecionadas[colunasSelecionadas["Data da Solicitação:"] < "2025-01-01"]) Não funcionou corretamente

#protocolo1 = colunasSelecionadas["Número do Protocolo:"] = "18130445/151225" It didn't work correctly
#protocolo2 = colunasSelecionadas["Número do Protocolo:"] = "96102723/121225" It didn't work correctly
#colunasSelecionadas[protocolo1 & protocolo2] It didn't work correctly

filtroMaiorQue30 = df["Idade"] > 30
filtroMenorQue40 = df["Idade"] < 40
filtroDeCidade = df["Cidade"] == "Caracas"

print(df[filtroMaiorQue30 & filtroMenorQue40 & filtroDeCidade].count(), "\n") #Filtrar por idade maior que 30, menor que 40 e cidade igual a Caracas

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

print(colunasSelecionadas["Status da solicitação:"].value_counts(), "\n") #count unique values in Status da Solicitação column

mediaSalario = df.groupby("ID Departamento")["Salário"].mean() #mean salary by department
print(mediaSalario, "\n")

somaSalario = df.groupby("ID Departamento")["Salário"].sum() #sum salary by department
print(somaSalario, "\n")

maiorSalario = df.groupby("ID Departamento")["Salário"].max() #max salary by department
print(maiorSalario, "\n")

menorSalario = df.groupby("ID Departamento")["Salário"].min().astype(float) #min salary by department
print(menorSalario, "\n")

groupbyIDDepartamento = df.groupby("ID Departamento").count() #count of employees by department
print(groupbyIDDepartamento,"\n")

groupbyLogradouro = colunasSelecionadas[["Logradouro:", "Número do Protocolo:"]].groupby("Logradouro:").count() #count by Logradouro
print(groupbyLogradouro,"\n")

ordenarPorNome = df.sort_values("Nome") #sort by Name
print(ordenarPorNome,"\n")

ordenarPorSalarioDesc = df.sort_values("Salário", ascending = False) #sort by Salary descending
print(ordenarPorSalarioDesc, "\n")

pathComplemento = Path("C:/Users/paulo.oliveira/desktop/Python/PandaTest/Complemento.csv")  #Sheet with departaments adresses
planilhaComplemento = pd.read_csv(pathComplemento, sep = ";")

planilhaFinal = pd.merge(planilhaServico, planilhaComplemento)  #merge two sheets using a common column
print(planilhaFinal.head(), "\n")

planilhaFinal2 = pd.merge(planilhaServico, planilhaComplemento, left_on = "Secretaria/Regional do responsável pelo atendimento:", right_on = "Secretaria/Regional do responsável pelo atendimento:")  #merge two sheets using a common column even with different names
print(planilhaFinal2.tail(), "\n")

pathComplemento2 = Path("C:/Users/paulo.oliveira/desktop/Python/PandaTest/Complemento2.csv")  #Sheet with departaments adresses
planilhaComplemento2 = pd.read_csv(pathComplemento2, sep = ";")

planilhaEnderecos = pd.concat([planilhaComplemento, planilhaComplemento2], ignore_index = True)  #concatenate two sheets (Complemento and Complemento2)
print(planilhaEnderecos.head(), "\n")

path3 = Path("C:/Users/paulo.oliveira/Desktop/Python/PandaTest/TodosEnderecos.csv")
planilhaEnderecos.to_csv(path3, sep = ";")  #export to csv

path4 = Path("C:/Users/paulo.oliveira/Desktop/Python/PandaTest/TodosEnderecos.xlsx")
planilhaEnderecos.to_excel(path4)  #export to Excel
