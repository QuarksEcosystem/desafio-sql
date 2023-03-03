from IPython.display import display
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

def trata_bd(BD_file):
    # Carregando o arquivo
    dados = pd.read_csv(BD_file, sep = ';', index_col = False)
    dados = dados.drop(dados.columns[[10]], axis = 'columns')

    # convertendo o valor para float
    dados['Valor'] = dados['Valor'].str.replace(' ', '', regex=True).str.replace(r'R\$', '', regex=True).str.replace('.', '', regex=True).str.replace(',', '.', regex=True).astype(float)

    # agrupando os dados por vendedor e somando os valores
    tabela = dados.groupby('Vendedor').agg({'Valor':'sum'})

    # ordenando do maior para o menor
    tabela_ordenada = tabela.sort_values(by='Valor', ascending=False)


    print(">>>>>>> SOMA DAS VENDAS POR VENDEDOR <<<<<<<\n\n",tabela_ordenada)

    maior_venda = dados[dados['Valor'] == dados['Valor'].max()]['Cliente']
    print("\nO cliente com maior venda é o {} cujo valor foi {}".format(maior_venda.values[0], dados['Valor'].max()))

    menor_venda = dados[dados['Valor'] == dados['Valor'].min()]['Cliente']
    print("\nO cliente com menor venda é o {} cujo valor foi {}\n".format(menor_venda.values[0], dados['Valor'].min()))

    tipos = dados.groupby('Tipo').Valor.mean().reset_index()
    print(">>>>>>> MEDIA DOS VALORES VENDIDOS POR CATEGORIA <<<<<<<\n",tipos)

    vendas = dados.groupby('Cliente')['ID'].count().reset_index(name='Numero de Vendas')
    vendas_ordenadas = vendas.sort_values(by='Numero de Vendas', ascending=False).set_index('Cliente')
    display("\n",vendas_ordenadas.to_string())

    display(dados.to_string())


    #transformando a coluna de data do formato (dia/mes/ano) para (ano-mes-dia) -> motivo disso é facilitar a importacao para as tabelas do mysql
    dados['Data da Venda'] = pd.to_datetime(dados['Data da Venda'], format = '%d/%m/%Y').dt.strftime('%Y-%m-%d')

    #transformando o id do formato(xxxx-yyyy) para (xxxxyyyy)
    dados['ID'] = dados['ID'].str.replace('-', '', regex=True)

    dados.to_csv('DB_novo.csv', sep =';', index = False)



def plota_grafico(trimestral_file):
    df = pd.read_csv(trimestral_file, delimiter=';')

    # Configurar o tamanho do gráfico
    plt.figure(figsize=(10, 5))

    # Criar um gráfico de barras com os valores totais de cada trimestre
    plt.bar(df['Trimestre'], df['Valor_Total'])

    # Adicionar rótulos para o eixo x e y
    plt.xlabel('Trimestre')
    plt.ylabel('Valor Total')

    # Alterar a orientação do eixo x para que os nomes fiquem na vertical
    plt.xticks(rotation=90)

    # Exibir o gráfico
    plt.show()



def main(BD_file,trimestral_file):
    trata_bd(BD_file)
    plota_grafico(trimestral_file)


    

if __name__ == '__main__':
        
    n = len(sys.argv)
        
    assert n == 3, 'Numero de argumentos invalidos'

    main(sys.argv[1],sys.argv[2])