#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 09:59:40 2025
@author: maurizio
"""

# Importação das bibliotecas necessárias
import pyomo.environ as pyo  # Para modelagem de otimização
import numpy as np           # Para cálculos numéricos e limites infinitos
import time                  # Para medir o tempo de execução
from pyomo.opt import SolverFactory  # Para configurar o solver
import matplotlib.pyplot as plt  # Para visualização gráfica
from matplotlib.patches import Polygon  # Para destacar a região viável

# Criação do modelo concreto
model = pyo.ConcreteModel(name="Problema de Otimização Linear")

# Definição das variáveis de decisão
# x: variável com limite superior 3, sem limite inferior
# y: variável não negativa
model.x = pyo.Var(bounds=(-np.inf, 3), within=pyo.Reals, name="x")
model.y = pyo.Var(bounds=(0, np.inf), within=pyo.Reals, name="y")

# Atribuindo variáveis a nomes locais para facilitar a escrita
x = model.x
y = model.y

# Definição das restrições
# Cada restrição é uma inequação linear que define a região viável
model.C1 = pyo.Constraint(expr=x + y <= 8, name="x + y <= 8")
model.C2 = pyo.Constraint(expr=8*x + 3*y >= -24, name="8x + 3y >= -24")
model.C3 = pyo.Constraint(expr=-6*x + 8*y <= 48, name="-6x + 8y <= 48")
model.C4 = pyo.Constraint(expr=3*x + 5*y <= 15, name="3x + 5y <= 15")

# Definição da função objetivo
# Minimizar -4x - 2y (equivalente a maximizar 4x + 2y)
model.obj = pyo.Objective(expr=-4*x - 2*y, sense=pyo.minimize, name="Função Objetivo")

# Medição do tempo de execução
tempo_inicial = time.time()

# Configuração do solver
opt = SolverFactory('gurobi')  # Pode usar 'glpk' ou 'cbc' se Gurobi não estiver disponível

# Resolução do modelo
results = opt.solve(model)

# Cálculo do tempo total de execução
tempo_final = time.time()
tempo_execucao = tempo_final - tempo_inicial

# Extração dos valores ótimos
x_value = pyo.value(model.x)
y_value = pyo.value(model.y)
obj_value = pyo.value(model.obj)

# Exibição dos resultados
print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
print(f"Valor ótimo de x: {x_value:.4f}")
print(f"Valor ótimo de y: {y_value:.4f}")
print(f"Valor da função objetivo: {obj_value:.4f}")

# --- Visualização com Matplotlib ---

# Definir intervalo para o gráfico
# Ajustamos os limites para focar na região viável
x_min, x_max = -1, 4
y_min, y_max = -1, 9
x_range = np.linspace(x_min, x_max, 400)
y_range = np.linspace(y_min, y_max, 400)

# Criar figura
plt.figure(figsize=(10, 10))

# --- Plotar as retas e regiões das restrições ---

# Restrição 1: x + y <= 8 -> y = 8 - x
# Região: abaixo da reta
plt.plot(x_range, 8 - x_range, 'b-', label='Restrição 1: x + y ≤ 8 (abaixo)')
plt.fill_between(x_range, y_min, 8 - x_range, where=(8 - x_range >= y_min), alpha=0.15, color='blue', hatch='//')
plt.annotate('x + y ≤ 8', xy=(2, 6), xytext=(1, 7), arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=10)

# Restrição 2: 8x + 3y >= -24 -> y >= (-24 - 8x)/3
# Região: acima da reta
y_C2 = (-24 - 8 * x_range) / 3
plt.plot(x_range, y_C2, 'r-', label='Restrição 2: 8x + 3y ≥ -24 (acima)')
plt.fill_between(x_range, y_C2, y_max, where=(y_C2 <= y_max), alpha=0.15, color='red', hatch='\\')
plt.annotate('8x + 3y ≥ -24', xy=(0, -8), xytext=(1, -6), arrowprops=dict(facecolor='red', shrink=0.05), fontsize=10)

# Restrição 3: -6x + 8y <= 48 -> y <= (48 + 6x)/8
# Região: abaixo da reta
y_C3 = (48 + 6 * x_range) / 8
plt.plot(x_range, y_C3, 'g-', label='Restrição 3: -6x + 8y ≤ 48 (abaixo)')
plt.fill_between(x_range, y_min, y_C3, where=(y_C3 >= y_min), alpha=0.15, color='green', hatch='x')
plt.annotate('-6x + 8y ≤ 48', xy=(0, 6), xytext=(1, 8), arrowprops=dict(facecolor='green', shrink=0.05), fontsize=10)

# Restrição 4: 3x + 5y <= 15 -> y <= (15 - 3x)/5
# Região: abaixo da reta
y_C4 = (15 - 3 * x_range) / 5
plt.plot(x_range, y_C4, 'm-', label='Restrição 4: 3x + 5y ≤ 15 (abaixo)')
plt.fill_between(x_range, y_min, y_C4, where=(y_C4 >= y_min), alpha=0.15, color='magenta', hatch='*')
plt.annotate('3x + 5y ≤ 15', xy=(3, 1), xytext=(2, 2), arrowprops=dict(facecolor='magenta', shrink=0.05), fontsize=10)

# Restrição 5: x <= 3
# Região: à esquerda da linha
plt.axvline(x=3, color='c', linestyle='--', label='Restrição 5: x ≤ 3 (esquerda)')
# Corrigimos o 'where' para ser um array booleano compatível com y_range
plt.fill_betweenx(y_range, x_min, 3, alpha=0.15, color='cyan', hatch='.')  # Removemos 'where' pois x_min <= 3 é sempre verdadeiro no intervalo
plt.annotate('x ≤ 3', xy=(3, 4), xytext=(2, 5), arrowprops=dict(facecolor='cyan', shrink=0.05), fontsize=10)

# Restrição 6: y >= 0
# Região: acima da linha
plt.axhline(y=0, color='orange', linestyle='--', label='Restrição 6: y ≥ 0 (acima)')  # Cor alterada para maior prefere
plt.fill_between(x_range, 0, y_max, alpha=0.15, color='orange', hatch='-')
plt.annotate('y ≥ 0', xy=(0, 0), xytext=(1, 1), arrowprops=dict(facecolor='orange', shrink=0.05), fontsize=10)

# --- Destacar a região viável ---
# Vértices da região viável (calculados aproximadamente com base nas interseções)
vertices = [
    (0, 0),    # y = 0, x = 0
    (3, 0),    # x = 3, y = 0
    (3, 1.2),  # x = 3, 3x + 5y = 15
    (1.5, 2.1),# Aproximado: 3x + 5y = 15 e x + y = 8
    (0, 6),    # x + y = 8, x = 0
]
regiao_viavel = Polygon(vertices, closed=True, facecolor='gray', alpha=0.3, label='Região Viável (interseção)')
plt.gca().add_patch(regiao_viavel)

# --- Plotar a reta da função objetivo no ponto ótimo ---
# Função objetivo: -4x - 2y = obj_value -> y = (-obj_value - 4x)/2
y_obj = (-obj_value - 4 * x_range) / 2
plt.plot(x_range, y_obj, 'k--', label=f'Função Objetivo: -4x - 2y = {obj_value:.2f}')

# --- Plotar o ponto ótimo ---
plt.plot(x_value, y_value, 'ro', markersize=10, label=f'Ponto Ótimo ({x_value:.2f}, {y_value:.2f})')

# --- Configurações do gráfico ---
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Visualização do Problema de Otimização Linear', fontsize=14)
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)

# Salvar o gráfico
plt.tight_layout()
plt.savefig('regiao_viavel_corrigida.png', bbox_inches='tight')
plt.close()

print("Gráfico salvo como 'regiao_viavel_corrigida.png'")