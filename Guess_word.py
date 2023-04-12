import random
import Guess_word

def play():
    mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    numero_letras = tamanho_palavra(palavra_secreta)
    print(" ".join(numero_letras))

    erro = 0

    enforcou = False
    acertou = False


    while (not enforcou and not acertou):
        chute = chute_do_jogador()
        if (chute in palavra_secreta):
            acertou_a_letra(chute, numero_letras, palavra_secreta)
        else:
            erro += 1
            desenha_forca(erro)

        print(" ".join(numero_letras))
        enforcou = erro == 7
        acertou = "_" not in numero_letras
    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo!")
def mensagem_abertura():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")
    print("Adivinhe a palavra secreta!")
def carrega_palavra_secreta():
    tema = False
    while (tema == False):
        try:
            tema_palavra = int(input("Escolha qual o tema da rodada [1] frutas [2] estados:"))
            if (tema_palavra == 1):
                print("O tema escolhido foi frutas! Boa sorte!")
                with open ('palavras_frutas.txt',encoding='UTF-8') as arquivo:
                    palavras = []
                    for linha in arquivo:
                        linha = linha.strip()
                        palavras.append(linha)
                tema = True
                palavra_secreta = random.choice(palavras).casefold()
                palavra_secreta = "".join(palavra_secreta.split())
            elif (tema_palavra == 2):
                with open('Palavras_estados.txt', encoding='UTF-8') as arquivo:
                    palavras = []
                    for linha in arquivo:
                        linha = linha.strip()
                        palavras.append(linha)
                tema = True
                palavra_secreta = random.choice(palavras).casefold()
                palavra_secreta = "".join(palavra_secreta.split())
            else:
                print("Escolha o tema conforme indicado!")
        except ValueError:
                print("Escolha o tema conforme indicado!")
    return palavra_secreta
def tamanho_palavra(palavra_secreta):
    return ["_" for letra in palavra_secreta]
def chute_do_jogador():
    chute = input("Chute uma letra:")
    chute = chute.strip().casefold()
    return chute
def acertou_a_letra(chute, numero_letras, palavra_secreta):
    indice = 0
    for letra in palavra_secreta:
        if (chute == letra):
            numero_letras[indice] = letra
        indice += 1

def imprime_mensagem_vencedor():
    print("Você acertou a palavra secreta!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
def imprime_mensagem_perdedor(palavra_secreta):
    print("*"*55)
    print("Suas tentativas acabaram! A palavra secreta era '{}'.".format(palavra_secreta))
    print("*" *55)
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erro):
    print("  _______     ")
    print(" |/      |    ")

    if(erro == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erro == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erro == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erro == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erro == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erro == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erro == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == ("__main__")):
    Guess_word.play()