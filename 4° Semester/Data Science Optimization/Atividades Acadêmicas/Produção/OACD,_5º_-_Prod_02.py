# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 10:16:09 2025

@author: maurizio.prizzi
"""

# Importa a biblioteca Pyomo para modelagem de otimização
import pyomo.environ as pyo
# Importa a classe SolverFactory para configurar o solver
from pyomo.opt import SolverFactory

# Cria um modelo concreto do Pyomo
m = pyo.ConcreteModel()

# Define os conjuntos e parâmetros do modelo
m.setMachine = pyo.Set(initialize=['A','B','C']) # Conjunto de máquinas disponíveis
m.Demand = 10000 # Demanda total a ser atendida
M = 1e6 # Constante grande para restrições Big-M

# Define as variáveis de decisão
m.C = pyo.Var(m.setMachine, bounds=(0,None)) # Custo de cada máquina (contínuo >= 0)
m.P = pyo.Var(m.setMachine, within=pyo.Integers, bounds=(0,None)) # Produção de cada máquina (inteiro >= 0)
m.B = pyo.Var(m.setMachine, within=pyo.Binary) # Variável binária (0 ou 1) para ativação da máquina

# Define a função objetivo
# Minimiza a soma dos custos de todas as máquinas
m.obj = pyo.Objective(expr=pyo.summation(m.C), sense=pyo.minimize)

# Define as restrições do modelo
# Restrição 1: A soma da produção de todas as máquinas deve ser igual a demanda
m.C1 = pyo.Constraint(expr=pyo.summation(m.P) == m.Demand)

# Restrição 2: Define o custo da máquina A como uma função quadrática da produção
# C[A] = 0.1*P[A]**2 + 0.5*P[A] + 0.1*B[A]
m.C2 = pyo.Constraint(expr=m.C['A'] == 0.1*m.P['A']**2 + 0.5*m.P['A'] + m.B['A']*0.1)

# Restrição 3: Define o custo da máquina B como uma função linear da produção
# C[B] = 0.3*P[B] + 0.5*B[B]
m.C3 = pyo.Constraint(expr=m.C['B'] == 0.3*m.P['B'] + m.B['B']*0.5)

# Restrição 4: Define o custo da máquina C como uma função cúbica da produção
# C[C] = 0.01*P[C]**3
m.C4 = pyo.Constraint(expr=m.C['C'] == 0.01*m.P['C']**3)

# Restrição 5: Se B[A]=0, então P[A] deve ser 0 (restrição Big-M para máquina A)
m.C5 = pyo.Constraint(expr=m.P['A'] <= m.B['A']*M)

# Restrição 6: Se B[B]=0, então P[B] deve ser 0 (restrição Big-M para máquina B)
m.C6 = pyo.Constraint(expr=m.P['B'] <= m.B['B']*M)

# Configura e resolve o modelo
# Usa o solver Couenne rodando no Docker
opt = SolverFactory('couenne', executable='couenne', solver_io='nl')
opt.options['host'] = '127.0.0.1' # Endereço do Docker
opt.options['port'] = 5000 # Porta mapeada

# Resolve o modelo e armazena os resultados
m.results = opt.solve(m)

# Imprime o modelo completo com resultados
m.pprint()

# Imprime o valor da função objetivo (custo toal mínimo)
print('|n|nOF:', pyo.value(m.obj))