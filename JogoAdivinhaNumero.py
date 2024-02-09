# Desafio

# Seleciona um número aleatoriamente
# pergunta um número ao usuário
# confere números
# Dá resultado

import random

def jogo_adivinhacao():
    print(f"Bemvindo ao jogo de adivinhacao!!\n")
    numAleatorio = random.randint(0, 9)

    numEscolhido1 = int(input("Tente a sorte e digite um número: \n"))
    if numEscolhido1 == numAleatorio:
        print("Você acertou!")
        print(f"O número aleatório era: {numAleatorio}\n")
    else:
        print("Ohh, no!! Número errado!")
        numEscolhido2 = int(input("Voce tem mais uma chance, Digite outro número: \n"))
        if numEscolhido2 == numAleatorio:
            print("Você acertou!")
            print(f"O número aleatório era: {numAleatorio}\n")
        else:
            print("Que mal!! Número errado, de novo! Esta e sua ultima chance!")
            numEscolhido3 = int(input("Digite o ultimo número: \n"))
            if numEscolhido3 == numAleatorio:
                print("Você acertou!")
                print(f"O número aleatório era: {numAleatorio}\n")
            else:
                print("Game Over...")
                print(f"O número aleatório era: {numAleatorio}\n")

jogo_adivinhacao()

"""""
def Main():
    numRandom = SelecionarNumero()
    PedeNumero(numRandom)

def SelecionarNumero():
    numSelecionado = random.randint(0, 9)
    print(f"O número gerado foi {numSelecionado}\n")
    return numSelecionado

def PedeNumero(numRandom):
    counter = 3
   while counter > 0:
        print(f"Você tem {counter} chances...")
        numEscolhido = int(input("Escolha um número: "))
        if numEscolhido == numRandom:
            print("Parabéns! você acertou!\n")
            break
        else:
            if numEscolhido > numRandom:
                print("Chute mais baixo.\n")
                counter -= 1
            else:
                print("Chute mais alto.\n")
                counter -= 1
                print("Game Over!")

Main()

import random

def jogo_de_adivinhacao():
    # Escolher um número aleatório entre 0 e 9
    numero_secreto = random.randint(0, 9)
    
    # Instruções para o jogador
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar um número entre 0 e 9.")
    print("Você tem três tentativas.")

    # Loop para as tentativas do jogador
    for tentativa in range(3):
        # Obter a tentativa do jogador
        palpite = int(input("Digite seu palpite: "))
        
        # Verificar se o palpite está correto
        if palpite == numero_secreto:
            print("Parabéns! Você acertou o número.")
            return  # Termina o jogo se o jogador acertar
        
        # Se o palpite estiver errado, informar ao jogador e dar uma dica
        print("Palpite errado. Tente novamente.")
    
    # Se o jogador não acertou após três tentativas, informar o número secreto
    print("Você perdeu! O número correto era", numero_secreto)

# Chamar a função para iniciar o jogo
jogo_de_adivinhacao()

import random

def jogo_adivinhacao():
    # Computador escolhe um número aleatório entre 0 e 9
    numero_secreto = random.randint(0, 9)
    
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número entre 0 e 9, você tem 3 tentativas.")

    tentativas = 3

    while tentativas > 0:
        # Usuário tenta adivinhar o número
        tentativa = int(input("Digite sua tentativa: "))

        if tentativa == numero_secreto:
            print("Parabéns! Você acertou!")
            break
        elif tentativa < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

        tentativas -= 1

    if tentativas == 0:
        print(f"Você perdeu! O número secreto era {numero_secreto}.")

# Chamando a função para iniciar o jogo
jogo_adivinhacao()
"""""