def jogar():
    rodada=0

    while ganhou() == 0:
        print("\nRodada ",rodada+1)
        print("Jogador: ", rodada%2 + 1)
        jogo()
        linha = int(input("\nLinha:"))
        coluna = int(input("Coluna:"))

        if tabuleiro[linha-1][coluna-1] == 0:
            if(rodada%2+1)==1:
                tabuleiro[linha-1][coluna-1]=1
            else:
                tabuleiro[linha-1][coluna-1]=-1
        else:
            print("Ocupado, escolha outro")
            rodada -=1

        if ganhou() == 1:
            print("Jogador ",rodada%2 + 1," ganhou apos ", rodada+1," rodadas")

        elif ganhou() == 2:
            print("Jogo deu empate após ", rodada+1," rodadas")

        rodada +=1
    
def ganhou():
    #linhas
    for i in range(3):
        soma = tabuleiro[i][0]+tabuleiro[i][1]+tabuleiro[i][2]
        if soma==3 or soma ==-3:
            return 1

    #colunas
    for i in range(3):
        soma = tabuleiro[0][i]+tabuleiro[1][i]+tabuleiro[2][i]
        if soma==3 or soma ==-3:
            return 1

    #diagonais
    diagonal1 = tabuleiro[0][0]+tabuleiro[1][1]+tabuleiro[2][2]
    diagonal2 = tabuleiro[0][2]+tabuleiro[1][1]+tabuleiro[2][0]
    if diagonal1==3 or diagonal1==-3 or diagonal2==3 or diagonal2==-3:
        return 1
    
    ocupados = 0
    for i in range(3):
      for j in range(3):
        if tabuleiro[i][j] == 1 or tabuleiro[i][j] == -1:
          ocupados +=1
          if ocupados == 9:
            return 2

    return 0

def jogo():
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                print(" - ", end=' ')
            elif tabuleiro[i][j] == 1:
                print(" X ", end=' ')
            elif tabuleiro[i][j] == -1:
                print(" O ", end=' ')

        print()
                

tabuleiro = [ [0 for i in range(3)] for j in range(3)]

jogar()
