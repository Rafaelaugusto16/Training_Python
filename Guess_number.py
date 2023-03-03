print("********************************")
print("Bem vindo ao jogo de adivinhação!")
print("********************************")
numero_secreto = 13
total_de_rodadas= 3

for rodada in range (1,total_de_rodadas + 1):
    print("Número de tentativas", rodada, "de", total_de_rodadas)
    chute = int(input("Entre com um número: "))
    print("Você digitou o número:", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if  (acertou):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Você errou! Seu número é maior que o número secreto")
        elif(menor):
            print("Você errou! Seu número é menor que o número secreto")
    rodada = rodada + 1
print("Fim do jogo!")