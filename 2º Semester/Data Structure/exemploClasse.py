class Pessoa:
    def __init__(self,nome,cpf):
        self.nome=nome
        self.cpf=cpf
    
p=Pessoa("joao","123.123.123-00")

print(p.nome)
print(p.cpf)