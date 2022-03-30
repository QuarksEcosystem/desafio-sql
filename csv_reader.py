import csv
import locale
import sys

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def main(argv):
    filename = str(sys.argv[1])

    #Cria a tabela auxiliar com o os vendedores e totais de venda ordenados de maior para menor
    s = sort_dict(salesman_dict(filename))
    print_salesman_table(s)
    create_auxiliar_table(s)

    #Imprime cliente compra mais cara e da mais barata
    minMaxClient(filename)

    #Média do valor de vendas por tipo de venda
    print_sales_mean(filename)

    #Total de vendas por clientes
    total_sales_per_client(filename)

#devolve um dictionary com os vendedores como chave e os valores totais vendidos como valor
def salesman_dict(filename):
    input_file = csv.DictReader(open(filename, encoding='utf-8-sig'), delimiter=";")
    salesman = {}
    for row in input_file:
        if row['Vendedor'] not in salesman:
            salesman[row['Vendedor']] = locale.atof(row['Valor'].strip(" R$"))
        else:
            salesman[row['Vendedor']] += locale.atof(row['Valor'].strip(" R$"))
    return salesman

#imprime todos os vendedores e seus respectivos valores totais de venda
def print_salesman_table(salesman_dict):
    print("{:<15} {:<15}".format('Vendedor','VendasTotais'))
    for s, v in salesman_dict.items():
        print("{:<15} {:<15}".format(s,locale.currency(v, grouping=True)))
    print("\n")

def sort_dict(dict):
    sorted_values = sorted(dict.values(), reverse=True)
    sorted_dict = {}

    for i in sorted_values:
        for k in dict.keys():
            if dict[k] == i:
                sorted_dict[k] = dict[k]
                break
    return sorted_dict

#imprime os clientes da compra mais cara e da compra mais barata
def minMaxClient(filename):
    input_file = csv.DictReader(open(filename, encoding='utf-8-sig'), delimiter=";")
    minClient = ""
    minVal = float('inf')
    maxClient = ""
    maxVal = 0.0
    for row in input_file:
        val = locale.atof(row['Valor'].strip(" R$"))
        if val > maxVal:
            maxVal = val
            maxClient = row['Cliente']
        if val < minVal:
            minVal = val
            minClient = row['Cliente']
    print(maxClient, "foi responsável pela maior compra") 
    print(minClient, "foi responsável pela menor compra.\n")

#Imprime o valor médio de cada tipo de venda        
def print_sales_mean(filename):
    input_file = csv.DictReader(open(filename, encoding='utf-8-sig'), delimiter=";")
    # Tipo, quantidade, valor total
    sales = {}
    for row in input_file:
        if row['Tipo'] not in sales:
            sales[row['Tipo']] = (1, locale.atof(row['Valor'].strip(" R$")))
        else:
            n, v = sales[row['Tipo']]
            sales[row['Tipo']] = (n + 1, v + locale.atof(row['Valor'].strip(" R$")))

    print("Valor médio por tipo de venda:")
    for k, i in sales.items():
        n, v = i
        print("{:<15} {:<15}".format(k,locale.currency(v/n, grouping=True)))
    print("\n")

#Cria um arquivo .csv com os vendedores por ordem de total arrecadado em vendas
def create_auxiliar_table(salesman_dict):
    with open('salesman.csv', 'w', newline='') as csvfile:
        fieldnames = ['Vendedor', 'Total de Vendas']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")

        writer.writeheader()
        for s, v in salesman_dict.items():
            writer.writerow({'Vendedor': s, 'Total de Vendas': locale.currency(v, grouping=True)})

#Total de vendas por clientes
def total_sales_per_client(filename):
    input_file = csv.DictReader(open(filename, encoding='utf-8-sig'), delimiter=";")
    # Tipo, quantidade, valor total
    clientSales = {}
    for row in input_file:
        if row['Cliente'] not in clientSales:
            clientSales[row['Cliente']] = 1
        else:
            clientSales[row['Cliente']] += 1

    print("Total de vendas por clientes:")
    for k, n in clientSales.items():
        print("{:<15} {:<15}".format(k,n))        

if __name__ == "__main__":
    main(sys.argv)