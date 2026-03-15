#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 11:22:18 2025

@author: maurizio
"""

import pyomo.environ as pyo
from pyomo.opt import SolverFactory

# Criando o modelo concreto para otimização
m = pyo.ConcreteModel()

# Definindo os pontos do problema (origem, intermediários e destino)
m.setAllPoints = ['A', 'P1', 'P2', 'P3', 'P4', 'B']  # Adicionamos P4 para mais complexidade
m.setPoints = ['P1', 'P2', 'P3', 'P4']  # Pontos intermediários

# Definindo as rotas possíveis entre os pontos (origem, destino)
m.setRoutes = [['A', 'P1'], ['A', 'P2'], ['P1', 'P2'], ['P1', 'P4'], 
               ['P2', 'P1'], ['P2', 'P3'], ['P3', 'P4'], ['P4', 'B'], 
               ['P3', 'B'], ['P1', 'B']]

# Criando dicionários para organizar rotas que saem e chegam em cada ponto
m.setRoutes_from = {key: [] for key in m.setAllPoints}  # Rotas saindo de cada ponto
m.setRoutes_to = {key: [] for key in m.setAllPoints}    # Rotas chegando em cada ponto
for route in m.setRoutes:
    m.setRoutes_from[route[0]].append(route[1])  # Adiciona destino às rotas saindo
    m.setRoutes_to[route[1]].append(route[0])    # Adiciona origem às rotas chegando

# Definindo as distâncias entre os pontos (em quilômetros, por exemplo)
m.D = {}
m.D['A', 'P1'] = 2
m.D['A', 'P2'] = 7
m.D['P1', 'P2'] = 10
m.D['P1', 'P4'] = 15
m.D['P2', 'P1'] = 10
m.D['P2', 'P3'] = 8
m.D['P3', 'P4'] = 6
m.D['P4', 'B'] = 4
m.D['P3', 'B'] = 5
m.D['P1', 'B'] = 30

# Definindo os custos de pedágio para cada rota (em reais, por exemplo)
m.C = {}
m.C['A', 'P1'] = 5
m.C['A', 'P2'] = 10
m.C['P1', 'P2'] = 8
m.C['P1', 'P4'] = 12
m.C['P2', 'P1'] = 8
m.C['P2', 'P3'] = 6
m.C['P3', 'P4'] = 4
m.C['P4', 'B'] = 3
m.C['P3', 'B'] = 7
m.C['P1', 'B'] = 15

# Verificando se todas as rotas têm distâncias e custos definidos
for route in m.setRoutes:
    if (route[0], route[1]) not in m.D:
        raise ValueError(f"Distância não definida para a rota {route[0]}-{route[1]}")
    if (route[0], route[1]) not in m.C:
        raise ValueError(f"Custo de pedágio não definido para a rota {route[0]}-{route[1]}")

# Definindo o orçamento máximo para pedágios (em reais)
m.budget = 25  # Não podemos gastar mais que 25 reais em pedágios

# Definindo variáveis binárias: 1 se usamos a rota, 0 se não usamos
m.x = pyo.Var(m.setRoutes, within=pyo.Binary)

# Função objetivo: minimizar a soma de distâncias e custos de pedágio
m.obj = pyo.Objective(
    expr=sum(m.x[route[0], route[1]] * (m.D[route[0], route[1]] + m.C[route[0], route[1]]) 
             for route in m.setRoutes),
    sense=pyo.minimize
)

# Restrições do modelo
# 1. Uma única rota deve sair do ponto de origem (A)
m.C1 = pyo.Constraint(
    expr=sum(m.x['A', j] for j in m.setRoutes_from['A']) == 1
)

# 2. Uma única rota deve chegar ao ponto de destino (B)
m.C2 = pyo.Constraint(
    expr=sum(m.x[i, 'B'] for i in m.setRoutes_to['B']) == 1
)

# 3. Conservação de fluxo: entradas iguais às saídas nos pontos intermediários
m.C3 = pyo.ConstraintList()
for i in m.setPoints:
    m.C3.add(
        sum(m.x[i, j] for j in m.setRoutes_from[i]) == 
        sum(m.x[j, i] for j in m.setRoutes_to[i])
    )

# 4. Restrição de orçamento: soma dos pedágios não pode exceder o limite
m.C4 = pyo.Constraint(
    expr=sum(m.x[route[0], route[1]] * m.C[route[0], route[1]] for route in m.setRoutes) <= m.budget
)

# Configurando e resolvendo o modelo com o solver Gurobi
opt = SolverFactory('gurobi')
try:
    m.results = opt.solve(m)  # Resolve o modelo
    if m.results.solver.status == pyo.SolverStatus.ok:
        print("\nSolução encontrada com sucesso!")
    else:
        raise ValueError("O solver não conseguiu encontrar uma solução ótima.")
except Exception as e:
    print(f"Erro ao resolver o modelo: {str(e)}")
    exit(1)

# Exibindo os resultados
print('\n\nValor Total (Distância + Pedágio):', pyo.value(m.obj))
print(f"Custo Total de Pedágio: {sum(pyo.value(m.x[r[0], r[1]]) * m.C[r[0], r[1]] for r in m.setRoutes):.2f}")
print("Rotas ativadas:")
for route in m.setRoutes:
    if pyo.value(m.x[route[0], route[1]]) >= 0.9:  # Usamos 0.9 para evitar erros de precisão
        print(f"{route[0]} → {route[1]} (Distância: {m.D[route[0], route[1]]}, Pedágio: {m.C[route[0], route[1]]})")
