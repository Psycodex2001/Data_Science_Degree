import pyomo.environ as pyo
from pyomo.opt import SolverFactory
import pandas as pd
import sys  # Importado para usar sys.exit()

# Criação de um modelo abstrato
m = pyo.AbstractModel(name="Seleção de Projetos com Dependências")

# Conjuntos a serem preenchidos pelo CSV
m.setO = pyo.Set(doc="Conjunto de projetos")
m.setD = pyo.Set(within=m.setO * m.setO, doc="Dependências (projeto, pré-requisito)")

# Parâmetros a serem carregados do CSV
m.R = pyo.Param(m.setO, within=pyo.NonNegativeReals, doc="Retorno por projeto")
m.NT = pyo.Param(m.setO, within=pyo.NonNegativeIntegers, doc="Número de times por projeto")

# Parâmetro fixo
m.Nteams = pyo.Param(initialize=5, doc="Total de times disponíveis")

# Variáveis de decisão
m.x = pyo.Var(m.setO, within=pyo.Binary, doc="Seleção de projetos (1 = selecionado, 0 = não)")

# Função objetivo: Maximizar o retorno total
def obj_rule(model):
    return sum(model.x[o] * model.R[o] for o in model.setO)
m.obj = pyo.Objective(rule=obj_rule, sense=pyo.maximize, doc="Retorno total")

# Restrições
def teams_limit_rule(model):
    return sum(model.x[o] * model.NT[o] for o in model.setO) <= model.Nteams
m.C1 = pyo.Constraint(rule=teams_limit_rule, doc="Limite de times")

def dependency_rule(model, dep, pre):
    return model.x[dep] <= model.x[pre]
m.C2 = pyo.Constraint(m.setD, rule=dependency_rule, doc="Restrições de dependência")

# Função para carregar dados do CSV de tabela única
def load_data_from_csv(csv_file):
    try:
        # Lê o CSV
        df = pd.read_csv(csv_file)
        print("Conteúdo bruto do CSV:")
        print(df)
        
        # Verifica as colunas disponíveis
        print("Colunas encontradas:", df.columns.tolist())
        
        # Extrai projetos únicos e seus atributos
        if 'Projeto' not in df.columns:
            raise ValueError("Coluna 'Projeto' não encontrada no CSV")
        projetos_data = df[['Projeto', 'Retorno', 'Times']].drop_duplicates(subset=['Projeto']).dropna(subset=['Projeto']).copy()
        projetos_data['Retorno'] = projetos_data['Retorno'].astype(float)  # Converte para float
        projetos_data['Times'] = projetos_data['Times'].astype(int)  # Converte para int
        projetos_dict = projetos_data.set_index('Projeto').to_dict()
        
        # Extrai dependências onde 'Dependencia' e 'PreRequisito' estão preenchidos
        if 'Dependencia' not in df.columns or 'PreRequisito' not in df.columns:
            print("Aviso: Colunas 'Dependencia' ou 'PreRequisito' não encontradas. Assumindo sem dependências.")
            dependencias_list = []
        else:
            dependencias_data = df.dropna(subset=['Dependencia', 'PreRequisito'])[['Dependencia', 'PreRequisito']]
            dependencias_list = [(dep, pre) for dep, pre in zip(dependencias_data['Dependencia'], dependencias_data['PreRequisito']) if pd.notna(pre)]
            print("Dependências extraídas:", dependencias_list)
        
        # Cria dicionário de dados para Pyomo
        data = {
            None: {
                'setO': {None: list(projetos_data['Projeto'])},
                'setD': {None: dependencias_list},
                'R': projetos_dict['Retorno'],
                'NT': projetos_dict['Times'],
                'Nteams': {None: 5}
            }
        }
        return data
    except Exception as e:
        raise ValueError(f"Erro ao processar o CSV: {str(e)}")

# Carrega os dados do arquivo CSV
csv_file = 'projetos.csv'
try:
    data = load_data_from_csv(csv_file)
except ValueError as e:
    print(e)
    sys.exit(1)  # Usa sys.exit() em vez de exit()

# Cria uma instância do modelo com os dados carregados
instance = m.create_instance(data)

# Resolução do modelo
try:
    opt = SolverFactory('gurobi')
    if not opt.available():
        print("Gurobi não disponível. Usando CBC...")
        opt = SolverFactory('cbc')
    
    results = opt.solve(instance, tee=True)
    
    if results.solver.status == pyo.SolverStatus.ok and \
       results.solver.termination_condition == pyo.TerminationCondition.optimal:
        print("\n=== Resultados ===")
        print(f"Valor ótimo da função objetivo: {pyo.value(instance.obj):.2f}")
        print("\nProjetos selecionados:")
        for o in instance.setO:
            if pyo.value(instance.x[o]) > 0.5:
                print(f"Projeto {o}: Selecionado (Retorno: {instance.R[o]}, Times: {instance.NT[o]})")
        
        total_times = sum(pyo.value(instance.x[o]) * instance.NT[o] for o in instance.setO)
        print(f"\nTotal de times utilizados: {total_times:.0f}/{instance.Nteams.value}")  # Corrige exibição de Nteams
    else:
        print("Não foi possível encontrar uma solução ótima.")
        
except Exception as e:
    print(f"Erro ao resolver o modelo: {str(e)}")