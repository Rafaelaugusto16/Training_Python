import random
import Guess_word

def play():
    mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    numero_letras = tamanho_palavra(palavra_secreta)
    tentativas = 6
    erro = 0
    enforcou = False
    acertou = False

    print(" ".join(numero_letras))
    while (not enforcou and not acertou):
        chute = input("Chute uma letra:")
        chute = chute.strip().casefold()
        indice = 0

        if (chute in palavra_secreta):
            for letra in palavra_secreta:
                if (chute == letra):
                    numero_letras [indice] = letra
                indice += 1

        else:
            tentativas -= 1
            print("Você errou! Restam apenas {} tentativas" .format(tentativas))
            erro += 1

        print(" ".join(numero_letras))
        enforcou = erro == 6
        acertou = "_" not in numero_letras
    if (acertou):
        print("Você acertou a palavra secreta!")
    else:
        print("Suas tentativas acabaram! A palavra secreta era '{}'." .format(palavra_secreta))
    print("Fim do jogo!")
def mensagem_abertura():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("********************************")
    print("Adivinhe a palavra secreta!")
def carrega_palavra_secreta():
    with open ('palavras.txt') as arquivo:
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    palavra_secreta = random.choice(palavras)
    return palavra_secreta
def tamanho_palavra(palavra_secreta):
    return ["_" for letra in palavra_secreta]

if (__name__ == ("__main__")):
    Guess_word.play()