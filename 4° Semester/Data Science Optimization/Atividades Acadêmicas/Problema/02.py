#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 13:36:28 2025

@author: maurizio
"""

import pyomo.environ as pyo
from pyomo.opt import SolverFactory

# Criação do modelo concreto com nome descritivo
m = pyo.ConcreteModel(name="Escalonamento de Tarefas com Restrições")

# Conjuntos
m.setJ = pyo.Set(initialize=['A', 'B', 'C', 'D', 'E', 'F'])  # Conjunto de tarefas
m.setD = pyo.Set(initialize=[1, 2, 3])  # Conjunto de dias

# Parâmetros
m.D = {'A': 2, 'B': 3, 'C': 5, 'D': 2, 'E': 6, 'F': 4}  # Duração das tarefas (horas)
m.P = {'A': 200, 'B': 500, 'C': 300, 'D': 100, 'E': 1000, 'F': 300}  # Lucro das tarefas (R$)
m.maxHours = 6  # Máximo de horas disponíveis por dia

# Variáveis de decisão
# x[j,d] = 1 se a tarefa j é agendada no dia d, 0 caso contrário
m.x = pyo.Var(m.setJ, m.setD, within=pyo.Binary, bounds=(0, 1), initialize=0)

# Função objetivo: Maximizar o lucro total
m.obj = pyo.Objective(
    expr=sum(m.x[j, d] * m.P[j] for j in m.setJ for d in m.setD),
    sense=pyo.maximize
)

# Restrições
m.C1 = pyo.ConstraintList()  # Limite de horas por dia
m.C2 = pyo.ConstraintList()  # Cada tarefa agendada no máximo uma vez
m.C3 = pyo.ConstraintList()  # No máximo uma tarefa por dia

# Definição das restrições
for d in m.setD:
    # C1: Soma das durações das tarefas em cada dia não excede maxHours
    m.C1.add(sum(m.x[j, d] * m.D[j] for j in m.setJ) <= m.maxHours)
    # C3: Apenas uma tarefa pode ser agendada por dia
    m.C3.add(sum(m.x[j, d] for j in m.setJ) <= 1)

for j in m.setJ:
    # C2: Cada tarefa é agendada em no máximo um dia
    m.C2.add(sum(m.x[j, d] for d in m.setD) <= 1)

# Resolução do modelo
try:
    # Configuração do solver Gurobi
    opt = SolverFactory('gurobi')
    # Resolução com log visível
    m.results = opt.solve(m, tee=True)

    # Exibição da estrutura do modelo (opcional para debug)
    print("\nEstrutura do Modelo:")
    m.pprint()

    # Exibição dos resultados
    print('\n=== Resultados da Otimização ===')
    print(f'Lucro Total: R${pyo.value(m.obj):.2f}')
    print(f'Status do Solver: {m.results.solver.status}')
    print(f'Condição de Término: {m.results.solver.termination_condition}')

    # Cronograma organizado por dia
    print('\nCronograma Otimizado:')
    for d in m.setD:
        print(f'Dia {d}:')
        tarefas_dia = [(j, m.D[j], m.P[j]) for j in m.setJ if pyo.value(m.x[j, d]) > 0.9]
        if tarefas_dia:
            for j, dur, lucro in tarefas_dia:
                print(f'  Tarefa {j} (Duração: {dur}h, Lucro: R${lucro})')
        else:
            print('  Nenhuma tarefa agendada')

except Exception as e:
    print(f"\nErro ao resolver o modelo: {str(e)}")
    print("Verifique se o Gurobi está instalado e licenciado corretamente.")
