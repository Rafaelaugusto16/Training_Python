import random

print("********************************")
print("Bem vindo ao jogo de adivinhação!")
print("********************************")
print("Adivinhe o número secreto!")

numero_secreto = random.randrange(1,21)
rodada = 1
nivel_do_jogo = 0

while (nivel_do_jogo != 1 or nivel_do_jogo != 2 or nivel_do_jogo != 3):
    print("Nivel [1] facil [2] médio [3] dificil")
    nivel_do_jogo = int(input("Escolha o nível de dificuldade:"))
    if (nivel_do_jogo == 1):
        total_de_rodadas = 6
        break
    elif (nivel_do_jogo == 2):
        total_de_rodadas = 4
        break
    elif (nivel_do_jogo == 3):
        total_de_rodadas = 3
        break
    else:
        print("Escolha o nível conforme indicado!")

while (rodada <= total_de_rodadas):
    print("Número de tentativas {} de {}".format(rodada, total_de_rodadas))
    chute = int(input("Entre com um número de 1 a 20: "))
    print("Você digitou o número:", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(chute<1 or chute>20):
        print("O número deve estar entre 1 e 20!")
        continue
    elif(chute>=1 and chute<=20):
        rodada = rodada + 1
        if  (acertou):
           print("Você acertou!")
           break
        else:
            if(maior):
                print("Você errou! Seu número é maior que o número secreto.")
            elif(menor):
                print("Você errou! Seu número é menor que o número secreto.")

print("Fim do jogo!\no número secreto era: {}!" .format(numero_secreto))