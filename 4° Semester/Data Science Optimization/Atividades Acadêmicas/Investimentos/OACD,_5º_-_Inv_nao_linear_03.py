# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 10:04:53 2025

@author: maurizio.prizzi
"""

# Importando as bibliotecas
import pyomo.environ as pyo
from pyomo.opt import SolverFactory

# Criando o modelo
m = pyo.ConcreteModel()

# Definindo o conjunto de fundos e o capital total 
m.setInv = pyo.Set(initialize=['A','B','C','D']) # Fundos A, B, C, D
m.Capital = 100000 # Total disponível: 100.000 reais

# Definindo as variáveis
m.C = pyo.Var(m.setInv, bounds=(0, None)) # Capital investido em cada fundo (C_A, C_B, C_C, C_D)
m.R = pyo.Var(m.setInv, bounds=(0, None)) # Retorno de cada fundo (R_A, R_B, R_C, R_D)

# Função objetivo: maximizar o retorno total
m.obj = pyo.Objective(expr=pyo.summation(m.R), sense=pyo.maximize)

# Restrições
m.C1 = pyo.Constraint(expr=pyo.summation(m.C) == m.Capital) # Total investido = 100.000 reais
m.C2 = pyo.Constraint(expr=m.R['A'] == 0.05 * m.C['A']) # Retorno de A: 5% ao ano
m.C3 = pyo.Constraint(expr=m.R['B'] == 0.10 * m.C['B']) # Retorno de B: 10% ao ano
m.C4 = pyo.Constraint(expr=m.R['C'] == 0.12 * m.C['C']) # Retorno de C: 12% ao ano

# Atenção: investimento não linear
m.C5 = pyo.Constraint(expr=m.R['D'] == 1e-6 * m.C['D']**2)
# Retorno de D: 10(to the power of)-6 * C_D (to the power of)2 (não linear)

m.C6 = pyo.Constraint(expr=m.C['B'] <= 0.2 * m.Capital) # Máximo 20% em B (20.000 reais)
m.C7 = pyo.Constraint(expr=m.C['C'] <= 0.1 * m.Capital) # Máximo 10% em C (10.000 reais)
m.C8 = pyo.Constraint(expr=m.C['D'] <= 0.3 * m.Capital) # Máximo 30% em D (30.000 reais)

# Configurando o solver IPOPT (não linear, gratuito)
opt = SolverFactory('ipopt')

# Resolvendo o modelo
m.results = opt.solve(m)

# Exibindo os resultado de forma clara
print("=== Resultados de Investimento (Não Linear) ===")
print(f"Fundo A (baixo risco): {pyo.value(m.C['A']):.2f} reais")
print(f"Fundo B (médio risco): {pyo.value(m.C['B']):.2f} reais")
print(f"Fundo C (alto risco): {pyo.value(m.C['C']):.2f} reais")
print(f"Fundo D (especial): {pyo.value(m.C['D']):.2f} reais")
print(f"Retorno Total Anual: {pyo.value(m.obj):.2f} reais")