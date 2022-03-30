from audioop import minmax
import csv
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def main():
    s = sort_dict(salesman_dict())
    print_salesman_table(s)
    
    minMaxClient()

def salesman_dict():
    input_file = csv.DictReader(open("DB_Teste.csv", encoding='utf-8-sig'), delimiter=";")
    salesman = {}
    for row in input_file:
        if row['Vendedor'] not in salesman:
            salesman[row['Vendedor']] = locale.atof(row['Valor'].strip(" R$"))
        else:
            salesman[row['Vendedor']] += locale.atof(row['Valor'].strip(" R$"))
    return salesman

def print_salesman_table(salesman_dict):
    print("{:<15} {:<15}".format('Vendedor','VendasTotais'))
    for s, v in salesman_dict.items():
        print("{:<15} {:<15}".format(s,locale.currency(v, grouping=True)))

def sort_dict(dict):
    sorted_values = sorted(dict.values(), reverse=True)
    sorted_dict = {}

    for i in sorted_values:
        for k in dict.keys():
            if dict[k] == i:
                sorted_dict[k] = dict[k]
                break
    return sorted_dict

def minMaxClient():
    input_file = csv.DictReader(open("DB_Teste.csv", encoding='utf-8-sig'), delimiter=";")
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
        


if __name__ == "__main__":
    main()