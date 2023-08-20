import random

def jogar():

    print("***************************************************************************************************")
    print("**Bem vindo ao jogo de avinhação, você terá 3 tentativas para acertar o número secreto**")
    print("\nAcertou de primeira: 100 pontos;\nNa segunda tentativa: 50 pontos;\nTerceira 10 pontos;\nErrou: 0.")
    print("***************************************************************************************************")

    numero_secreto = random.randint(1, 20)

    for tentativas in range(1, 4):

        print(f"Tentativa: {tentativas}")
        chute = int(input(f"Digite um número inteiro de 1 a 20: "))

        while True:

            if chute > 20 or chute < 0:
                chute = int(input(f"Digite um número inteiro de 1 a 20(Não pode ser negativo): "))
            else:
                break

        print(f"Você digitou {chute}")

        if chute == numero_secreto:
            print(f"Você acertou! O número era {numero_secreto}")
            print("Fim do jogo!")
            break

        elif tentativas == 3:
            print(f"Você não acertou em 3 tentativas, o número era {numero_secreto}")    
        elif chute > numero_secreto:
            print("O número que você digitou é maior que o secreto, tente novamente!")
        elif chute < numero_secreto:
            print("O número que você digitou é menor que o secreto, tente novamente!")

    if tentativas == 1:
        print("Você fez 100 pontos, parabéns!")
    elif tentativas == 2:
        print("Você fez 50 pontos, poderia ser melhor!")
    elif tentativas == 3 and chute == numero_secreto:
        print("Você fez 10 pontos, tenta melhorar!")
    else:
        print("Você fez 0 pontinhos! Esperava mais sorte.")

if __name__ == '__main__':
    jogar()
        