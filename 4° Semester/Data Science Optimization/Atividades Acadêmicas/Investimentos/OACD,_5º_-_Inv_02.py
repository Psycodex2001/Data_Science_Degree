# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 09:06:32 2025

@author: maurizio.prizzi
"""

# importar as bibliotecas
import pyomo.environ as pyo
from pyomo.opt import SolverFactory

# Criando o dicionário para mapear os fundos: A (alto), M (médio), B (baixo)
fundos = {
    'A': {'nome': 'Alto Risco', 'retorno': 0.12}, # 12% ao ano
    'M': {'nome': 'Médio Risco', 'retorno': 0.10}, # 10% ao ano
    'B': {'nome': 'Baixo Risco', 'retorno': 0.05} # 5% ao ano
}

# Definindo o capital total disponível (em reais)
capital_total = 100000

# Definindo o valor que queremos investir no fundo de alto risco (valor ajustável)
valor_alto_risco = 70000 # Pode ser alterado (ex.: 10.000, 50.000, 70.000)

# Criando o modelo de otimização
m = pyo.ConcreteModel()

# Definindo o conjunto de fundos com base nas chaves do dicionário
m.setInv = pyo.Set(initialize=fundos.keys())

# Definindo variáveis: quantidade investida (C) e retorno (R) para cada fundo
m.C = pyo.Var(m.setInv, bounds=(0, None)) # Investimento em cada fundo (>= 0)
m.R = pyo.Var(m.setInv, bounds=(0, None)) # Retorno de cada fundo (>= 0)

# Função objetivo: maximizar o retorno total (soma dos retornos)
m.obj = pyo.Objective(expr=pyo.summation(m.R), sense=pyo.maximize)

# Restrições do problema
m.C1 = pyo.Constraint(expr=pyo.summation(m.C) == capital_total) # Total investido = 100.000
m.C2 = pyo.Constraint(expr=m.R['B'] == fundos['B']['retorno'] * m.C['B']) # Retorno do fundo B
m.C3 = pyo.Constraint(expr=m.R['M'] == fundos['M']['retorno'] * m.C['M']) # Retorno do fundo M
m.C4 = pyo.Constraint(expr=m.R['A'] == fundos['A']['retorno'] * m.C['A']) # Retorno do fundo A
m.C5 = pyo.Constraint(expr=m.C['M'] <= 0.2 * capital_total) # Máximo 20% no fundo M (médio risco)
m.C6 = pyo.Constraint(expr=m.C['A'] == valor_alto_risco) # Fixando o valor no fundo A (alto risco)

# Configurando o solver GLPK
opt = SolverFactory('glpk')

# Resolvendo o modelo
m.results = opt.solve(m)

# Exibindo os resultdos de forma clara
print("=== Resultados do Investimento ===")
print(f"Valor escolhido para o fundo de alto risco (A): {valor_alto_risco:.2f} reais")
for fundo in fundos:
    print(f"Fundo {fundo} ({fundos[fundo]['nome']}): {pyo.value(m.C[fundo]):.2f} reais")
print(f"Retorno Total Anual: {pyo.value(m.obj):.2f} reais")

# Comentário final: podemos mudar 'valor_alto_risco' e rodar novamente
print("|nDica: Altere o 'valor_alto_risco' no código e execute para ver outros cenários.")