'''
    soma_lista.py
    Crie um script em python que tenha uma funcao para adicionar
    numeros a uma lista, e depois tenha outra funcao que retorne
    a soma de todos os elementos dessa lista.
    a lista deve ser passada por parametro para as funcoes

'''

def add_lista(lista):
    num = int(input('Digite um numero'))
    lista.append(num)
    return lista

def soma_lista(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma

def maior_lista(lista):
    tmp = 0
    for num in lista:
        if tmp < num:
            tmp = num
    return tmp

def media_lista(lista):
    media = soma_lista(lista) / len(lista)
    return media

if __name__ == '__main__':
    lista = []
    add_lista(lista)
    add_lista(lista)
    add_lista(lista)
    add_lista(lista)
    add_lista(lista)
    soma = soma_lista(lista)
    print(soma)