# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 08:17:10 2025

@author: maurizio.prizzi
"""

import pyomo.environ as pyo
from pyomo.opt import SolverFactory

# Criando o modelo
m = pyo.ConcreteModel()

# Definindo o conjunto de fundos e o capital total
m.setInv = pyo.Set(initialize=['A', 'B', 'C'])
m.Capital = 100000

# Definindo as variáveis
m.C = pyo.Var(m.setInv, bounds=(0, None)) # Quantidade investida em cada fundo
m.R = pyo.Var(m.setInv, bounds=(0, None)) # Retorno de cada fundo

# Função objetivo: maximizar o retorno total
m.obj = pyo.Objective(expr=pyo.summation(m.R), sense=pyo.maximize)

# Restrições
m.C1 = pyo.Constraint(expr=pyo.summation(m.C) == m.Capital) # Total investido = 100.000
m.C2 = pyo.Constraint(expr=m.R['A'] == 0.05 * m.C['A']) # Retorno de A = 5%
m.C3 = pyo.Constraint(expr=m.R['B'] == 0.10 * m.C['B']) # Retorno de B = 10%
m.C4 = pyo.Constraint(expr=m.R['C'] == 0.12 * m.C['C']) # Retorno de C = 12%
m.C5 = pyo.Constraint(expr=m.C['B'] <= 0.2 * m.Capital) # Máximo 20% em B
m.C6 = pyo.Constraint(expr=m.C['C'] <= 0.1 * m.Capital) # Máximo 10% em C

# Configurando o solver GLPK
opt = SolverFactory('glpk')

# Resolvendo o modelo
m.results = opt.solve(m)

# Exibindo os resultados de forma clara
print('=== Resultados do Investimento ===')
print(f"Fundo A (baixo risco): {pyo.value(m.C['A']):.2f} reais")
print(f"Fundo B (médio risco): {pyo.value(m.C['B']):.2f} reais")
print(f"Fundo C (alto risco): {pyo.value(m.C['C']):.2f} reais")
print(f"Retorno Total Anual: {pyo.value(m.obj):.2f} reais")