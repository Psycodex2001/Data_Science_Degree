#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 14:20:46 2025

@author: maurizio
"""

import pyomo.environ as pyo
from pyomo.opt import SolverFactory

# Criação do modelo concreto com nome descritivo
m = pyo.ConcreteModel(name="Seleção de Projetos com Dependências")

# Conjuntos e parâmetros fixos no código
m.setO = pyo.Set(initialize=['A', 'B', 'C', 'D', 'E'])  # Conjunto de projetos disponíveis
m.R = {'A': 500, 'B': 4000, 'C': 3000, 'D': 2000, 'E': 2000}  # Retorno financeiro por projeto
m.NT = {'A': 1, 'B': 3, 'C': 2, 'D': 1, 'E': 5}  # Número de times necessários por projeto
m.Nteams = 5  # Total de times disponíveis

# Variáveis de decisão
# x[o] = 1 se o projeto o é selecionado, 0 caso contrário
m.x = pyo.Var(m.setO, within=pyo.Binary, doc="Seleção de projetos")

# Função objetivo
# Maximiza o retorno total dos projetos selecionados
m.obj = pyo.Objective(
    expr=sum(m.x[o] * m.R[o] for o in m.setO),
    sense=pyo.maximize,
    doc="Retorno total"
)

# Restrições
m.C1 = pyo.Constraint(
    expr=sum(m.x[o] * m.NT[o] for o in m.setO) <= m.Nteams,
    doc="Limite de times disponíveis"
)
m.C2 = pyo.Constraint(
    expr=m.x['C'] <= m.x['A'],
    doc="Projeto C depende do projeto A"
)
m.C3 = pyo.Constraint(
    expr=m.x['D'] <= m.x['A'],
    doc="Projeto D depende do projeto A"
)
m.C4 = pyo.Constraint(
    expr=m.x['D'] <= m.x['C'],
    doc="Projeto D depende do projeto C"
)

# Resolução do modelo
try:
    # Configuração do solver (Gurobi como preferência)
    opt = SolverFactory('gurobi')
    
    # Verifica se o Gurobi está disponível, usa CBC como alternativa
    if not opt.available():
        print("Gurobi não disponível. Tentando CBC como alternativa...")
        opt = SolverFactory('cbc')
    
    # Resolve o modelo e armazena os resultados
    results = opt.solve(m, tee=True)  # tee=True mostra o log do solver
    
    # Verifica se a solução foi encontrada com sucesso
    if results.solver.status == pyo.SolverStatus.ok and \
       results.solver.termination_condition == pyo.TerminationCondition.optimal:
        print("\n=== Resultados ===")
        print(f"Valor ótimo da função objetivo: {pyo.value(m.obj):.2f}")
        print("\nProjetos selecionados:")
        for o in m.setO:
            if pyo.value(m.x[o]) > 0.5:  # Tolerância numérica para considerar 1
                print(f"Projeto {o}: Selecionado (Retorno: {m.R[o]}, Times: {m.NT[o]})")
        
        # Calcula e exibe o total de times utilizados
        total_times = sum(pyo.value(m.x[o]) * m.NT[o] for o in m.setO)
        print(f"\nTotal de times utilizados: {total_times:.0f}/{m.Nteams}")
    else:
        print("Não foi possível encontrar uma solução ótima.")
        
except Exception as e:
    print(f"Erro ao resolver o modelo: {str(e)}")

# Opcional: exibe a estrutura completa do modelo (descomente se necessário)
# m.pprint()