def somar():
    print(1 + 2)

# Crie uma funcao que recebe dois numeros por
# parametro e retorna a sua soma
def soma(x, y):
    z = x + y
    return z

if __name__ == '__main__':
    somar()
    resultado = soma(2, 5)
    print(resultado)

    numero1 = int(input("Digite um numero: "))
    numero2 = int(input("Digite um numero: "))
    resultado2 = soma(numero1, numero2)
    print(resultado2)

