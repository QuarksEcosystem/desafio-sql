O csv_reader é responsável por ler .csv que tenham o mesmo formato do "DB_Teste.csv"
e realizar as tarefas especificadas no desafio.
Para executar o csv_reader usando o arquivo .csv fornecido basta abrir a pasta no prompt de comando e executar 
python3 csv_reader.py "DB_Teste.csv"

Queries pedidas:

1)Listar todas as vendas (ID) e seus respectivos clientes apenas no ano de 2020:

SELECT * FROM public."Vendas"
WHERE data BETWEEN '2020-01-01' AND '2020-12-31';

2)Listar a equipe de cada vendedor:

SELECT * FROM public."Vendedores"
ORDER BY vendedor_id ASC 

como todos os vendedores tem um campo "Equipe", basta dar SELECT em todos vendedores

3)Construir uma tabela que avalia trimestralmente o resultado de vendas:

SELECT
  date_part('year', data) AS Ano,
  date_part('quarter', data) AS Trimestre,
  SUM(valor) AS TotalSales
FROM
  public."Vendas"
WHERE
  data > '2017-01-01'
GROUP BY
  date_part('year', data), date_part('quarter', data)
ORDER BY Ano ASC

A tabela foi exportada para o arquivo output.csv utilizando o seguinte comando na ferramente PSQL, para a criação do gráfico:
-c \copy (SELECT date_part('year', data) AS Ano, date_part('quarter', data) AS Trimestre, SUM(valor) AS TotalSales FROM public."Vendas" WHERE data > '2017-01-01' GROUP BY date_part('year', data), date_part('quarter', data)ORDER BY Ano ASC) To 'D:\git\desafio-sql\output.csv' DELIMITER ';' CSV  HEADER

O gráfico resultando foi o output.png


