'''
converter_horas.py
Crie um script em python onde recebe um valor que
representa uma hora no formado 12h e converte a mesma
para o formato 24h (split)
'''

def convert_to_12(hora):
    partes = hora.split(':')
    if int(partes[0]) > 24:
        return "Horas nao existe"
    elif int(partes[0]) > 12:
        new_hora = int(partes[0]) - 12
        modificador = "PM"
    else:
        new_hora = int(partes[0])
        modificador = "AM"
    if int(partes[1]) >= 60:
        return "Minutos nao existe"
    return f"{new_hora}:{partes[1]} {modificador}"

def convert_to_24(hora):
    quebrar = hora.split(' ')
    partes = quebrar[0].split(':')
    modificador = quebrar[1]
    if modificador == 'PM':
        new_hora = int(partes[0]) + 12
    else:
        new_hora = int(partes[0])
    return f"{new_hora}:{partes[1]}"

if __name__ == '__main__':
    print(convert_to_12("16:20"))
    print(convert_to_24("4:20 PM"))

# hora = "12/232/22/222/222/222/222/"
# quebrado = hora.split("/")
# print(quebrado)