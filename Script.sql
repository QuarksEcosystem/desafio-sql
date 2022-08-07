-- Aqui foram selecionadas as variáveis Clinte e Id do contrato, depois filtrado para os que eram do ano de 2020, --
-- como inicialmente não sabia converter de string para data, peguei os quatro ultimos digitos da string que correspondiam --
-- ao ano --
SELECT ﻿Cliente, ID
FROM `csv_db 7`.`db_teste.csv`
WHERE RIGHT(`Data da Venda`,4) = 2020;

-- Aqui foram selecionadas as variáveis vendedor e equipe, foram agrupadas por vendedor por cada vendedor apresentar uma equipe --
-- Mas uma equipe poderia apresentar mais de um vendedor e a informação do segundo seria suprimida no group by --
SELECT Vendedor, Equipe
FROM `csv_db 7`.`db_teste.csv`
group by Vendedor ;

-- Aqui primeiro converti a data que estava em string para o formato de data, depois busquei o trimestre assossiado aquela data, então--
-- o valor que estava no formato de string removi o "R$" e os pontos, troquei as virgulas por pontos, converti para numerico e fiz o somatorio--
-- então finalmente filtrei para cada ano para conseguir agregar por trimestre, criando assim 4 tabelas --
SELECT year(STR_TO_DATE(`Data da Venda`,"%d/%m/%Y")), Quarter(STR_TO_DATE(`Data da Venda`,"%d/%m/%Y")), sum(cast(Replace(Replace(REPLACE(Valor, "R$ ", ""), ".", ""), ",", ".") as decimal(10,2)))
FROM `csv_db 7`.`db_teste.csv`
where year(STR_TO_DATE(`Data da Venda`,"%d/%m/%Y")) = '2018'
group by (Quarter(STR_TO_DATE(`Data da Venda`,"%d/%m/%Y")));


SELECT year(STR_TO_DATE(`Data da Venda`,"%d/%m/%Y")), Quarter(STR_TO_DATE(`Data da Venda`,"%d/%m/%Y")), sum(cast(Replace(Replace(REPLACE(Valor, "R$ ", ""), ".", ""), ",", ".") as decimal(10,2)))
FROM `csv_db 7`.`db_teste.csv`
where year(STR_TO_DATE(`Data da Venda`,"%d/%m/%Y")) = '2019'
group by (Quarter(STR_TO_DATE(`Data da Venda`,"%d/%m/%Y")));


SELECT year(STR_TO_DATE(`Data da Venda`,"%d/%m/%Y")), Quarter(STR_TO_DATE(`Data da Venda`,"%d/%m/%Y")), sum(cast(Replace(Replace(REPLACE(Valor, "R$ ", ""), ".", ""), ",", ".") as decimal(10,2)))
FROM `csv_db 7`.`db_teste.csv`
where year(STR_TO_DATE(`Data da Venda`,"%d/%m/%Y")) = '2020'
group by (Quarter(STR_TO_DATE(`Data da Venda`,"%d/%m/%Y")));


SELECT year(STR_TO_DATE(`Data da Venda`,"%d/%m/%Y")), Quarter(STR_TO_DATE(`Data da Venda`,"%d/%m/%Y")), sum(cast(Replace(Replace(REPLACE(Valor, "R$ ", ""), ".", ""), ",", ".") as decimal(10,2)))
FROM `csv_db 7`.`db_teste.csv`
where year(STR_TO_DATE(`Data da Venda`,"%d/%m/%Y")) = '2021'
group by (Quarter(STR_TO_DATE(`Data da Venda`,"%d/%m/%Y")));

-- Finalmente, juntei as 4 tabelas em uma única tabela final que será utilizada no python para plotar o gráfico --
SELECT ano, trimestre, vendas
FROM tabela1
UNION
SELECT ano, trimestre, vendas
FROM tabela2
UNION
SELECT ano, trimestre, vendas
FROM tabela3
UNION
SELECT ano, trimestre, vendas
FROM tabela4