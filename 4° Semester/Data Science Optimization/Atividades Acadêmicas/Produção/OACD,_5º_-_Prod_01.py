# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 09:14:05 2025

@author: maurizio.prizzi
"""

import pyomo.environ as pyo
from pyomo.opt import SolverFactory

# Cria um modelo concreto do Pyomo
m = pyo.ConcreteModel()

# Definição de conjuntos e parâmetros
# Conjunto de máquinas: A, B e C
m.setMachine = pyo.Set(initialize=['A','B','C'])
# demanda total a ser atendida
m.Demand = 10000

# Definição das variáveis
# C[i]: Custo de produção da máquina i
m.C = pyo.Var(m.setMachine, bounds=(0,None)) # Limite inferior: 0, sem limite superior
# P[i]: quantidade produzida pela máquina i (inteiro)
m.P = pyo.Var(m.setMachine, within=pyo.Integers, bounds=(0,None)) # Limite inferior: 0, sem limite superior

# Funçaõ objetivo: minimizar a soma dos custos de produção
m.obj = pyo.Objective(expr=pyo.summation(m.C), sense=pyo.minimize)

# Definição das restrições
# Restrição C1: A soma das produção das máquinas deve ser igual à demanda
m.C1 = pyo.Constraint(expr=pyo.summation(m.P) == m.Demand)
# Restrição C2: Custo da máquina A è uma função quadrática da produção
m.C2 = pyo.Constraint(expr=m.C['A'] == 0.1*m.P['A']**2 + 0.5*m.P['A'] + 0.1)
# Restrição C3: Custo da máquina B é uma função linear da produção
m.C3 = pyo.Constraint(expr=m.C['B'] == 0.3*m.P['B']+0.5)
# Restrição C4: Custo da máquina C é uma função cúbica da produção
m.C4 = pyo.Constraint(expr=m.C['C'] == 0.01*m.P['C']**3)

# Solução do modelo
# Utiliza o solver Couenne, adequado para prblemas não lineares inteiros
opt = SolverFactory('couenne')
m.results = opt.solve(m)

# Impressão detalhada do modelo e dos resultados
m.pprint()

# Impressão do valor da função objetivo
print('|n|nOF:',pyo.value(m.obj))