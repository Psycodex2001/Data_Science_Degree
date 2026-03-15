#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 11:22:18 2025

@author: maurizio
"""

import pyomo.environ as pyo
from pyomo.opt import SolverFactory

# Criando o modelo concreto
m = pyo.ConcreteModel()

# Definindo conjuntos de pontos
m.setAllPoints = ['A', 'P1', 'P2', 'P3', 'B']  # Todos os pontos do grafo
m.setPoints = ['P1', 'P2', 'P3']  # Pontos intermediários

# Definindo conjunto de rotas (origem, destino)
m.setRoutes = [['A', 'P1'], ['A', 'P2'], ['P1', 'P2'], ['P2', 'P1'], 
               ['P1', 'B'], ['P2', 'P3'], ['P3', 'B']]

# Criando dicionários para rotas saindo e chegando em cada ponto
m.setRoutes_from = {key: [] for key in m.setAllPoints}  # Rotas saindo do ponto
m.setRoutes_to = {key: [] for key in m.setAllPoints}    # Rotas chegando no ponto
for route in m.setRoutes:
    m.setRoutes_from[route[0]].append(route[1])
    m.setRoutes_to[route[1]].append(route[0])

# Definindo parâmetros (distâncias entre pontos)
m.D = {}
m.D['A', 'P1'] = 2
m.D['A', 'P2'] = 7
m.D['P1', 'P2'] = 10
m.D['P2', 'P1'] = 10
m.D['P1', 'B'] = 30
m.D['P2', 'P3'] = 8
m.D['P3', 'B'] = 5

# Verificando se todas as rotas têm distâncias definidas
for route in m.setRoutes:
    if (route[0], route[1]) not in m.D:
        raise ValueError(f"Distância não definida para a rota {route[0]}-{route[1]}")

# Definindo variáveis binárias (1 se a rota é usada, 0 caso contrário)
m.x = pyo.Var(m.setRoutes, within=pyo.Binary)

# Função objetivo: minimizar a soma das distâncias das rotas selecionadas
m.obj = pyo.Objective(
    expr=sum(m.x[route[0], route[1]] * m.D[route[0], route[1]] for route in m.setRoutes),
    sense=pyo.minimize
)

# Restrições
# 1. Exatamente uma rota deve sair do ponto de origem (A)
m.C1 = pyo.Constraint(
    expr=sum(m.x['A', j] for j in m.setRoutes_from['A']) == 1
)

# 2. Exatamente uma rota deve chegar ao ponto de destino (B)
m.C2 = pyo.Constraint(
    expr=sum(m.x[i, 'B'] for i in m.setRoutes_to['B']) == 1
)

# 3. Conservação de fluxo: entradas = saídas em pontos intermediários
m.C3 = pyo.ConstraintList()
for i in m.setPoints:
    m.C3.add(
        sum(m.x[i, j] for j in m.setRoutes_from[i]) == 
        sum(m.x[j, i] for j in m.setRoutes_to[i])
    )

# Resolvendo o modelo
opt = SolverFactory('gurobi')
try:
    m.results = opt.solve(m)
    # Verificando se a solução foi encontrada
    if m.results.solver.status == pyo.SolverStatus.ok:
        print("\nSolução encontrada com sucesso!")
    else:
        raise ValueError("O solver não encontrou uma solução ótima.")
except Exception as e:
    print(f"Erro ao resolver o modelo: {str(e)}")
    exit(1)

# Exibindo o modelo completo (opcional, para depuração)
m.pprint()

# Exibindo resultados
print('\n\nValor da Função Objetivo:', pyo.value(m.obj))
print("Rotas ativadas:")
for route in m.setRoutes:
    if pyo.value(m.x[route[0], route[1]]) >= 0.9:  # Considera 0.9 para evitar erros de precisão
        print(f'{route[0]} → {route[1]}')