numero = int(input("Digite o número para ver a tabuada: "))
inicio = int(input("Digite o valor inicial do intervalo: "))
fim = int(input("Digite o valor final do intervalo: "))

for i in range(inicio, fim + 1):
    print(f"{numero} x {i} = {numero * i}")
