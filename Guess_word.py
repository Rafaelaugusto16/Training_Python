import random

import Guess_word


def play():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("********************************")
    print("Adivinhe a palavra secreta!")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        chute = input("Chute uma letra:")

        posição_letra = 0
        for letra in palavra_secreta:
            if (chute == letra):
                print("Você acertou a letra! {} está na posição {} " .format(chute,posição_letra))
            posição_letra = posição_letra +1

if (__name__ == ("__main__")):
    Guess_word.play()


