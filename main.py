import advinhacao
import forca

def escolha_jogo():
    
    print("*******************************")
    print("**Bem vindo ao dash de jogos!**")
    print("*******************************")

    print("Escolha qual jogo você quer jogar:")
    jogo = int(input("Para jogar Adivinhação digite: 1\nPara jogar Forca digite: 2\nQual será sua opção? "))

    if jogo == 1:
        advinhacao.jogar()
    elif jogo == 2:
        forca.jogar()

if __name__ == '__main__':
    escolha_jogo()