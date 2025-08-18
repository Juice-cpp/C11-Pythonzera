while True:
    sexo = input("Digite o sexo (M/F): ").strip().upper()
    if sexo == "M":
        print("Homem")
        break
    elif sexo == "F":
        print("Mulher")
        break
    else:
        print("Sexo inválido, tente novamente.")
