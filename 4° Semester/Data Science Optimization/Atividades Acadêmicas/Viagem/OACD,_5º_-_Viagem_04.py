#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 17:09:41 2025

@author: maurizio
"""

from pyomo.environ import *

# --- 1. DADOS DO PROBLEMA ---
# Aqui, guardamos as informações sobre as opções de viagem.
# Exemplo 4: Minimizar o Tempo de Viagem com Orçamento

# Opções de ida (EUA para Espanha)
opcoes_ida = {
    'A': {'tempo': 8, 'custo': 2000},  # Opção A: 8 horas, 2000 dólares
    'B': {'tempo': 12, 'custo': 1000}, # Opção B: 12 horas, 1000 dólares
    'C': {'tempo': 16, 'custo': 900}  # Opção C: 16 horas, 900 dólares
}

# Opções de volta (Espanha para EUA)
opcoes_volta = {
    'D': {'tempo': 9, 'custo': 1500}, # Opção D: 9 horas, 1500 dólares
    'E': {'tempo': 32, 'custo': 500} # Opção E: 32 horas, 500 dólares
}

orcamento = 2500  # Orçamento máximo disponível para a viagem (em dólares)

# --- 2. CRIANDO O MODELO ---
# Aqui, vamos montar o modelo matemático usando o Pyomo.

modelo = ConcreteModel()  # Cria um modelo concreto (onde os dados são definidos diretamente)

# --- 3. CONJUNTOS DE OPÇÕES ---
# Vamos criar "listas" (conjuntos) para as opções de ida e volta.

modelo.I = Set(initialize=opcoes_ida.keys())  # Conjunto I: 'A', 'B', 'C' (opções de ida)
modelo.J = Set(initialize=opcoes_volta.keys()) # Conjunto J: 'D', 'E' (opções de volta)

# --- 4. VARIÁVEIS DE ESCOLHA ---
# Criamos variáveis para representar se cada opção de voo foi escolhida ou não.
# São variáveis "binárias": 1 se a opção for escolhida, 0 se não for.

modelo.x = Var(modelo.I, within=Binary) # Variáveis x: x['A'], x['B'], x['C']
modelo.y = Var(modelo.J, within=Binary) # Variáveis y: y['D'], y['E']

# --- 5. FUNÇÃO OBJETIVO ---
# Definimos o que queremos minimizar: o tempo total da viagem.

# Calcula o tempo total somando os tempos das opções escolhidas
modelo.tempo_total = Objective(
    expr=sum(modelo.x[i] * opcoes_ida[i]['tempo'] for i in modelo.I) +
         sum(modelo.y[j] * opcoes_volta[j]['tempo'] for j in modelo.J),
    sense=minimize  # Queremos minimizar o tempo
)

# --- 6. RESTRIÇÕES ---
# Definimos as regras que o modelo deve seguir.

# Restrição 1: Escolher exatamente uma opção de ida
modelo.uma_opcao_ida = Constraint(
    expr=sum(modelo.x[i] for i in modelo.I) == 1
)

# Restrição 2: Escolher exatamente uma opção de volta
modelo.uma_opcao_volta = Constraint(
    expr=sum(modelo.y[j] for j in modelo.J) == 1
)

# Restrição 3: O custo total não pode ultrapassar o orçamento
modelo.limite_orcamento = Constraint(
    expr=sum(modelo.x[i] * opcoes_ida[i]['custo'] for i in modelo.I) +
         sum(modelo.y[j] * opcoes_volta[j]['custo'] for j in modelo.J) <= orcamento
)

# --- 7. RESOLVENDO O PROBLEMA ---
# Pedimos para o Pyomo encontrar a melhor solução usando o GLPK (ou outro solver).

solucionador = SolverFactory('glpk')  # Escolhe o GLPK para resolver o problema
resultados = solucionador.solve(modelo) # Encontra a solução

# --- 8. MOSTRANDO O RESULTADO ---

# Verifica se o solver encontrou uma solução
print("Status da solução:", resultados.solver.status)

if resultados.solver.status == 'ok': # Se encontrou uma solução...
    print("Tempo total de viagem:", modelo.tempo_total()) # Mostra o tempo total
    print("Custo total de viagem:", sum(modelo.x[i]() * opcoes_ida[i]['custo'] for i in modelo.I) +
                                 sum(modelo.y[j]() * opcoes_volta[j]['custo'] for j in modelo.J))
    print("Rota de ida:")
    for i in modelo.I: # Para cada opção de ida...
        if modelo.x[i]() == 1: # Se a opção foi escolhida...
            print(f"  Opção {i}: {opcoes_ida[i]['tempo']} horas, US${opcoes_ida[i]['custo']}")
    print("Rota de volta:")
    for j in modelo.J: # Para cada opção de volta...
        if modelo.y[j]() == 1: # Se a opção foi escolhida...
            print(f"  Opção {j}: {opcoes_volta[j]['tempo']} horas, US${opcoes_volta[j]['custo']}")
else: # Se não encontrou uma solução...
    print("Não foi possível encontrar uma solução ótima.")