import Guess_number
import Guess_word
print("Escolha o jogo que deseja jogar")
jogo = int(input("Adivinhe o número [1] ou Adivinhe a palavra [2]:"))
if (jogo == 1):
    print("Você escolheu Adivinhe o número! Boa sorte!")
    Guess_number.play()
elif(jogo == 2):
    print("Você escolheu Adivinhe a palavra! Boa sorte!")
    Guess_word.play()
else:
    print("escolha um jogo conforme indicado!")
