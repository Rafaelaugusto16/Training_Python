print("********************************")
print("Bem vindo ao jogo de adivinhação!")
print("********************************")
numero_secreto = 13
total_de_rodadas= 3
rodada= 1
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
print("Fim do jogo!")