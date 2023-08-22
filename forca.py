import random

def bem_vindo():
    '''
    Retorna o boas-vindas ao jogador
    '''

    print("**************************")
    print("****Bem vindo a Forca!****")
    print("**************************\n")

def palavras():
    '''
    Retorna a lista de palavras para o jogo
    '''

    palavras = []

    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    return palavras

def segredo(lista_palavras):
    '''
    Retorna a palavra secreta do jogo
    '''
    segredo = random.choice(lista_palavras).upper()
    return segredo

def dicas(palavra_secreta):
    '''
    Retorna as dicas para o jogador de qual tipo de palavra que é
    '''
    lista_palavras = palavras()

    if palavra_secreta.capitalize() in lista_palavras[:25]:
        print("DICA: É uma fruta!\n")
    elif palavra_secreta.capitalize() in lista_palavras[25:50]:
        print("DICA: É um vegetal!\n")
    elif palavra_secreta.capitalize() in lista_palavras[50:70]:
        print("DICA: É uma montadora de carros!\n")
    elif palavra_secreta.capitalize() in lista_palavras[70:]:
        print("DICA: É um objeto!\n")

def mensagem_perdedor(palavra_secreta):
    '''
    Retorna a mensagem visual mais bonita do perdedor
    '''

    print("Puxa, você foi enforcado!\n")
    print(f"A palavra era {palavra_secreta}")
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

def mensagem_vencedor(palavra_secreta):
    '''
    Retorna a mensagem do vencedor
    '''

    print(f"Parabéns, você acertou, a palavra era: {palavra_secreta}")
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

def desenha_forca(erros):
    '''
    Retorna o desenho visual da forca
    '''

    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def logica(palavra_secreta):
    '''
    Retorna a lógica central do looping do jogo
    '''

    #print(palavra_secreta)
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0
    tentativas = 6

    print(f"Sua palavra:\n{letras_acertadas}\n")

    while not enforcou and not acertou:

        print(f"Você tem {tentativas} tentativas!")
        chute = input("Qual a letra? ").strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1

        else:
            erros += 1
            tentativas -= 1
            desenha_forca(erros)

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)


    if acertou:
        mensagem_vencedor(palavra_secreta)
    else:
        mensagem_perdedor(palavra_secreta)


def jogar():
    '''
    Retorna o jogo principal
    '''
    lista_palavras = palavras()
    palavra_secreta = segredo(lista_palavras)

    bem_vindo()

    dicas(palavra_secreta)

    logica(palavra_secreta)

if __name__ == '__main__':
    jogar()