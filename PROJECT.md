
Desafio Python:
Utilização: 
	O programa foi criado utilizando a IDE Vscode, mas deve ser compatível com qualquer ambiente. Ao iniciá-lo, o programa exibe um menu instando o usuário a escolher as funções que deseja executar. São aceitas letras maiúsculas ou minúsculas. O arquivo csv utilizado é o mesmo fornecido, com apenas uma diferença no nome, e encontra-se anexado à mesma pasta do desafio.

Parte 1:

Enunciado: Construa uma tabela auxiliar que sumarize o valor vendido por cada vendedor, ordenando do maior para o menor.

Resposta:
	Observação: para o funcionamento desta função, é necessário importar as bibliotecas csv, pandas e decimal. O csvfile utilizado se encontrava no mesmo diretório que o programa, e se chamava ‘BD_Teste.csv’, e se encontra anexo a este respositório.

	Primeiramente, foi necessário alterar o .csv fornecido, trocando seu delimitador “,” para “;”, pois em seu estado bruto, os valores em reais eram separados dos centavos, o que criaria resultados diferentes dos buscados.
	Com os ajustes feitos, parti para a criação da função vendedoresTotal(csvfile):

![alt text]([[https://imgur.com/K5A3gtY](https://github.com/bcatao92/desafio-sql/blob/main/imagem1.jpg)](https://github.com/bcatao92/desafio-sql/blob/main/imagem1.jpg?raw=true))

	A função cria um reader para o arquivo csv e um dicionário, pula a linha do cabeçalho e itera pelo arquivo salvando vendedores como chaves e calculando o total de suas vendas. Para somar os valores, foi necessário criar uma função que transformasse os valores de string para decimal, conforme vemos a seguir:

![alt text](https://imgur.com/8UIVTMa)

	Com o dicionário garantindo que os vendedores tinham suas respectivas somas, faltava ordená-los de acordo como os valores, o que não é possível num dicionário. Para isso criei o sort_dicio, uma lista de tuplas ordenada do maior valor para o menor, e uma lista vazia chamada valores, que receberia os valores tratados novamente como string, para que eu pudesse formatar-los novamente como dinheiro:

![alt text](https://imgur.com/riq2vra)

	Por fim, para gerar a tabela, foi necessário criar um DataFrame que recebesse os valores e os títulos da tabela, segundo a fórmula a seguir:

![alt text](https://imgur.com/v3wiHx3)

Parte 2:
Enunciado: Imprima e identifica qual foi o cliente responsável pela venda com maior valor e com menor valor;

	Resposta:
	
  A função maiorMenor(csvfile) foi utilizada para responder a esta demanda.
  
  ![alt text](https://imgur.com/w5fiSdS)
  
	Como as outras, ela cria um leitor de csv e pula a primeira linha do arquivo fornecido. Ela então itera pelo arquivo (deletando a última coluna, criada por um erro de leitura no csv original) e adiciona os clientes e suas respectivas compras numa lista que é organizada do maior para o menor.
	A função então imprime uma mensagem dizendo qual cliente fez a maior compra singular e seu valor, e qual fez a menor compra e seu valor.

Parte 3:
	Enunciado: Imprima valor médio por Tipo de venda (Serviços, Licenciamento, Produtos)

	Resposta:

	Para esta demanda, achei importante importar a biblioteca collections.
  
  ![alt text](https://imgur.com/tzxV7aL)

	A função mediasTipos(csvfile) cria o dicionário tipos, um collections.Counter chamado contaTipo e uma lista chamada medias. A função então itera pelo arquivo csv contando as ocorrências de cada tipo e armazenando em contaTipo, além de guardar os tipos de serviços e somar suas respectivas arrecadações no dicionário tipos.
	A seguir, contaTipo e tipos são organizados alfabeticamente, de modo que as posições dos tipos sejam correspondentes nas duas listas.
	Por fim, utilizei um for loop para calcular as médias, dividindo os valores totais pelas ocorrências dos tipos e armazenando-as justo aos seus respectivos tipos na lista medias criada anteriormente. Esta lista então é usada para criar o DataFrame que é impresso como resultado da função.

Parte 4:
Enunciado: Imprima o número de vendas realizada por cliente;
Resposta:
	A biblioteca collections foi usada novamente nesta função.
	Para contar quantas vezes um cliente específico fez compras com a empresa, foi criado um Counter, que foi alimentado na iteração do csv_reader, retornando uma lista com cada cliente e sua frequência. A lista, contaCliente.most_common(), foi utilizada como fonte para o DataFrame, que tinha como colunas “Cliente” e “Vendas”.
 ![alt text](https://imgur.com/fq3gCGZ)


Desafio SQL

O database manager utilizado foi o PostgreSQL, por questão de familiaridade.

Parte 1: 
Enunciado: Construa o modelo de relacionamento com as categorias utilizadas em todos os campos do arquivo CSV (colocar imagem);

Criando o modelo de relacionamento com o arquivo CSV fornecido. Note que para que a coluna “Valor” não seja separada em duas, foi necessário trocar os delimitadores de “,” para “;” no arquivo original.
A seguir, imagem com a Query utilizada e relação criada:

![alt text](https://imgur.com/GTdIoAF)

Parte 2:
Enunciado: Listar todas as vendas (ID) e seus respectivos clientes apenas no ano de 2020


Query:

![alt text](https://imgur.com/Pw26Ema)

![alt text](https://imgur.com/FEXVr7j)

Parte 3:
Enunciado: Listar a equipe de cada vendedor

Query:
![alt text](https://imgur.com/xXqYmi6)
![alt text](https://imgur.com/xPcvAZj)

Parte 4:
- Construir uma tabela que avalia trimestralmente o resultado de vendas e plote um gráfico deste histórico.

Tabela:

![alt text](https://imgur.com/IgIqMxw)

Para plotar o gráfico, foi necessário converter os valores da receita para Numeric, de outra forma o PostgresSQL não leria a coluna “Receita” como número.

![alt text](https://imgur.com/M7DBJwW)
