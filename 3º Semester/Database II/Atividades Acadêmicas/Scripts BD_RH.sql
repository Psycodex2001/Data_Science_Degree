#Criação do BD_RH
create database bd_rh;
#acionar o BD_RH para a execução de comandos
use bd_rh;
#criação da tabela tb_funcionario
create table tb_funcionario(
	matricula int primary key,
    nome varchar(100) not null,
    dtNascimento date not null,
    salario decimal(10,2),
    codCargo int,
    codDepartamento int
);
#criação da tabela tb_cargo
create table tb_cargo(
	codCargo int primary key,
    descricao varchar(100)
);
#criação da tabela tb_departamento
create table tb_departamento(
	codDepartamento int primary key,
    descricao varchar(100)
);
#criação do relacionamento tb_funcionario-tb_cargo
alter table tb_funcionario
add constraint fk_cargo
foreign key (codCargo) references tb_cargo(codCargo);
#criação do relacionamento tb_funcionario-tb_departamento
alter table tb_funcionario
add constraint fk_departamento
foreign key (codDepartamento) references tb_departamento(codDepartamento);
#popular a tabela tb_cargo
insert into tb_cargo (codCargo, descricao)
values  (1,'Enfermeiro(a)'),
		(2,'Administrador(a)'),
        (3,'Analista'),
        (4,'Engenheiro(a)'),
        (5,'Advogado(a)'),
        (6,'Gerente'),
        (7,'Executivo(a)');
#popular a tabela tb_departamento
insert into tb_departamento(codDepartamento, descricao)
values  (1,'Enfermaria'),
		(2,'Administração'),
        (3,'Informática'),
        (4,'Engenharia'),
        (5,'Jurídico'),
        (6,'Logística'),
        (7,'Presidência');
select * from tb_departamento;
#popular a tabela tb_funcionario
insert into tb_funcionario(matricula,nome,dtNascimento, salario, codCargo, codDepartamento)
values  (1,'Ana Clara','1997-07-05',3000,1,5),
		(2,'Patricia Azevedo','1944-07-04',4000,1,1),
        (3,'José Maria','1971-05-10',6000,1,3),
        (4,'Sônia Abrantes','1979-05-29',7000, 1,4),
        (5,'Valdir Reinaldo','1960-09-22',1600,2,2),
        (6,'José Alberto','1955-01-13',15000,2,2);
select * from tb_funcionario;
#Listar registro(s) com codDepartamento = 2 na tabela tb_funcionario
select * from tb_funcionario where codDepartamento = 2;
#Listar registro(s) com codCargo = 1 na tabela tb_funcionario
select * from tb_funcionario where codCargo = 1;
#Remover registro com codCargo = 1 na tabela tb_cargo
delete from tb_cargo where codCargo = 1;
#Remover registro com codDepartamento = 1 na tabela tb_departamento
delete from tb_departamento where codDepartamento = 1;
#Alterar o salário do funcionário com matricula 1 para 6000
update tb_funcionario set salario = 6000 where matricula = 1;
#Diminuir o salário de todos os funcionários em 5%
update tb_funcionario set salario = salario*0.95;
#Listar os funcionários que possem salário > 5000
select * from tb_funcionario where salario > 5000;
#Listar funcionários(as) que são administradores(as)
select * from tb_funcionario where codCargo = 2;
#Listar funcionários(as) que trabalham na enfermaria
select * from tb_funcionario where codDepartamento = 1;
#Listar todos os funcionários, exceto os que trabalham 
#no departamento com codigo = 2
select * from tb_funcionario where codDepartamento <> 2;
#recuperar os registros nos quais o nome do funcionário inicam com Jose
select * from tb_funcionario where nome like 'Jose%';
#recuperar os registros nos quais o ultimo sobrenome seja Abrantes
select * from tb_funcionario where nome like '%Abrantes';
#recuperar os registros que possuem sobre que começa com 'a'
select * from tb_funcionario where nome like '% A%';
#recuperar os funcionarios que possuem os cargos 1, 4 ou 5
select * from tb_funcionario
where codCargo in (1,4,5);
#o comando abaixo traz o meso resultado do comando acima
select * from tb_funcionario
where codCargo = 1 or codCargo = 4 or codCargo = 5;
# Recuperar os registros dos funcionários que recebem entre
# 5000 e 8000
select * from tb_funcionario
where salario between 5000 and 8000;
#O comando abaixo traz os mesmos resultados do de cima
select * from tb_funcionario
where salario >= 5000 and salario <=8000;
# recuperar todos os funcionários ordenando pelo codDepartamento
select * from tb_funcionario order by codDepartamento;
# recuperar os funcionário ordenando pelo codDepartamento e nome
select * from tb_funcionario order by codDepartamento, nome;
# recuperar todos os funcionários ordenando pelo codDepartamento
# em ordem descrescente
select * from tb_funcionario order by codDepartamento desc;
# recuperar os dois primeiros registros da tabela funcionario
select * from tb_funcionario limit 2;
#selecionar codDepartamento da tb_funcionario
select distinct codDepartamento from tb_funcionario;
#Listar todos os funcionários que trabalham no departamento 
# de “Administração”
select * from tb_funcionario where codDepartamento = 2;
#Listar todos os funcionários que possuem o nome que inicia com 
# a letra “J”
select * from tb_funcionario where nome like 'J%';
#Listar os cargos com código igual a 3 e 4
select * from tb_cargo where codCargo in (3,4);
#Listar os nomes funcionários e ordem alfabética
select nome from tb_funcionario order by nome;
#Listar os nomes funcionários e ordem alfabética decrescente
select nome from tb_funcionario order by nome desc;
#Listar os três primeiros registros da tabela tb_departamento
select * from tb_departamento limit 3;
#Listar os funcionários que possuem salário entre 
# R$ 5 mil e R$ 10 mil
select * from tb_funcionario
where salario between 5000 and 10000;
#Listar os funcionários que possuem salário 
# maior que R$ 10 mil ou menor que R$ 5 mil
select * from tb_funcionario
where salario > 10000 or salario < 5000;
#Listar os códigos de cargo existentes na tabela funcionário 
# ordenados de maneira decrescente. Não exiba códigos repetidos.
select distinct codCargo from tb_funcionario 
order by codCargo desc;
#Listar a matrícula do funcionário, o nome do funcionário e a descrição do departamento no qual trabalha
select f.matricula, f.nome, d.descricao
from tb_funcionario as f
inner join tb_departamento as d on f.codDepartamento = d.codDepartamento;
#Listar a matrícula do funcionário, o nome do funcionário e 
# a descrição do cargo do funcionário
select f.matricula, f.nome, c.descricao
from tb_funcionario as f
inner join tb_cargo as c on f.codCargo = c.codCargo;
#Listar a matrícula do funcionário, o nome do funcionário, 
# a descrição do departamento no qual trabalha e a 
#descrição do cargo do funcionário
select f.matricula, f.nome, d.descricao as departamento, c.descricao as cargo
from tb_funcionario as f
inner join tb_departamento as d on f.codDepartamento = d.codDepartamento
inner join tb_cargo as c on f.codCargo = c.codCargo;
#Criar uma view que lista matricula, nome do funcionário e nome do departamento
create view vw_01 as
select matricula, nome, descricao
from tb_funcionario f
inner join tb_departamento d on f.codDepartamento = d.codDepartamento;
select * from vw_01;
#Criar uma view que lista  matricula, nome do funcionário, salário e nome do cargo. 
# A lista deve contemplar apenas funcionários com salário maior ou igual a R$ 5.000,00
create view vw_02 as
select matricula, nome, salario, descricao
from tb_funcionario f
inner join tb_cargo c on f.codCargo = c.codCargo
where salario >=5000;
select * from vw_02;
#Criar uma view que lista matricula, nome do funcionário, salário e 
#nome do departamento. 
#A lista deve contemplar apenas funcionários com salário menor ou igual a R$ 5.000,00
create view vw_03 as
select matricula, nome, salario, descricao
from tb_funcionario f
inner join tb_departamento d on f.codDepartamento = d.codDepartamento
where salario <= 5000;
select * from vw_03;
#Criar uma view que lista matricula, nome do funcionário, salário, 
# departamento e cargo.
create view vw_04 as
select matricula, nome, salario, d.descricao as departamento, c.descricao as cargo
from tb_funcionario f
inner join tb_departamento d on f.codDepartamento = d.codDepartamento
inner join tb_cargo c on f.codCargo = c.codCargo;
select * from vw_04;
#Recuperar o nome do funcionário com o respectivo ano de nascimento
select nome, YEAR(dtNascimento) from tb_funcionario;
# Recuperar o nome do funcionário com o respectivo mês de nascimento
select nome, MONTH(dtNascimento) from tb_funcionario;
# Recuperar o nome do funcionário com o respectivo dia do nascimento 
select nome, DAY(dtNascimento) from tb_funcionario;
select * from tb_funcionario;
# Formatar a data para ser exibida em formato específico
select nome, DATE_FORMAT(dtNascimento, '%d/%m/%Y') from tb_funcionario;
# Recuperar o nome, a data de nascimento e a data atual
select nome, dtNascimento, curdate() from tb_funcionario;
select curdate();
select DATE_FORMAT(curdate(), '%d/%m');
# Recuperar o nome do funcionario, a data de nascimento, a data atual e a
# diferença de dias entre a data atual e a de nasicmento
select nome, dtNascimento, curdate(), dateDiff(curDate(),dtNascimento)
from tb_funcionario;
#vamos ver quantos dias se passaram desde o nosso nascimento
select dateDiff(curDate(),'1983-02-04');
# Recuperar o nome do funcionario, a data de nascimento, a data atual e a
# diferença em anos a data atual e a de nasicmento
select nome, dtNascimento, curdate(), dateDiff(curDate(),dtNascimento)/365
from tb_funcionario;
# Recuperar o nome do funcionario, a data de nascimento, a data atual e a
# diferença ARREDONDADA em anos a data atual e a de nasicmento
select nome, dtNascimento, curdate(), 
		round(dateDiff(curDate(),dtNascimento)/365,0)
from tb_funcionario;
# Função para arredondar para baixo
select nome, dtNascimento, curdate(), 
		floor(dateDiff(curDate(),dtNascimento)/365)
from tb_funcionario;
# Função para arredondar para cima
select nome, dtNascimento, curdate(), 
		ceil(dateDiff(curDate(),dtNascimento)/365)
from tb_funcionario;
# Função timestamp é uma função de operação de datas mais sofisticada que
#a DateDiff.
# retornar o nome e a idade do funcionário utilizando timestampdiff
select nome, timestampdiff(year, dtNascimento, curDate())
from tb_funcionario;
select nome, timestampdiff(month, dtNascimento, curDate()) as diferencaMeses
from tb_funcionario;
select nome, timestampdiff(day, dtNascimento, curDate()) as diferencaDias
from tb_funcionario;
select nome, timestampdiff(hour, dtNascimento, curDate()) as diferencaHoras
from tb_funcionario;
# Retornar a soma de todos os salários da tb_funcionario
select sum(salario) from tb_funcionario;
#Retornar a média dos salários da tb_funcionario
select avg(salario) from tb_funcionario;
#Recuperar a quantidade de linhas (ou registros) da tb_funcionario
select count(matricula) from tb_funcionario;
#Recuperar o maior salário da tb_funcionario
select max(salario) from tb_funcionario;
# Em um comando, recuperar o nome do funcionario que possui o maior salario
select nome
from tb_funcionario
where salario = (select max(salario) from tb_funcionario);
# Recuperar o menor salário da tb_funcionario
select min(salario) from tb_funcionario;
#Listar o menor ano de nascimento da tabela tb_funcionario
select min(Year(dtNascimento)) from tb_funcionario;
#Listar o maior mês de nascimento da tabela tb_funcionário
select max(Month(dtNascimento)) from tb_funcionario;
#Listar o total de registros da tabela tb_cargo
select count(codCargo) from tb_cargo;
#Listar a idade dos funcionários que trabalham no departamento de Enfermaria
select nome, timestampdiff(year,dtNascimento,curDate()) as dtNascimento
from tb_funcionario f
inner join tb_departamento d on f.codDepartamento = d.codDepartamento
where d.descricao = 'Enfermaria';
#Listar o total do salário dos funcionários que possuem 
#o cargo Administrador(a)
select sum(salario)
from tb_funcionario f
inner join tb_cargo c on f.codCargo = c.codCargo
where c.descricao = 'Administrador(a)';

#Listar todos as editoras com os respectivos livros utilizando left outer join
# As editoras que não possuem livros devem ser exibidas.
select e.descricao as editor, l.titulo
from tb_editora e
left outer join tb_livro l on e.codEditora = l.codEditora;
#Recuperar o produto cartesiano dos livros com os genêros
select l.titulo, g.descricao
from tb_genero g
cross join tb_livro l;
#Listar todos os departamentos com os respectivos funcionários utilizando o left outer join
#Os departamentos que não possuem funcionários devem ser exibidos
select d.descricao as departamento, f.nome
from tb_departamento d
left outer join tb_funcionario f on d.codDepartamento = f.codDepartamento;
#Listar todos os funcionários com os respectivos cargos utilizando o right outer join
#Os cargos que não possuem funcionários devem ser exibidos
select f.nome, c.descricao as cargo
from tb_funcionario f
right outer join tb_cargo c on f.codCargo = c.codCargo;
#Listar cada cargo com todos os funcionário
select c.descricao as cargo, f.nome
from tb_cargo c
cross join tb_funcionario f;
#Listar cada departamento com todos os funcionários
select d.descricao as departamento, f.nome
from tb_departamento d
cross join tb_funcionario f;
#Listar cada título de livro com todas as editoras
select l.titulo, e.descricao
from tb_livro l
cross join tb_editora e;
#Listar a quantidade de funcionários por departamento
select d.descricao as departamento, count(*) as quantidade
from tb_departamento d
inner join tb_funcionario f on d.codDepartamento = f.codDepartamento
group by departamento
order by quantidade desc;
#Listar a quantidade de funcionários por cargo, 
#ordenando a quantidade por ordem descrescente
select c.descricao as cargo, count(*) as quantidade
from tb_cargo c
inner join tb_funcionario f on c.codCargo = f.codCargo
group by cargo
order by quantidade desc;
#Listar o valor total dos salários de cada departamento
select d.descricao as departamento, sum(f.salario) as total
from tb_departamento d
inner join tb_funcionario f on d.codDepartamento = f.codDepartamento
group by departamento
order by total desc;
#Listar a média salarial por cargo
select c.descricao as cargo, avg(f.salario) as media
from tb_cargo c
inner join tb_funcionario f on c.codCargo = f.codCargo
group by cargo
order by media desc;
#Diminuir em 10% os salários dos funcionários e depois desfazer a transação
select * from tb_funcionario;
start transaction;
update tb_funcionario set salario = salario*0.9;
select * from tb_funcionario;
rollback;
select * from tb_funcionario;
#Aumentar em 10% os salários dos funcionários e efetivar a transação
start transaction;
update tb_funcionario set salario = salario * 1.1;
select * from tb_funcionario;
commit;
select * from tb_funcionario;
#Listar os funcionários que recebem abaixo da média salarial
select nome, salario from tb_funcionario
where salario < (select avg(salario) from tb_funcionario);
#Listar os funcionários, com a descrição dos respectivos cargos, 
# que recebem acima da média salarial
select nome, descricao, salario
from tb_funcionario f
inner join tb_cargo c on f.codCargo = c.codCargo
where
salario > (select avg(salario) from tb_funcionario);
#Listar os dados da TB_funcionário referentes ao registro do 
# funcionário que possui o maior salário
select * from tb_funcionario
where salario = (select max(salario) from tb_funcionario);
#Listar os dados do funcionário referentes ao registro do 
# funcionário que possui o menor salário
select * from tb_funcionario
where salario = (select min(salario) from tb_funcionario);
#Listar a descrição do cargo com a respectiva quantidade de funcionários, 
# exibindo apenas os cargos que possuem mais de um funcionário
select descricao, count(*) as qtd
from tb_cargo c
inner join tb_funcionario f on c.codCargo = f.codCargo
group by descricao
having qtd > 1;
#análise de índices
show index from tb_funcionario;
create index idx_dtNascimento on tb_funcionario(dtNascimento);

# Criar uma stored procedure para listar 
#(Matricula, funcionário, salario) da tb_funcionario 
DELIMITER //
create procedure getFuncionarios()
begin
	select * from tb_funcionario;
END //
DELIMITER ;
call getFuncionarios();
#Criar uma stored procedure para alterar o nome do funcionario 
# a partir da matricula 
DELIMITER //
create procedure alteraNome(codFuncionario INT, novoNome VARCHAR(100))
begin
	update tb_funcionario set nome  = novoNome 
    where matricula = codFuncionario;
	select * from tb_funcionario;
end //
DELIMITER ;
CALL alteraNome(1, 'Ricardo Akl');
#Criar uma stored procedure para listar os funcionários por codCargo
DELIMITER //
create procedure listaFuncionario(cargo int)
begin
	select * from tb_funcionario 
    where codcargo = cargo;
end //
DELIMITER ;
CALL listaFuncionario(2);
