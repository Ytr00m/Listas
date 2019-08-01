def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        quantia = n % (m+1)
        if quantia > 0:
            return quantia
        return m


def usuario_escolhe_jogada(n, m):
    jogada = 0
    while jogada == 0:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada > n or jogada < 1 or jogada > m:
            print("Oops! Jogada inválida! Tente de novo.\n")
            jogada = 0
    return jogada
def campeonato():
    print("Voce escolheu um campeonato!\n")
    print("**** Partida 1 ****\n")
    usuario = 0
    computador = 0
    nump = 1
    for _ in range(3):
        vencedor = partcamp()
        nump += 1
        if nump <= 3:
            print("**** Partida {} ****\n".format(nump))
        if vencedor == 1:

            usuario = usuario + 1
        else:
            computador = computador + 1
    print("Placar final: Você  {} x {}  Computador".format(usuario, computador))           
def partida():
        print("Voce escolheu uma partida isolada!\n")
        print("**** Partida ****\n")
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        print(" ")
        if n % (m + 1) != 0:
            print("Computador começa!\n")
            while n > 0:
                jogadacomp = computador_escolhe_jogada(n, m)
                resto = n - jogadacomp
                if jogadacomp == 1:
                    print("O computador tirou uma peça.")
                elif jogadacomp != 1:
                    print("O computador tirou " + str(jogadacomp) + " peças.")
                if resto == 0:
                    print("Fim do jogo! O computador ganhou!\n")
                    break
                elif resto == 1:
                    print("Agora restam uma peça no tabuleiro.\n")
                if resto != 1:
                    print("Agora restam " + str(resto) +  " peças no tabuleiro.\n")
                n = resto 
                jogadaplayer = usuario_escolhe_jogada(n, m)
                resto = n - jogadaplayer
                if jogadaplayer == 1:
                    print("Você tirou uma peça.")
                elif jogadaplayer != 1:
                    print("Você tirou " + str(jogadaplayer) + " peças.")
                if resto == 0:
                    print("Fim do jogo! Você ganhou!\n")
                    break
                elif resto == 1:
                    print("Agora restam uma peça no tabuleiro.\n")
                if resto != 1:
                    print("Agora restam " + str(resto) +  " peças no tabuleiro.\n")
                n = resto
        if n % (m + 1) == 0:
            print("Você começa!\n")
            while n > 0:
                jogadaplayer = usuario_escolhe_jogada(n, m)
                resto = n - jogadaplayer
                if jogadaplayer == 1:
                    print("Você tirou uma peça.")
                elif jogadaplayer != 1:
                    print("Você tirou " + str(jogadaplayer) + " peças.")
                if resto == 0:
                    print("Fim do jogo! Você ganhou!\n")
                    break
                elif resto == 1:
                    print("Agora restam uma peça no tabuleiro.\n")
                if resto != 1:
                    print("Agora restam " + str(resto) +  " peças no tabuleiro.\n")
                n = resto
                jogadacomp = computador_escolhe_jogada(n, m)
                resto = n - jogadacomp
                if jogadacomp == 1:
                    print("O computador tirou uma peça.")
                elif jogadacomp != 1:
                    print("O computador tirou " + str(jogadacomp) + " peças.")
                if resto == 0:
                    print("Fim do jogo! O computador ganhou!\n")
                    break
                elif resto == 1:
                    print("Agora restam uma peça no tabuleiro.\n")
                if resto != 1:
                    print("Agora restam " + str(resto) +  "peças no tabuleiro.\n")
                n = resto 
def partcamp():
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        print(" ")
        if n % (m + 1) != 0:
            print("Computador começa!\n")
            while n > 0:
                jogadacomp = computador_escolhe_jogada(n, m)
                resto = n - jogadacomp
                if jogadacomp == 1:
                    print("O computador tirou uma peça.")
                elif jogadacomp != 1:
                    print("O computador tirou " + str(jogadacomp) + " peças.")
                if resto == 0:
                    print("Fim do jogo! O computador ganhou!\n")
                    break
                    return 0
                elif resto == 1:
                    print("Agora restam uma peça no tabuleiro.\n")
                if resto != 1:
                    print("Agora restam " + str(resto) +  " peças no tabuleiro.\n")
                n = resto 
                jogadaplayer = usuario_escolhe_jogada(n, m)
                resto = n - jogadaplayer
                if jogadaplayer == 1:
                    print("Você tirou uma peça.")
                elif jogadaplayer != 1:
                    print("Você tirou " + str(jogadaplayer) + " peças.")
                if resto == 0:
                    print("Fim do jogo! Você ganhou!\n")
                    break
                    return 1
                elif resto == 1:
                    print("Agora restam uma peça no tabuleiro.\n")
                if resto != 1:
                    print("Agora restam " + str(resto) +  " peças no tabuleiro.\n")
                n = resto
        if n % (m + 1) == 0:
            print("Você começa!\n")
            while n > 0:
                jogadaplayer = usuario_escolhe_jogada(n, m)
                resto = n - jogadaplayer
                if jogadaplayer == 1:
                    print("Você tirou uma peça.")
                elif jogadaplayer != 1:
                    print("Você tirou " + str(jogadaplayer) + " peças.")
                if resto == 0:
                    print("Fim do jogo! Você ganhou!\n")
                    break
                elif resto == 1:
                    print("Agora restam uma peça no tabuleiro.\n")
                if resto != 1:
                    print("Agora restam " + str(resto) +  " peças no tabuleiro.\n")
                n = resto
                jogadacomp = computador_escolhe_jogada(n, m)
                resto = n - jogadacomp
                if jogadacomp == 1:
                    print("O computador tirou uma peça.")
                elif jogadacomp != 1:
                    print("O computador tirou " + str(jogadacomp) + " peças.")
                if resto == 0:
                    print("Fim do jogo! O computador ganhou!\n")
                    break
                elif resto == 1:
                    print("Agora restam uma peça no tabuleiro.\n")
                if resto != 1:
                    print("Agora restam " + str(resto) +  "peças no tabuleiro.\n")
                n = resto 
print("Bem-vindo ao jogo do NIM! Escolha:\n")
print("1 - para jogar uma partida isolada")
escolha = int(input("2 - para jogar um campeonato "))
print(" ")
if escolha == 1:          
    partida()
if escolha == 2:
    campeonato()

    
