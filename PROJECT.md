# Índice
 * [Descrição da Resolução](#descrição-do-Desafio)
 * [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
 * [Tecnologias utilizadas, Versões e Sistema Operacional](#Tecnologias-utilizadas,-Versões-e-Sistema-Operacional)
 * [Como Executar o Projeto](#Como-Executar-o-Projeto)
 * [Desenvolvedor do Desafio](#Desenvolvedor-do-Desafio)

# Descrição da Resolução

Para resolver o desafio foram utilizadas as seguintes bibliotecas da linguagem python: Pandas, MatPlotLib, NumPy, Sys e IPython. Para melhor detalhar o que fiz, optei por fazer um Jupyter Notebook pois nele é possível executar códigos em Python, adicionar textos explicativos e fotos. Mas de antemão os passos que eu segui para foram:
-  `Passo 1`: Abri o arquivo csv utilizando a biblioteca pandas.
- `Passo 2`: Apaguei a última coluna do arquivo pois não haviam dados nela.
-  `Passo 3`: Modifiquei os dados da coluna valor, para que o formato dos dados fiquem como float.
- `Passo 4`: Com o DataFrame já modificado, utilizei das funcionalidades da biblioteca Pandas, Numpy e IPhython para resolver as questões propostas na primeira parte.
- `Passo 5`: Transformei a coluna de data do formato (dia/mês/ano) para (ano-mês-dia), para facilitar a importação dos dados para as tabelas do mysql.
-  `Passo 6`: Transformei o id do formato (xxxx-yyyy) para (xxxxyyyy), tirei o hífen pois tive problemas ao importar os dados para a base de dados.
- `Passo 7`: Com o as modificações feitas, gerei um novo arquivo .csv que foi o utilizado para preencher o banco de dados criado no mysql.
- `Passo 8`: Com o .csv atualizado em mãos, gerei o Modelo Relacional de Entidades utilizando o site draw.io.
- `Passo 9`: Com Modelo Relacional de Entidades em mão criei a base de dados e as tabelas com as queries que são mostradas no Notebook Jupyter.
- `Passo 10`: Com base de dados e tabelas criadas, prenchi as tabelas com o arquivo .csv que gerei no paso 7.
- `Passo 11`: Após preencher a base se dados utilizei as queries que estão demonstradas no Notebook Jupyter para realizar as consultar pedidas.
- `Passo 12`: A ultima query gera um arquivo .csv, utilizei ele para plotar o gráfico pedido utilizando a biblioteca MatLabLib na linguagem Python.

# Funcionalidades e Demonstração da Aplicação

A demostração e códigos utilizados estão todos no arquivo  **Desafio_SQL.ipynb**.

## Tecnologias utilizadas, Versões e Sistema Operacional

Para este desafio utilizei da linguagem de programação **Python** versão **3.10.6**, **GCC** versão **11.3.0**. Utilizei como banco de dados o **MySQL** versão **8.0.32** e por último meu sistema operacional: **Linux Ubuntu** versão **22.04.2**









# Como Executar o Projeto
Para executar o projeto é necessário ter os arquivos  **[solucao.py](https://github.com/luanacarlos/desafio-sql/blob/main/solucao.py "solucao.py")**, **[DB_Teste.csv](https://github.com/luanacarlos/desafio-sql/blob/main/DB_Teste.csv "DB_Teste.csv")**, **[DB_Avaliaçao_Trimestral.csv](https://github.com/luanacarlos/desafio-sql/blob/main/DB_Avalia%C3%A7ao_Trimestral.csv "DB_Avaliaçao_Trimestral.csv")** salvos em mesma pasta.
-  `Passo 1`: Abrir um terminal Linux ou Windows
- `Passo 2`: Acessar a pasta onde os arquivos se encontram
- `Passo 3`: Digitar o comando "python3 solucao.py DB_Teste.csv DB_Avaliaçao_Trimestral.cs" e pressionar ENTER.


## EXTRA

É possível executar o programa de uma só vez pois eu deixei os bancos de dados processados de acordo como é mostrado em **[Desafio_SQL.ipynb](https://github.com/luanacarlos/desafio-sql/blob/main/Desafio_SQL.ipynb "Desafio_SQL.ipynb")**. Caso deseje utilizar outra base de dados é possível! Basta ter salvo em mesma pasta os arquivos **[parte1.py](https://github.com/luanacarlos/desafio-sql/blob/main/parte1.py "parte1.py")**, **[parte2.py](https://github.com/luanacarlos/desafio-sql/blob/main/parte2.py "parte2.py")** e **o banco de dado que você deseja usar**.
-  `Passo 1`: Abrir um terminal Linux ou Windows
- `Passo 2`: Acessar a pasta onde os arquivos se encontram
- `Passo 3`: Digitar o comando "python3 parte1.py banco_desejado.csv" e pressionar ENTER.
- `Passo 4`:Após isso o programa irá gerar um arquivo chamado BD_novo.csv, com esse arquivo basta preencher as tabelas geradas e mostradas em **[Desafio_SQL.ipynb](https://github.com/luanacarlos/desafio-sql/blob/main/Desafio_SQL.ipynb "Desafio_SQL.ipynb")**,  a última query resultará no banco de dados **BD_Avaliaçao_Trimestral.csv**, basta salvar na mesma pasta que os arquivos anteriormente citados.
- `Passo 5`:Abrir um terminal Linux ou Windows
- `Passo 6`: Acessar a pasta onde os arquivos se encontram
- `Passo 7`: Digitar o comando "python3 parte2.py BD_Avaliaçao_Trimestral.csv" e pressionar ENTER.



#  Desenvolvedor do Desafio


 | [<img src="https://imgur.com/a/Qk45Kl5" width=96><br><sub>Luan Carlos Cunha Loureiro de Alencar</sub>](https://github.com/luanacarlos) | 
  | :---: | 
