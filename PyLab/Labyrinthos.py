import time

import numpy as np

# labirinto = [[0,1,0,0,0,0],
#              [0,1,1,0,1,0],
#              [0,1,0,0,1,0],
#              [0,1,1,1,1,0],
#              [0,0,0,1,0,0],
#              [0,1,1,1,0,0],
#              [0,1,0,1,1,0],
#              [0,0,0,0,1,0]]

labirinto = [[0,1,0,0,0,0],
             [0,1,1,0,1,0],
             [0,1,0,0,1,0],
             [0,1,1,1,1,0],
             [0,0,0,1,0,0],
             [0,1,1,1,0,0],
             [0,1,0,1,1,0],
             [0,1,0,0,0,0]]

#Armazena coordenadas que tem 1, isso é caminho

def labirintoExiste(lab):
    start = None
    end = None
    for i in range(len(lab[0])):
        if(lab[0][i] == 1):
            start = (0,i)
    for i in range(len(lab[-1])):
        if (lab[-1][i] == 1):
            end = (len(lab)-1, i)
    assert start is not None and end is not None, "Labirinto não existe"
    return start,end

# funcao para caminhar pelo labirinto
def caminhaLabirinto(lab, start, end):

    #posição atual no labirinto
    posicaoAtual = np.array(start)
    
    # Pra aonde o "caminhante" está olhando
    #-------------------CIMA-BAIXO-ESQUERDA-DIREITA
    direcoes = np.array([(1,0), (-1,0), (0,-1), (0,1)])
    frenteAtual = 0 #TODO variavel que ta olhando pra minha frente atual, isso é frente relativa

    while True:
        print("=============INCIO WHILE=============")
        time.sleep(1)
        print("Estou em: " +  str(posicaoAtual))


        if (np.array_equal(posicaoAtual, np.array(end))):
            print("CHEGUEEEEEEEEEEEEEI\nFIM DO LABIRINTO")
            break

        # checa acima
        proximoPosicao = np.add(np.array(posicaoAtual),np.array(direcoes[0]))
        print("Estou olhando para: "+ str(proximoPosicao))
        x,y = proximoPosicao[0],proximoPosicao[1]
        if(lab[x][y] == 1):
            posicaoAtual = proximoPosicao
            print("CIMA!")
            continue

        # checa a direita
        proximoPosicao = np.add(np.array(posicaoAtual), np.array(direcoes[3]))
        x,y = proximoPosicao[0],proximoPosicao[1]
        if(lab[x][y] == 1):
            posicaoAtual = proximoPosicao
            print("DIREITA!")
            continue

        # checa a esquerda
        proximoPosicao = np.add(np.array(posicaoAtual), np.array(direcoes[2]))
        x, y = proximoPosicao[0], proximoPosicao[1]
        if (lab[x][y] == 1):
            posicaoAtual = proximoPosicao
            print("ESQUERDA!")
            continue

        # checa a baixo
        proximoPosicao = np.add(np.array(posicaoAtual), np.array(direcoes[1]))
        x, y = proximoPosicao[0], proximoPosicao[1]
        if (lab[x][y] == 1):
            posicaoAtual = proximoPosicao
            print("BAIXO!")
            continue

        if (np.array_equal(posicaoAtual, np.array(start))):
            print("LABIRINTO FALSO, tentou...")
            break


#testes
x = None
y = None
x,y = labirintoExiste(labirinto)
print(x)
print(y)
caminhaLabirinto(labirinto,x,y)