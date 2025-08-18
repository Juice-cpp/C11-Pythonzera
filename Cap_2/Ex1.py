nome = input("Digite seu nome completo: ").strip()

print("Maiúsculas:", nome.upper())
print("Minúsculas:", nome.lower())
print("Total de letras (sem espaços):", len(nome.replace(" ", "")))

nomes = nome.split()
nomes[-1] = "do Inatel"
print("Com último nome trocado:", " ".join(nomes))
