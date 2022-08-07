# Primeiramente iremos importar a base de dados, em seguida notamos que a variável valor está no formato de 
# string e para realizar as operações como somatório e média devemos converte-la para numérico.
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/QuarksEcosystem/desafio-sql/main/DB_Teste.csv', sep = ';')
df['newValor']=df['Valor'].replace("R\$|\.","",regex = True)
df['newValor']=df['newValor'].replace(",",".",regex = True)
df['newValor'] = df['newValor'].astype(float)

# Então agrupamos a base por vendedores, fazemos a soma dos valores de cada vendedor e ordenamos.
df.groupby('Vendedor')['newValor'].agg(['sum']).sort_values(by=['sum'],
                                                                  ascending = False)
# Aqui buscamos o máximo e mínimo dos valores e após achar as linhas correspondentes bucamos qual o 
# cliente delas. 
i = df['newValor'].idxmax()
j = df['newValor'].idxmin()
df[['Cliente', 'newValor']].iloc[i,:].newValor
print(f""" O {df.iloc[i].Cliente} foi o que apresendou o maior valor,
      de {df.iloc[i].newValor} reais.""")
     
print(f""" O {df.iloc[j].Cliente} foi o que apresendou o menor valor,
      de {df.iloc[j].newValor} reais.""")
      
# Aqui agrupamos os valores por tipo de venda e pegamos as médias dos valores por tipos de venda.    
df.groupby('Tipo')['newValor'].agg(['mean'])

# Finalmente, agrupamos a base pelos clientes, realizamos a contagem desses clientes para saber o
# número de vendas e ordenamos.
df.groupby('Cliente')['Cliente'].agg(['count']).sort_values(by=['count'],
                                                            ascending = False)
                              
#Construção do gráfico do resultados de venda trimestralmente proveniente do tratamento do banco no sql
df2 = pd.read_csv('TabelaJunta.csv', sep = ',')
df2['anotrimestre']= df2['ano'].map(str) + '.' + df2['trimestre'].map(str)
df2['anotrimestre'] = df2['anotrimestre'].astype('str')
#Foi criado uma nova coluna juntando ano e semestre, então foi feito um gráfico de linha devido a dependencia temporal 
#dos dados.

import matplotlib.pyplot as plt
plt.plot(df2['anotrimestre'], df2['vendas'])
plt.xticks(rotation=45)
plt.yscale('log')
plt.title('Resultado de vendas por trimestre de 2018 até 2021')
plt.xlabel('Trimestres')
plt.ylabel('Valor total de vendas (R$)')
plt.show()