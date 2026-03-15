#criar o banco de dados BD_LIVRO
create database bd_livro;
#selecionar o banco de dados BD_LIVRO para execução de comandos
use bd_livro;
#criar tb_livro
create table tb_livro(
	isbn int primary key,
    titulo varchar(100) not null,
    preco decimal (10,2),
    codGenero int,
    codEditora int
);
#criar tb_genero
create table tb_genero(
	codGenero int primary key,
    descricao varchar(100)
);
#criar tb_editora
create table tb_editora(
	codEditora int primary key,
    descricao varchar(100)
);
#criar relacionamento tb_livro-tb_genero
alter table tb_livro
add constraint fk_genero
foreign key (codGenero) references tb_genero(codGenero);
#criar relacionamento tb_livro-tb_editora
alter table tb_livro
add constraint fk_editora
foreign key (codEditora) references tb_editora(codEditora);
# adicionar a coluna dtPublicacao na tb_livro
alter table tb_livro
add dtPublicacao date;
#Alterar o tipo da coluna dtPublicacao para datetime e not null
alter table tb_livro
modify column dtPublicacao datetime not null;
#Remover a coluna dtPublicacao da tb_livro
alter table tb_livro
drop column dtPublicacao;
# Mudar o nome da coluna titulo para tituloLivro
alter table tb_livro
change titulo tituloLivro varchar(100);
# Altera novamente o nome da coluna para titulo
alter table tb_livro
change tituloLivro titulo varchar(100);
#criação de tabela de teste
create table tb_teste(
	codTeste int primary key,
    teste varchar(100)
);
#remover a tabela tb_teste
drop table tb_teste;
#selecionar todos os registros da tb_livro
select * from tb_livro;
#inserir o genero computação na tb_genero
insert into tb_genero(codGenero,descricao)
values (1,'Computação');
select * from tb_genero;
#inserir a editora Novatec na tb_editora
insert into tb_editora(codEditora,descricao)
values(1,'Novatec');
select * from tb_editora;
#inserir o livro Banco de Dados na tb_livro
insert into tb_livro(isbn,titulo,preco,codGenero,codEditora)
values (1,'Banco de Dados', 120.50, 1, 1);
select * from tb_livro;
# alimentar a tb_genero com mais genêros
insert into tb_genero(codGenero, descricao)
values  (2,'Medicina'),
		(3,'Engenharia'),
        (4,'Jurídico'),
        (5,'Arquitetura'),
        (6,'Biologia'),
        (7,'Mecatrônica');
select * from tb_genero;
# alimentar a tb_editora
insert into tb_editora(codEditora,descricao)
values  (2,'Amazon'),
		(3,'Coopmed'),
		(4,'Livraria Florence'),
        (5,'Blucher'),
        (6,'Mundial'),
        (7,'Saraiva'),
        (8,'Editora Fórum'),
        (9,'Dickens');
select * from tb_editora;
select * from tb_livro;
#popular a tabela tb_livro
insert into tb_livro (isbn, titulo, preco, codGenero,codEditora)
values  (2,'Engenharia de Software',300,1,1),
		(3, 'Ortopedia',310,2,3),
        (4,'Cardiologia',320,2,4),
        (5,'Estrutura Predial',200,3,5),
        (6,'Estrutura Hidráulica',300,3,6),
        (7,'Direito Penal',150,4,7),
        (8,'Direito Civil',200,4,8),
        (9,'Cores',200,5,7),
        (10, 'Paisagismo',250,5,8),
        (11,'Virus',300,6,9),
        (12,'Bactéria',300,6,9);
select * from tb_livro;
#especificar as colunas que devem ser recuperadas na consulta
select isbn, titulo from tb_livro;
#recuperar todas as colunas e registros da tb_livro
#onde o isbn=4
select * from tb_livro where isbn =4;
#recuperar apenas o titulo e o preço do livro com isbn=4
select titulo, preco from tb_livro where isbn=4;
#atualizar a descrição da editora com codEditora=9
select * from tb_editora where codEditora = 9;
update tb_editora 
set descricao = 'Thomson'
where codEditora = 9;
#atualizar o codEditora e o codGenero do livro
#com isbn = 1
update tb_livro
set codEditora =1, codGenero=2
where isbn=1;
select * from tb_livro;
#remover o livro com isbn=9
delete from tb_livro where isbn=9;
select * from tb_livro;
#Listar registro com codEditora = 1 na tabela tb_editora
select * from tb_editora where codEditora = 1;
#Listar registro(s) com codGenero = 1 na tabela tb_livro
select * from tb_livro where codGenero = 1;
#Remover o registro com codEditora = 2 na tabela tb_editora
delete from tb_editora where codEditora = 2;
#Remover registro com codGenero = 1 na tabela tb_genero
delete from tb_genero where codGenero = 1;
#Alterar o preço do livro com ISBN=1 para 500.00
update tb_livro set preco = 500 where isbn = 1;
#Aumentar o preço de todos os livros em 10%
update tb_livro set preco = preco * 1.1;
update tb_livro set preco = preco + (preco*10/100);
update tb_livro set preco = preco + (preco*0.10);
#Listar os registros da tabela tb_livro que possuem 
# preço > 350
select * from tb_livro where preco > 350;
#Listar os livros da editora com código 8
select * from tb_livro where codEditora = 8;
# recuperar o titulo do livro e a descrição da editora
select tb_livro.titulo, tb_editora.descricao
from tb_livro
inner join tb_editora on tb_livro.codEditora = tb_editora.codEditora;
# Desenvolva um script SQL que exiba os títulos dos livros 
# com as respectivas descrições dos gêneros
select tb_livro.titulo, tb_genero.descricao
from tb_livro
inner join tb_genero on tb_livro.codGenero = tb_genero.codGenero;
#Desenvolva um script SQL que exiba os títulos dos livros, 
#os respectivos gêneros e as respectivas editoras 
select tb_livro.titulo, tb_genero.descricao, tb_editora.descricao
from tb_livro
inner join tb_genero on tb_livro.codGenero = tb_genero.codGenero
inner join tb_editora on tb_livro.codEditora = tb_editora.codEditora;
#Listar titulo e a descrição da editora quando o preço for maior que R$250,00
select l.titulo, e.descricao
from tb_livro as l
inner join tb_editora as e on l.codEditora = e.codEditora
where l.preco > 250;
#Listar titulo e a descrição do gênero quando o preço for entre R$200,00 e R$300,00
select l.titulo, g.descricao
from tb_livro l
inner join tb_genero g on l.codGenero = g.codGenero
where preco between 200 and 300;
#Listar título, descrição da editora e descrição do gênero quando o código 
# da editora for 1, 2 ou 3
select l.titulo, e.descricao as editora, g.descricao as genero
from tb_livro l
inner join tb_editora e on l.codEditora = e.codEditora
inner join tb_genero g on l.codGenero = g.codGenero
where e.codEditora in (1,2,3);
#Listar título e a descrição da editora dos registros que possuem 
# a descrição da editora igual a “Novatec”
select l.titulo, e.descricao as editora
from tb_livro l
inner join tb_editora e on l.codEditora = e.codEditora
where e.descricao like 'Novatec';
#criar uma view, denominada vw_01, que contemplará 
# o titulo e o preço dos livros
create view vw_01 as
select titulo, preco from tb_livro;
select * from vw_01;
# criar uma view que contempla o ISBN e o título dos livros
create view vw_02 as
select isbn, titulo from tb_livro;
select * from vw_02;
# criar uma view para exibir o titulo 
# com a descrição da editora correspondente
create view vw_03 as
select l.titulo, e.descricao
from tb_livro l 
inner join tb_editora e on l.codEditora = e.codEditora;
#Criar uma view que liste ISBN, titulo e preco
create view vw_04 as
select isbn, titulo, preco
from tb_livro;
select * from vw_04;
#Criar uma view que liste ISBN, titulo, preco e 
# preco com 10% de desconto
create view vw_05 as
select isbn, titulo, preco, preco*0.9 as precoComDesconto
from tb_livro;
select * from vw_05;
#Criar uma view que liste ISBN, titulo e editora
create view vw_06 as
select isbn, titulo, descricao
from tb_livro l
inner join tb_editora e on l.codEditora = e.codEditora;
select * from vw_06;
#Criar uma view que liste ISBN, titulo e gênero
create view vw_07 as
select isbn, titulo, descricao
from tb_livro l
inner join tb_genero g on l.codGenero = g.codGenero;
select * from vw_07;
#Criar uma view que liste ISBN, titulo, preco, 
# editora e gênero ordenada por preço
create view vw_08 as
select isbn, titulo, preco, e.descricao as editora, g.descricao as genero
from tb_livro l
inner join tb_editora e on l.codEditora = e.codEditora
inner join tb_genero g on l.codGenero = g.codGenero;
select * from vw_08;

#retornar todas as editoras com os respectivos livros.
#as editoras que não possuem livros associados também deve ser retornadas
select e.descricao as editora, l.titulo
from tb_editora e
inner join tb_livro l on e.codEditora = l.codEditora;

select e.descricao as editora, l.titulo
from tb_editora e
left outer join tb_livro l on e.codEditora = l.codEditora;
# recuperar os titulos com os respectivos genêros
# os genêros se livros também devem ser exibidos
select l.titulo, g.descricao as genero
from tb_livro l
right outer join tb_genero g on l.codGenero = g.codGenero;
#recuperar soma dos preços dos livros por editora
select e.descricao as editora, sum(l.preco)
from tb_editora e
inner join tb_livro l on e.codEditora = l.codEditora
group by editora;
# quantidade de livros por editora
select codEditora, count(*)
from tb_livro
group by codEditora;
#quantidade de livros por descrição de editora
select e.descricao as editora, count(*)
from tb_editora e
inner join tb_livro l on e.codEditora = l.codEditora
group by editora
having count(*)>1
order by count(*) desc;
#quantidade de livros por descrição de gênero
select g.descricao as genero, count(*)
from tb_genero g
inner join tb_livro l on l.codGenero = g.codGenero
group by genero
order by count(*) desc;
#Retornar todos os livros com código de editora menor do que 3 utilizando subquery
select * from tb_livro where codEditora in 
	(select codEditora from tb_livro where codEditora <3);
#Listar o isbn, o título, o preço e o gênero do livro que possui o menor preço
select isbn, titulo, preco, descricao as genero
from tb_livro l
inner join tb_genero g on l.codGenero = g.codGenero
where preco = (select min(preco) from tb_livro);
# Listar o isbn e o título dos livros que custam abaixo da média de preços
select isbn, titulo, preco
from tb_livro
where preco < (select avg(preco) from tb_livro);
# Criar índice na coluna preco da tabela tb_livro
show index from tb_livro;
create index idx_preco on tb_livro(preco);
#Stored Procedure que recupera o preço a partir do código do livro
DELIMITER //
create procedure getPreco(codLivro int)
begin
	select preco
    from tb_livro
    where isbn=codLivro;
end //
DELIMITER ;

call getPreco(2);
