# Como executar

Para executar os notebooks do projeto é necessário:
- Realizar o download desse repositório;
- Ter instalado na máquina Python e as bilbiotecas pandas, numpy e sqlite3;
- Ter uma IDE na sua máquina (recomendo VS Code por ser muito bom).

Tendo seguido os passos acima é só abrir a pasta do repositório e clicar nos notebooks disponíveis (desafio_python e desafio_sql) que a IDE automaticamente vai abrir o notebook selecionado.

# Projeto:
## desafio_python
Nesse primeiro desafio foi dividido em 4 partes.
Na primeira parte foi pedido para que fosse construido uma tabela que sumarizasse o valor vendido por cada vendedor, ordenado do maior para o menor.
Para resolver esse problema importei as bibliotecas necessárias para a resolução do problema (pandas e numpy).
Em seguida importei os dados que estavam em formato csv com a biblioteca pandas usando a função read_csv() e salvei esses dados na variavel dados para que depois eu pudesse manipula-los.
Utilizei a função head() para olhar os primeiros 5 registros do DataFrame para ter uma ideia de como eram os dados do arquivo csv e, após isso usei a função info() para ver se haviam dados faltantes e, também, os tipos de dados de cada coluna.
Verifiquei que para manipular os valores da coluna "Valor" era necessário fazer algumas alterações, pois não estava com o tipo de dado correto e ainda possuiam letras e símbolos. Fiz as alterações necessárias tirando os símbolos "R$" dos valores e alterando o "." por um espaço vazio e a "," por ".".
Criei uma função para que depois que eu manipulasse os dados da coluna "Valor" eu retornasse elas para o formato de moeda.
Para criar a tabela que sumarizasse o valor vendido por cada vendedor eu utilizei a função groupby() para agrupar os dados por "Vendedor" realizando a soma de cada venda feita por vendedor junto com a função sort_values() para ordenar em ordem do maior valor para o menor, em seguida já realizo a transformação dos valores para moeda e imprimo a tabela.

Na segunda parte foi para que imprimisse e indentificasse qual cliente foi responsável pela venda com maior valor e menor valor.
Para resolver esse problema eu identifiquei qual foi o maior valor e o menor valor. Após isso realizei uma filtragem com esses dois valores para que fosse retornado as linhas que batiam com nosso critério (maior valor e menor valor).
Com as linhas retornadas imprimi qual era o cliente e o valor da venda.

Na terceira parte o objetivo era imprimir valor médio por tipo de venda. 
Para resolver eu utilizei a função groupby() para agrupar os dados pela coluna "Tipo" realizando a média dos valores das vendas. Logo depois foi feito a transformação dos valores para moeda e em seguida imprimo o Tipo e o Valor Médio.

Na quarta parte o desafio era imprimir o número de vendas realizadas por cliente.
Utilizei a função groupby() pra agrupar os dados por cliente e realizar a contagem de quantas vezes a coluna "ID" aparecia por cliente, ou seja, se para o cliente 1 apareceu 4 ocorrências do coluna "ID" então ele realizou 4 vendas.
E para finalizar imprimi os nomes dos Clientes com o número de vendas.

## desafio_sql
No desafio de SQL antes de começar ele tive que pegar o arquivo csv e transforma-lo em um arquivo .db (em banco de dados). Para fazer isso utilizei o SQLite.
Após realizada a transformação criei um notebook em python para poder manipular esse banco de dados.
Primeiramente tive que importar as bibliotecas pandas, numpy e sqlite3. Após importar eua bro uma conexão com o banco de dados e crio um cursor para poder manipular o banco de dados.
Esse segundo desafio foi separado em 3 partes.

Na primeira parte o objetivo era listar todas as vendas (ID) e seus respectivos clientes apenas no ano de 2020. Para sulocionar o desafio utilizei uma query no qual selecionava apenas as colunas ID e Cliente do banco de dados DB_Teste onde a DatadaVenda apenas possuísse o ano de 2020. Com o resultado da query eu crio uma DataFrame para poder visualizar os dados retornados pela query.

Na segunda parte foi pedido para listar a equipe de cada vendedor. Para realizar a consulta foi utilizado uma query que seleciona as colunas ID e Cliente do banco de dados DB_Teste e agrupo eles por Vendedor. Logo em seguida salvo os valores retornados da query em um DataFrame para poder visualiza-los.

Na última parte o desafio era construir uma tabela que avalia trimestralmente o resultado das vendas e um gráfico desse histórico. Para resolver esse desafio criei uma query no qual eu utilizava a coluna DatadaVenda e fazia transformações nela para poder retirar dela o ano e o mes de cada venda para em seguida criar uma coluna trimestre no qual identificava qual mes fazia parte de cada trimestre e, tambem, tive que realizar transformações na coluna Valor para poder manipular os valores. Ao final agrupo os dados Ano e Trimestre e salvo os dados retornados pela query em um DataFrame.
Com o Dataframe eu ploto um gráfico de linhas para mostrar como foi o histórico das vendas por ano/trimestre.