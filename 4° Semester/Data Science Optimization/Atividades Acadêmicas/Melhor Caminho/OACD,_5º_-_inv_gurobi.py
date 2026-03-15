import pyomo.environ as pyo
from pyomo.opt import SolverFactory

# Criando o modelo concreto
m = pyo.ConcreteModel()

# Definindo o conjunto de máquinas e a demanda
m.setMachine = pyo.Set(initialize=['A', 'B', 'C'])  # Máquinas disponíveis
m.Demand = 10000  # Demanda total a ser atendida

# Definindo variáveis
m.C = pyo.Var(m.setMachine, bounds=(0, None))  # Custo de produção por máquina
m.P = pyo.Var(m.setMachine, within=pyo.NonNegativeIntegers)  # Produção (inteiros >= 0)

# Função objetivo: minimizar a soma dos custos
m.obj = pyo.Objective(expr=pyo.summation(m.C), sense=pyo.minimize)

# Restrições
m.C1 = pyo.Constraint(expr=pyo.summation(m.P) == m.Demand)  # Soma da produção = demanda
m.C2 = pyo.Constraint(expr=m.C['A'] == 0.1 * m.P['A']**2 + 0.5 * m.P['A'] + 0.1)  # Custo de A
m.C3 = pyo.Constraint(expr=m.C['B'] == 0.3 * m.P['B'] + 0.5)  # Custo de B
m.C4 = pyo.Constraint(expr=m.C['C'] == 0.05 * m.P['C']**2 + 0.1 * m.P['C'])  # Custo de C

# Resolvendo com Gurobi
opt = SolverFactory('gurobi')
try:
    m.results = opt.solve(m, tee=True)  # Mostra o log do solver
    if m.results.solver.status == pyo.SolverStatus.ok:
        print("\nSolução encontrada com sucesso!")
    else:
        print("O solver não encontrou uma solução ótima.")
except Exception as e:
    print(f"Erro ao resolver o modelo: {str(e)}")
    exit(1)

# Exibindo resultados
print('\n\nCusto Total:', pyo.value(m.obj))
for machine in m.setMachine:
    print(f"Máquina {machine}: Produção = {pyo.value(m.P[machine])}, Custo = {pyo.value(m.C[machine])}")