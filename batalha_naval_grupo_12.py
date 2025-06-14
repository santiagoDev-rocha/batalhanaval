# Função para escolher o tamanho do tabuleiro
def tamanho_tabuleiro():
    escolha = 0
    letras10x10 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    letras12x12 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
    letras15x15 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    matriz10x10 = [["[ ~ ]" for _ in range(10)] for _ in range(10)]
    matriz12x12 = [["[ ~ ]" for _ in range(12)] for _ in range(12)]
    matriz15x15 = [["[ ~ ]" for _ in range(15)] for _ in range(15)]

    print(f"1 = 10x10 \n2 = 12x12 \n3 = 15x15")
    while escolha not in [1, 2, 3]:
        try:
            escolha = int(input("Digite a sua escolha de tamanho: "))
            if escolha not in [1, 2, 3]:
                print(f"Inválido")
        except ValueError:
            print("Inválido")

    if escolha == 1:
        print("=-" * 26)
        print("  ", end="")
        print(letras10x10)
        for i, linha in enumerate(matriz10x10, start=1):
            print(f"{i} ", end="")
            for j in linha:
                print(j, end="")
            print()
    elif escolha == 2:
        print("=-" * 26)
        print("  ", end="")
        print(letras12x12)
        for i, linha in enumerate(matriz12x12, start=1):
            print(f"{i} ", end="")
            for j in linha:
                print(j, end="")
            print()
    else:
        print("=-" * 26)
        print("  ", end="")
        print(letras15x15)
        for i, linha in enumerate(matriz15x15, start=1):
            print(f"{i} ", end="")
            for j in linha:
                print(j, end="")
            print()
    if escolha == 1:
        return 10, letras10x10, matriz10x10
    elif escolha == 2:
        return 12, letras12x12, matriz12x12
    else:
        return 15, letras15x15, matriz15x15


# Exibe o tabuleiro formatado
def exibir_tabuleiro(matriz, letras):
    print("  ", end="")
    print(letras)
    for i, linha in enumerate(matriz, start=1):
        print(f"{i} ", end="")
        for j in linha:
            print(j, end="")
        print()


# Jogador posiciona os navios
def posicionar_navios(matriz, letras):
    navios = {
        "Encouraçado": 5,
        "Porta-Aviões": 4,
        "Contratorpedeiro1": 3,
        "Contratorpedeiro2": 3,
        "Submarino1": 2,
        "Submarino2": 2,
    }

    for navio, tamanho in navios.items():
        posicionado = False
        while not posicionado:
            print(f"\nPosicione o {navio} ({tamanho} espaços):")
            posicao = input("Digite a posição (ex: A1): ").upper()
            direcao = input("Posição horizontal (H) ou vertical (V): ").upper()

            if len(posicao) < 2 or direcao not in ['H', 'V']:
                print("Inválido.")
                continue

            letra = posicao[0]
            num = posicao[1:]
            linha = int(num) - 1
            coluna = letras.index(letra)

            if direcao == 'H':
                if coluna + tamanho > len(matriz[0]):
                    print("Navio ultrapassa os limites do tabuleiro")
                    continue
                if any(matriz[linha][coluna + i] != "[ ~ ]" for i in range(tamanho)):
                    print("Posição já ocupada")
                    continue
                for i in range(tamanho):
                    matriz[linha][coluna + i] = "[ N ]"
            else:
                if linha + tamanho > len(matriz):
                    print("Navio ultrapassa os limites do tabuleiro")
                    continue
                if any((linha + i >= len(matriz)) or matriz[linha + i][coluna] != "[ ~ ]" for i in range(tamanho)):
                    print("Posição já ocupada")
                    continue
                for i in range(tamanho):
                    matriz[linha + i][coluna] = "[ N ]"
            posicionado = True
            print(f"{navio} posicionado com sucesso")

    print("\nTabuleiro do jogador:")
    print("=-" * 26)
    print("  ", end="")
    print(letras)
    for i, linha in enumerate(matriz, start=1):
        print(f"{i} ", end="")
        for j in linha:
            print(j, end="")
        print()

# Posiciona os navios da IA
def posicionar_navios_ia(matriz, letras):
    import random
    navios = {
        "Encouraçado": 5,
        "Porta-Aviões": 4,
        "Contratorpedeiro1": 3,
        "Contratorpedeiro2": 3,
        "Submarino1": 2,
        "Submarino2": 2,
    }
    for navio, tamanho in navios.items():
        posicionado = False
        while not posicionado:
            linha = random.randint(0, len(matriz) - 1)
            coluna = random.randint(0, len(matriz[0]) - tamanho)
            direcao = random.choice(['H', 'V'])

            if direcao == 'H':
                if any(matriz[linha][coluna + i] != "[ ~ ]" for i in range(tamanho)):
                    continue
                for i in range(tamanho):
                    matriz[linha][coluna + i] = "[ N ]"
            else:
                if any(matriz[linha + i][coluna] != "[ ~ ]" for i in range(tamanho)):
                    continue
                for i in range(tamanho):
                    matriz[linha + i][coluna] = "[ N ]"
            posicionado = True
            print("Navios posicionados com sucesso pela IA")

# Conta os acertos 
def contar_acertos(tabuleiro):
    return sum(cell == "[ X ]" for row in tabuleiro for cell in row)


# Executa o ataque
def realizar_ataque(tabuleiro, letras, visao_jogador, visao_ia=None, jogador=True):
    import random

    if jogador:
        escolha = False
        while not escolha:
            alvo = input("Digite a posição para atacar: ").upper()
            if len(alvo) < 2:
                print("Inválido")
                continue

            letra = alvo[0]
            numero = alvo[1:]

            linha = int(numero) - 1
            coluna = letras.index(letra)

            if visao_jogador[linha][coluna] != "[ ~ ]":
                print("Você já atacou essa posição.")
                continue

            if tabuleiro[linha][coluna] == "[ N ]":
                visao_jogador[linha][coluna] = "[ X ]"
                print("Acertou!")
            else:
                visao_jogador[linha][coluna] = "[ O ]"
                print("Errou!")
            escolha = True

    else:
        if visao_ia is None:
            print("Erro: visão da IA não fornecida.")
            return

        posicoes = [
            (i, j)
            for i in range(len(tabuleiro))
            for j in range(len(tabuleiro[0]))
            if visao_ia[i][j] == "[ ~ ]"
        ]

        if posicoes:
            linha, coluna = random.choice(posicoes)

            if tabuleiro[linha][coluna] == "[ N ]":
                tabuleiro[linha][coluna] = "[ X ]"
                print(f"IA acertou na posição {letras[coluna]}{linha + 1}")
            else:
                tabuleiro[linha][coluna] = "[ O ]"
                print(f"IA errou na posição {letras[coluna]}{linha + 1}")


# Modo jogador vs IA
def jogadorVsIA():
    import time
    print("Modo Jogador vs IA selecionado")
    tamanho, letras, matriz_jogador = tamanho_tabuleiro()
    matriz_ia = [["[ ~ ]" for _ in range(tamanho)] for _ in range(tamanho)]
    visao_jogador = [["[ ~ ]" for _ in range(tamanho)] for _ in range(tamanho)]
    visao_ia = [["[ ~ ]" for _ in range(tamanho)] for _ in range(tamanho)]

    posicionar_navios(matriz_jogador, letras)
    posicionar_navios_ia(matriz_ia, letras)

    acertos_jogador = 0
    acertos_ia = 0
    vencedor = None
    rodada = 1

    while vencedor is None:
        print(f"\nRodada: {rodada}")
        print("Vez do jogador atacar:")
        realizar_ataque(matriz_ia, letras, visao_jogador, visao_ia, jogador=True)
        acertos_jogador = contar_acertos(visao_jogador)
        if acertos_jogador >= 19:
            vencedor = "Jogador"

        if vencedor is None:
            print("Vez da IA de atacar:")
            time.sleep(2)
            realizar_ataque(matriz_jogador, letras, visao_ia, visao_jogador, jogador=False)
            acertos_ia = contar_acertos(matriz_jogador)
            if acertos_ia >= 19:
                vencedor = "IA"

        # Exibe os tabuleiros da rodada
        print("\nSua visão do tabuleiro da IA:")
        exibir_tabuleiro(visao_jogador, letras)
        print("\nSeu tabuleiro após ataque da IA:")
        exibir_tabuleiro(matriz_jogador, letras)

        rodada += 1

    print(f"\n{vencedor} venceu a partida com 19 acertos!")
    print("Fim de jogo, obrigado por jogar!")


# Modo jogador vs jogador
def jogadorVsJogador():
    print("Modo Jogador vs Jogador selecionado")
    tamanho, letras, matriz_jogador1 = tamanho_tabuleiro()
    _, _, matriz_jogador2 = tamanho_tabuleiro()

    print("\nJogador 1, posicione seus navios:")
    posicionar_navios(matriz_jogador1, letras)
    print("\n" * 50)

    print("Jogador 2, posicione seus navios:")
    posicionar_navios(matriz_jogador2, letras)
    print("\n" * 50)

    visao_jogador1 = [["[ ~ ]" for _ in range(tamanho)] for _ in range(tamanho)]
    visao_jogador2 = [["[ ~ ]" for _ in range(tamanho)] for _ in range(tamanho)]

    acertos_jogador1 = 0
    acertos_jogador2 = 0
    vencedor = None
    rodada = 1

    while vencedor is None:
        print(f"\n--- Rodada {rodada} ---")

        print("\nJogador 1, sua vez de atacar:")
        realizar_ataque(matriz_jogador2, letras, visao_jogador1, jogador=True)
        acertos_jogador1 = contar_acertos(visao_jogador1)
        if acertos_jogador1 >= 19:
            vencedor = "Jogador 1"
        else:
            print("\nJogador 2, sua vez de atacar:")
            realizar_ataque(matriz_jogador1, letras, visao_jogador2, jogador=True)
            acertos_jogador2 = contar_acertos(visao_jogador2)
            if acertos_jogador2 >= 19:
                vencedor = "Jogador 2"

        print("\nVisão do Jogador 1:")
        exibir_tabuleiro(visao_jogador1, letras)
        print("\nVisão do Jogador 2:")
        exibir_tabuleiro(visao_jogador2, letras)

        rodada += 1

    print(f"\n{vencedor} venceu a partida!")
    print("Fim de jogo, obrigado por jogar!")


# Função de escolha de modo de jogo
def modo_jogo():
    modo_de_jogo = int(input(f"Escolha o modo de jogo \n1 = IA \n2 = Jogador x Jogador:"))
    if modo_de_jogo == 1:
        jogadorVsIA()
    elif modo_de_jogo == 2:
        jogadorVsJogador()
    else:
        print("Modo de jogo invalido!")


# Menu do jogo
def menu():
    opcao = ""
    while opcao != 2:
        print("\n=-=-=-=-=-=-menu=-=-=-=-=-=-=")
        print("1.tamanho tabuleiro")
        print("2.modo de jogo")
        opcao = int(input("digite sua opção(1-2):"))
        if opcao == 1:
            tamanho_tabuleiro()
        elif opcao == 2:
            modo_jogo()
        else:
            print("Opção inválida! Tente novamente")

print("=-=-=-=-=-=-=Batalha Naval=-=-=-=-=-=-=")
menu()
