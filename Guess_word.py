import random

import Guess_word


def play():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("********************************")
    print("Adivinhe a palavra secreta!")

    palavra_secreta = "UVINHA".casefold()
    tamanho_palavra = list("_"*(len(palavra_secreta)))
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
          erro += 1
        print(tamanho_palavra)
        enforcou = erro == 6
        acertou = "_" not in tamanho_palavra
    if (acertou):
        print("Você acertou a palavra secreta!")
    else:
        print("Suas tentativas acabaram!")
    print("Fim do jogo!")

if (__name__ == ("__main__")):
    Guess_word.play()


