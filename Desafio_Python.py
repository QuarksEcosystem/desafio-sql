import csv
import pandas as pd
import decimal
import collections
##################Transforma os valores monetários de string em decimal para calcular receita
def stringToDec(linha):
        aux = linha.replace(".","").replace(",",".")
        aux = decimal.Decimal(aux)
        return aux
##################Transforma decimais em strings
def decToString(linha):
      aux = str(linha)
      aux = aux.replace(".",",")
      aux = "R$ " + aux
      linha = aux
      return linha
###############Cria o datafram a partir dos dados
def criaDataFrame(fonte,titulo1,titulo2):
    df = pd.DataFrame(
    data = fonte,
    columns = [titulo1, titulo2])
    return df

def auxiliarDicio(dicio):
    for line in csv_reader:
            del(line[-1])
            if dicio.get(line[5]) != None:
                dicio[line[5]] = dicio[line[5]] + stringToDec(line[-1][4:])
            else:
                dicio[line[5]] = stringToDec(line[-1][4:])

def clienteVendas(csvfile):
    with open(csvfile, 'r') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=";")    
        
        next(csv_file)
        contaCliente = collections.Counter()
        for line in csv_reader:
             contaCliente[line[0]] += 1 #######Conta clientes distintos e suas aparições
        #########Cria tabela com cliente e quantas vezes ele compra da empresa
        print(criaDataFrame(contaCliente.most_common(),"Cliente", "Vendas"))
        print("")
        csv_file.close()

def vendedoresTotal(csvfile):
    with open(csvfile, 'r') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=";")    
        dicio = dict()
        next(csv_file)
        for line in csv_reader:
            del(line[-1])
            if dicio.get(line[5]) != None:
                dicio[line[5]] = dicio[line[5]] + stringToDec(line[-1][4:])
            else:
                dicio[line[5]] = stringToDec(line[-1][4:])
        sort_dicio = sorted(dicio.items(), key=lambda x: x[1], reverse=True)
        valores = []
        for item in sort_dicio:
            valores.append([item[0],decToString(item[1])])
        print("")
        print(criaDataFrame(valores,"Vendedor","Total"))
        print("")
        csv_file.close()

def maiorMenor(csvfile):
    with open(csvfile, 'r') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=";")    
        clientes = list()
        next(csv_file)
        for line in csv_reader:
            del(line[-1])
            clientes.append([line[0],stringToDec(line[-1][4:])])
###############Pega os valores pra contar as vendas
    ordem = sorted(clientes, key = lambda x: x[1])
    print("O cliente responsável pela venda de maior valor foi o ",ordem[-1][0],", que pagou",decToString(ordem[-1][1]),".","\nO cliente responsável pela venda de menor valor foi o ", ordem[0][0], ", que pagou", decToString(ordem[0][-1]))
    print("")
    csv_file.close()
    
def mediasTipos(csvfile):
    with open(csvfile, 'r') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=";")
        tipos = dict()
        contaTipo = collections.Counter() #lista os diferentes tipos
        medias = list()
        next(csv_file)
        for line in csv_reader:
            del(line[-1])
            contaTipo[line[2]] += 1 #conta os tipos

               #########Soma os valores arrecadados por cada tipo num dicionário
            if tipos.get(line[2]) != None:
                tipos[line[2]] = tipos[line[2]] + stringToDec(line[-1][4:])
            else:
                tipos[line[2]] = stringToDec(line[-1][4:])

    auxConta = sorted(contaTipo.most_common()) #####Recebe os tipos e suas ocorrências organizados alfabeticamente
    auxValores = sorted(tipos.items())         #####Recebe os tipos e suas arrecadações
    
    ###########Calcula as médias
    for i in range(len(auxConta)):
         medias.append([auxConta[i][0], decToString(round(auxValores[i][1]/auxConta[i][1],2))])   
      
    print("\n",criaDataFrame(medias,"Tipo","Média"),"\n") 
    csv_file.close()        

x = ""
while input not in ['A','a','B','b','C','c','D','d']:
    x = input("Para visualizar, digite:\nA - Tabela das vendas totais por vendedor\nB - Ver os clientes que fizeram a maior e a menor compra\nC - Média de vendas por tipos\nD - O número de vendas por clientes\nQualquer outra tecla - Sair \n")
    match x:
        case 'A': vendedoresTotal('DB_Teste.csv')
        case 'a': vendedoresTotal('DB_Teste.csv')
        case 'B': maiorMenor('DB_Teste.csv')
        case 'b': maiorMenor('DB_Teste.csv')
        case 'C': mediasTipos('DB_Teste.csv')
        case 'c': mediasTipos('DB_Teste.csv')    
        case 'D': clienteVendas('DB_Teste.csv')
        case 'd': clienteVendas('DB_Teste.csv')
        case _: quit()


