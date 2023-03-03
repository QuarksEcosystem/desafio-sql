import pandas as pd
import matplotlib.pyplot as plt
import sys


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



def main(trimestral_file):

    plota_grafico(trimestral_file)


    

if __name__ == '__main__':
        
    n = len(sys.argv)
        
    assert n == 2, 'Numero de argumentos invalidos'

    main(sys.argv[1])