#  Arquivo principal correspondente à 2ª etapa do Projeto Bola na Rede
# Equipe 3: Abraão, Élen, Eduardo, Felipe, Gabriel e Samantha


from random import choice
import json

class color:
    RED = '\033[91m'


class paramsZat:
    head = "50.02%"
    trunk = "44.86%"
    arm = "55.02%"
    forearm = "57.26%"
    hand = "63.09%"
    thigh = "45.49%"
    leg = "40.47%"
    foot = "55.85%"

# Escolhe um goleiro aleatoriamente
# Talvez não seja necessário
def escolher_goleiro(data):
    goleiro = choice(data)
    return goleiro


f = open("json/goleiros.json")
data_goleiros = json.load(f)

# Escolhendo um goleiro
goleiro = escolher_goleiro(data_goleiros)
print(goleiro)

#valores seguindo tabela de zat: parâmetros anatômicos
print("Tabela de Parâmetros Antropométricos (Centro de MASSA)")
print(f"""Cabeça: {paramsZat.head}
Tronco: {paramsZat.trunk}
Braço: {paramsZat.arm}
Antebraço: {paramsZat.forearm}
Mão: {paramsZat.hand}
Coxa: {paramsZat.thigh}
Perna: {paramsZat.leg}
Pé: {paramsZat.foot}
""")

# Valores sobre as dimensões da elipse POK (extraídos da primeira etapa do GP 2)
s = 2.12183514 # DeltaX
k = 3.08507778 # DeltaY

# Valores padrões do goleiro, para testes
h_goleiro = 1.88
m_goleiro = 80.58

# * Desenvolvimento do projeto a seguir, usando o método precisa apenas da massa corporal e de sua estatura
def calc_CM(m, h):
    form = (s*m + k*h)**2 / 4

    return form


print("Central de Testes")
print(f"Com base na trajetória do goleiro {goleiro}, seu centro de MASSA é {calc_CM()}!")
print("**** Método Utilizado: Zatsiorsky ****")
# fecha o arquivo
f.close()