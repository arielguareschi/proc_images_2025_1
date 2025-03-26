'''
    limpa_duplicados.py
    crie um script em python onde devera ter duas funcoes,
    uma para adicionar elementos na lista, e outra para verificar
    se existem elementos duplicados na lista e retornar a lista
    sem duplicidades
'''


def add_lista(lista):
    elemento = input('Digite um valor')
    lista.append(elemento)
    return lista


def limpar_duplicados(lista):
    nova = []
    for elemento in lista:
        if elemento not in nova:
            nova.append(elemento)
    return nova


if __name__ == '__main__':
    lista = [1, 2, 2, 4, 5, 6, 7, 8, 8, 3, '3']
    print(limpar_duplicados(lista))
