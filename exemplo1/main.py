print("Hello Word")

nome = "Tiburso"
nome =123456
nome = 12346.66
nome = True

if nome == "Jagunco":
    print("Nome jagunco")
elif nome == "Jocasta":
    print("Nome jocasta")
else:
    print("Eh outro nome")

nome = input("Digite seu nome: ")

# concatenacao
print("O nome digitado e " + nome)
# juncao
print("Voce digitou", nome)
# interpolacao
print(f"Voce digitou {nome}")
