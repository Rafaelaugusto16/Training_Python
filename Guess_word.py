import random

import Guess_word

def play():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("********************************")
    print("Adivinhe a palavra secreta!")

    palavra_secreta = "uva".casefold()
    tamanho_palavra = ["_" for letra in palavra_secreta]

    tentativas = 6
    erro = 0
    enforcou = False
    acertou = False

    print((tamanho_palavra))
    while (not enforcou and not acertou):
        chute = input("Chute uma letra:")
        chute = chute.strip().casefold()
        indice = 0

        if (chute in palavra_secreta):
            for letra in palavra_secreta:
                if (chute == letra):
                    tamanho_palavra [indice] = letra
                indice += 1

        else:
            tentativas -= 1
            print("Você errou! Restam apenas {} tentativas" .format(tentativas))
            erro += 1

        print(tamanho_palavra)
        enforcou = erro == 6
        acertou = "_" not in tamanho_palavra
    if (acertou):
        print("Você acertou a palavra secreta!")
    else:
        print("Suas tentativas acabaram! A palavra secreta era '{}'." .format(palavra_secreta))
    print("Fim do jogo!")

if (__name__ == ("__main__")):
    Guess_word.play()


