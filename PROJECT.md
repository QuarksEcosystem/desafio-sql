# Como executar

O projeto foi implementado pelo Google Colaboratoty ou Colab, para acessar o Colab é necessário ter uma conta do Google.

Para executar os notebooks do projeto:
- Fazer download do repositório;
- Uma conta no Google para utilizar o Google Colab;
- Ou ter instalado na máquina Python, as bibliotecas pandas, numpy e squlite3 e uma IDE na máquina(como VS Code)

# Projeto:

## Desafio em Python

Para iniciar o desafio, importei as bibliotecas pandas e numpy, fiz upload dos dados "DB_Teste.csv" e utilizei a função
read_csv() e salvei os dados na varíavel db para manipulá-los. Utilizei a função info() para visualizar as informações
e os tipos dos dados. Verifiquei que existia uma coluna chamada "Unnamed: 10" com somente valores nulos, então utilizei
a função drop() para retirá-la e percebi que a coluna "Valor" não estava no tipo de dado correto para utilizá-los e continha
letras e símbolos. Comecei removendo da coluna "Valor" os símbolos "R$", susbtituí os "." por espaço vazio e as "," por ".".
Em seguida renomeei as colunas "Data da Venda" e "Duração do Contrato (Meses)" por, respectivamente, "Data_da_Venda" e 
"Duracao_do_Contrato_Meses", percebi que essas alterações poderiam ser importantes para poder manipular da melhor forma os
dados. E criei uma função chamada "transforma_moeda" para retornar os valores da coluna "Valor" em formato de moeda.

Nesse primeiro desafio era proposto 4 tarefas. A primeira tarefa era criar uma tabela para sumarizar o valor vendido por cada
vendedor, ordenando do maior para o menor. Para essa tarefa criei uma tabela chamada "tab_auxiliar" e utilizei a função 
groupby() para agrupar os dados da coluna "Vendedor" e realizando a soma de cada venda realizada por vendedor, utilizei a 
função sort_values() para ordenar do maior valor para o menor e em seguida transformo os dados de "Valor" para formato de
moeda e imprimo a tabela.

A segunda tarefa era para imprimir e identifar qual foi o cliente responsável pela venda com maior valor e com menor valor.
Para essa tarefa criei uma tabela chamada "tab_venda" e utilizei a função groupby() para agrupar a coluna "Cliente" e a função
agg() para retornar a soma do "Valor", em seguida ordenei com sort_values() e apliquei a função "transforma_moeda" para
padronizar o "Valor". Depois fiz um print() para retornar o responsável pela venda com maior valor e de menor valor.

A terceira tarefa era para imprimir o valor médio por tipo de venda, criei uma tabela chamada "tab_medio_tipo", utilizei o
groupby() para agrupar o "Tipo" e agg() para retornar a média do "Valor". Utilizei o sort_values() para ordenar, apliquei
a função "transforma_dados" para padronizar o "Valor" e fiz um print() para imprimir o "Tipo" e o valor médio.

A quarta e última tarefa do desafio em python era imprimir o número de vendas realizada por cliente, comecei criando uma
tabela chamada "tab_n_vendas_cliente" e usei o groupby() para agrupar "Cliente" e a função count() no "ID" para realizar 
a contagem de quantas vezes a coluna "ID" aparecia por cliente, consequente a quantidade de vendas. Usei o sort_values()
para ordenar a quantidade de aparecimentos do menor para o maior e renomeei a coluna "ID" para "Numero_de_Vendas", em
seguida imprimi os clientes e o número de vendas para cada cliente.

## Desafio em SQL

Para iniciar esse desafio eu fiz uma cópia da "DB_Teste.csv" já com as alterações realizada no desafio anterior e nomeei
de "DB_Teste_atualizada", e fiz upload no Google Colab no "desafio_sql". Logo em seguida importei o sqlite3, pandas e numpy.
Utilizei a função read_csv(), salvei os dados na varíavel db e fiz um drop() para retirar a coluna "index" que veio na
"DB_Teste_atualizada". Em seguida fiz "db.columns.str.strip()" para remover possíveis espaços em branco. Para criar o banco
de dados tive que fazer um processo para transformar os dados em .csv para .db, nesse processo criei uma variável chamada
"connection" e utilizei a função sqlite3.connect() para criar e conectar a um banco de dados, o qual nomeei de "DB_Teste.db".
Em seguida usei a função to_sql() para gravar os dados armazenados em "DB_Teste_atualizada.csv" no "DB_Teste.bd", por fim
utilizo a função close() para fechar o arquivo "DB_Teste.db". Após isso eu abro uma conexão com o banco de dados criado e
crio um cursor para manipular o banco de dados.

Nesse desafio tinham 4 tarefas, a primeira seria para criar um modelo de relacionamento utilizando as categorias do arquivo
.csv, o qual está no repositório como "Modelo_de_Relacionamento.png".

Continuando a segunda tarefa era listar todas as vendas(ID) e seus respectivos clientes apenas no ano de 2020. Para realizar
a tarefa fiz uma query para selecionar as colunas "ID", "Cliente" e "Data_da_Venda" do banco de dados "DB_Teste", onde
a "Data_da_Venda" fosse de 2020. E crio um DataFrame chamado "vendasID_cliente" para visualizar a query retornada.

A terceira tarefa foi para listar a equipe de cada vendedor, então realizei uma query para selecionar apenas as linhas
distintas das colunas "Equipe" e "Vendedor" do banco de dados "DB_Teste" e agrupar por "Vendedor". Então crio o DataFrame
"equipe_vendedor" e retorno para visualizar a consulta onde lista a equipe de cada vendedor.

A última tarefa era para construir uma tabela que avalia trimestralmente o resultado de vendas e plotar um gráfico do
histórico. Para esta tarefa criei uma query que utiliza a coluna "Data_da_Venda" e faz transformações nela para retirar o
ano e o mês de cada venda para criar uma coluna "Trimestre", a qual identifica qual mês faz parte de cada trimestre. Por
fim crio um DataFrame "tab_venda_trimestral" com a query retornada. E com a "tab_venda_trimestral" ploto um gráfico de
linhas para visualizar o histórico de vendas por ano/trimestre.
