#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 13:35:24 2025

@author: maurizio
"""

import pyomo.environ as pyo
from pyomo.opt import SolverFactory

# Criação do modelo concreto
m = pyo.ConcreteModel(name="Escalonamento de Tarefas")

# Conjuntos
m.setJ = pyo.Set(initialize=['A','B','C','D','E','F'])  # Conjunto de tarefas
m.setD = pyo.Set(initialize=[1,2,3])  # Conjunto de dias

# Parâmetros
m.D = {'A':2, 'B':3, 'C':5, 'D':2, 'E':6, 'F':4}  # Duração das tarefas em horas
m.P = {'A':200, 'B':500, 'C':300, 'D':100, 'E':1000, 'F':300}  # Lucro por tarefa
m.maxHours = 6  # Máximo de horas por dia

# Variáveis de decisão
# x[j,d] = 1 se tarefa j é agendada no dia d, 0 caso contrário
m.x = pyo.Var(m.setJ, m.setD, within=pyo.Binary, bounds=(0,1), initialize=0)

# Função objetivo: Maximizar o lucro total
m.obj = pyo.Objective(
    expr=sum(m.x[j,d] * m.P[j] for j in m.setJ for d in m.setD),
    sense=pyo.maximize
)

# Restrições
m.C1 = pyo.ConstraintList()  # Restrição de horas por dia
m.C2 = pyo.ConstraintList()  # Restrição de agendamento único

# Restrição 1: Soma das horas das tarefas por dia <= máximo de horas
for d in m.setD:
    m.C1.add(
        sum(m.x[j,d] * m.D[j] for j in m.setJ) <= m.maxHours
    )

# Restrição 2: Cada tarefa pode ser agendada no máximo uma vez
for j in m.setJ:
    m.C2.add(
        sum(m.x[j,d] for d in m.setD) <= 1
    )

# Resolução do modelo
try:
    # Configuração do solver Gurobi
    opt = SolverFactory('gurobi')
    # Resolução do modelo e armazenamento dos resultados
    resultados = opt.solve(m, tee=True)  # tee=True mostra o log do solver
    
    # Exibição da estrutura do modelo
    print("\nEstrutura do Modelo:")
    m.pprint()
    
    # Resultados
    print('\nResultados da Otimização:')
    print(f'Lucro Total: {pyo.value(m.obj):.2f}')
    print(f'Status do Solver: {resultados.solver.status}')
    print(f'Condição de Término: {resultados.solver.termination_condition}')
    
    # Impressão do cronograma
    print('\nCronograma Otimizado:')
    for d in m.setD:
        print(f'\nDia {d}:')
        for j in m.setJ:
            if pyo.value(m.x[j,d]) > 0.9:  # Verifica se a tarefa está agendada
                print(f'  Tarefa {j}: Duração={m.D[j]}h, Lucro=R${m.P[j]}')

except Exception as e:
    print(f"\nErro ao resolver o modelo: {str(e)}")
    print("Verifique se o Gurobi está instalado e licenciado corretamente.")