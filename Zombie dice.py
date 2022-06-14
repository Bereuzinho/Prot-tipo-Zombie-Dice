from random import randint
from time import sleep
from operator import itemgetter
from collections import namedtuple

print("ZOMBIE DICE (Protótipo semana 4)")

print("Seja bem vindo ao ZOMBIE DICE!")
sleep(1)

print("⇋"*30)

numJogadores : int = 0
while numJogadores < 2 :
     numJogadores = int(input("Informe a quantidade de jogadores: "))
     if numJogadores < 2 :
         print("Precisa de dois ou mais jogadores!")
     else :
         break

print("⇋"*30)

listaDeJogadores : str = []

for i in range(numJogadores) :
    nome = str(input("Digite o nickname do jogador:" ))
    listaDeJogadores.append(nome)



print("⇋⇋⇋⇋⇋⇋ Lista de jogadores : ⇋⇋⇋⇋⇋⇋")


for i in range(len(listaDeJogadores)) :
    print("🧟 jogador ", str(i+1),": ", (listaDeJogadores[i]))
    sleep(1)

dadoVerde : str = "CPCTPC"
dadoAmarelo : str = "TPCTPC"
dadoVermelho : str = "TPTCPT"

numDadoVerde : int = 6
numDadoAmarelo : int = 4
numDadoVermelho : int = 3

listaDados : str = []
for i in range(numDadoVerde) :
    listaDados.append(dadoVerde)
for i in range(numDadoAmarelo) :
    listaDados.append(dadoAmarelo)
for i in range(numDadoVermelho) :
    listaDados.append(dadoVermelho)

print("⇋⇋⇋⇋⇋⇋ INICIANDO O JOGO ! ⇋⇋⇋⇋⇋⇋")

jogadorAtual : int = 0
dadosSorteados : str = []
tiros : int = 0
cerebros : int = 0
passos : int = 0
quantDados : int = 0

while True  :
    print(" 🕹️ Turno do jogador :", listaDeJogadores[jogadorAtual])
    for i in range (4) :
        numSorteado : int = randint(0, len(listaDados) - 1)
        dadoSorteado = listaDados[numSorteado]
        if dadoSorteado == "CPCTPC" :
            corDado = "Verde"
        elif dadoSorteado == "TPCTPC" :
            corDado = "Amarelo"
        else :
            corDado = "Vermelho"


        print(" 🎲 Dado sorteado ", corDado)
        dadosSorteados.append(dadoSorteado)
        sleep(1)

    print("⇋" * 30)

    print("As faces sorteadas foram :")

    for dadoSorteado in dadosSorteados :
        numFaceDado = randint(0,5)
    if dadoSorteado[numFaceDado] == "C":
        print("- 🤯 CÉREBRO (Você comeu um cérebro)")
        cerebros = + 1
    elif dadoSorteado[numFaceDado] == "T" :
        print("- 🔫 TIRO (Você levou um tiro)")
        tiros = +1
    else :
        print("- 🚶 Passos (Uma vitima escapou)")
        passos = +1
    sleep(1)

    print("⇋" * 30)

    print("Score atual : ")
    sleep(1)
    print("Cérebros ",cerebros)
    sleep(1)
    print("Tiros ",tiros)
    sleep(1)
    print("Fugitivos",passos)
    sleep(1)

    print("⇋" * 30)

    continuarTurno : str = input(" ⛔️Você deseja continuar rolando os dados? (s = sim / n = não)  ⛔️")
    if continuarTurno == "n" :
        jogadorAtual = jogadorAtual +1
        dadoSorteado = []
        tiros = 0
        cerebros = 0
        passos = 0
        if jogadorAtual == len(listaDeJogadores) :
            print(" ⇋⇋⇋⇋⇋ Finalizando o protótipo do jogo ... ⇋⇋⇋⇋⇋ ")
            break

        else :
            print("Iniciando mais uma rodada do jogo! ")
            dadoSorteado = []

























