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

# Valores padrões do goleiro, para testes
h_goleiro = 1.88
m_goleiro = 80.58



# Valores sobre as dimensões da elipse POK (extraídos da primeira etapa do GP 2)
s = 2.12183514 # DeltaX
k = 3.08507778 # DeltaY
# * Desenvolvimento do projeto a seguir, usando o método precisa apenas da massa corporal e de sua estatura
def calc_CM(m, h):
    #calculo da massa conforme tabela -> tronco e braço
    m1 = (m * 44.86/100)
    m2 = (m * 55.02/100)
   

    # massa total 
    mzao  = m1 + m2

    #vetores posição de acordo com o deslocamento na elipse
    r1 = 1 / mzao * (m1*s) #somatório do eixo X da elipse
    r2 = 1 / mzao * (m2*k)

    #centro da massa = vetor posição (somatório de acordo com elipse)
    form = (m1*r1 + m2*r2) / mzao

    return form


print("Central de Testes")
print(f"Com base na trajetória do goleiro -> Altura: {h_goleiro} e Massa: {m_goleiro}, seu centro de MASSA é {calc_CM(m_goleiro, h_goleiro):2f} no Tronco e no Braço!")
print("**** Método Utilizado: Zatsiorsky ****")
# fecha o arquivo
f.close()