# Projeto   

Foram utilizadas as ferramentas MySQL, Python e a IDE Spyder na realização desse projeto.

## Primeira etapa: Python

As atividades realizadas nesta primeira etapa foram primeiro a importação da base e tratamento das variáveis, para isso foi utilizada a biblioteca Pandas e o link do raw da base no github usando a função read_csv() e atentando para o separador ser o ";", em seguida visualizei base através do "variable explorer" presente no Spyder, então criei uma nova variável que representaria a variável "Valor" em formato numérico, para isso utilizei a função replace para remover os "R$" e "." em seguida substitui as "," por "." e finalmente converti para o formato "float".

O primeiro objetivo consistia em agrupar a base por vendedores, após isso realizar a soma de suas respectivas vendas e ordenar da maior para menor soma. Dessa forma, foi utilizado o groupby por vendedor, o agg junto com sort_values da soma dos valores, em seguida o arcending false para ordenar.

O segundo objetivo consistia em buscar quais os clientes com maior e menor valor de venda, para isso foi utilizado o idxmax() e idxmin() para achar a posição na tabela das linhas que apresentavam o maior e o menor valor de venda, então foram selecionados as variáveis Cliente e Valor com a função iloc[,:] para retornar apenas a linha filtrada.

O terceiro objetivo consistia em achar o valor médio para cada tipo de venda, então foi utilizado o groupby() no tipo da venda e o agg() da média dos valores. 

Finalmente, o quarto objetivo era descobrir o número de vendas por cliente, dessa forma foi utilizado o groupby() nos clientes e o agg() + sort_values() da contagem, com ascending = false para ordenar.

## Segunda Etapa: SQL

As atividades da segunda etapa foram realizadas pelo MySQL, Workbench.

O primeiro objetivo era criar um modelo de relacionamento com as variáveis da planilha, então foi utilizado o Diagram do Workbench e manualmente construindo o diagrama e suas relações. Tiveram então quatro pontos principais ao olhar para o problema: A planilha aparentava ser sobre uma emprese que prestava serviços então os 4 pilares enxergados foram: o produto, o consumidor, os funcionários e a equipe. Dessa forma, a chave primaria que relacionava todos os bancos seria o ID do contrato, pois é único para todos os produtos e através dele podemos chegar nos vendedores, nos clientes e nas equipes. As tabelas então ficaram: 

	* Cliente: que contém o cliente e o ID do contrato;
	* Equipe: que contém a equipe e o ID do contrato;
	* Vendedor: que contém o vendedor e o ID do contrato;
	* Contrato: que contém o ID, o tipo, a categoria, data da venda, duração do contrato, região e valor;

Cada contrato apresenta uma relação de um para um para cliente, vendedor e equipe, mas um cliente cliente pode apresentar vários contratos, a relação é análoga para vendedor e contrato, equipe e contrato, finalmente uma equipe podia apresentar vários vendedores.

Então para realização do segundo objetivo foi criado um schrema no workbench e a função "Table data import wizard" para leitura do csv, todas as variáveis exceto "duração do contrato" foram inicialmente lidas como string (text). O segundo objetivo foi selecionar o cliente e o id do csv e filtrar para o ano de 2020. Para isso foram utilizadas as funções select, from, where e right, pois para filtrar o ano a variável  estava como string então foram pegos os últimos quatro dígitos e igualados a 2020.

O terceiro objetivo consistia em buscar os vendedores e suas respectivas equipes, para isso foi utilizado o select, from e o group by, o group by foi utilizado nos vendedores e não nas equipes pois uma equipe poderia apresentar mais de um vendedor e essa informação seria suprimida.

O quarto objetivo foi dividido em três partes: Primeiro foi convertida a data que estava em string para o formato de data, depois buscado o trimestre associado aquela data, então do valor que estava no formato de string, foram removidos os "R$" e os pontos, trocadas as virgulas por pontos, finalmente convertido para numérico e feito o somatório então foi filtrado para cada ano para conseguir agregar por trimestre, criando assim 4 tabelas. As funções utilizadas para isso foram Select, year(retorna o ano), srt_to_date(converter para data), quarter(agrupar em trimestre), sum, cast e as decimal( juntas para converter para numérico), replace, where e group by. Então as quatro tabelas foram exportadas e importadas através do "Table data import wizard",  então agregadas em uma única tabela com o union. Então com essa tabela voltamos ao python para plotar o gráfico do valor de vendas por trimestre.

Então foi lido o arquivo csv que foi salvo no diretório utilizando a mesma função, mas dessa vez o separador foi ",". Então as variáveis ano e trimestre foram agregadas em uma que foi categorizada.  Então foi construído um gráfico de linha para visualizar a mudança nos totais através dos trimestres. Foi utilizado para isso a biblioteca matplotlib, com as funções plot para a construção da linha, xticks e yscale para melhor visualização das informações dos eixos, title, xlabel e ylabel para as etiquetas e titulo. 