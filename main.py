'''
Criar um jogo de Sudoku usando restrições CSP

'''

def matrizTeste():
    jogo = []
    for i in range(0, 9):
        a = []
        for j in range(0, 9):
            a.append(j)
        jogo.append(a)
    return jogo

def desenhar(jogo: list):
    '''
    recebe uma matriz
    [
    [valores da linha 1],
    .
    .
    .
    [valores da linha 9]
    ]
    '''
    contador = 1
    print("   ", end="")
    for letra in "ABCDEFGHI":
        print(f" {letra} ", end="")
    print("")
    for linha in jogo:
        print(f" {contador} ", end="")
        for valor in linha:
            print(f" {valor} ", end="")
        print("")
        contador += 1

def allDiff(linha):
    if len(set(linha)) != 9:
        return False
    return True

def gerarPares():
    pares = {}
    for i in range(0, 9):
        for j in range(0, 9):
            bloco_i, bloco_j = i//3, j//3
            p = set((i, k) for k in range(0, 9)) | \
                set((k, j) for k in range(0, 9)) | \
                set((bloco_i*3 + k, bloco_j*3 + ii) for k in range(3) for ii in range(3))
            p.remove((i, j))
            pares[(i, j)] = p
    return pares

def gerarDominio(jogo):
    dominios = {}
    for i in range(0, 9):
        for j in range(0, 9):
            if jogo[i][j]:
                dominios[(i,j)] = {jogo[i][j]}
            else:
                dominios[(i,j)] = set(range(1, 10))

def completo(dominios):
    for i in dominios:
        if len(dominios[i]) != 1:
            return False
    return True
            

def ac3(jogo: list):
    pass

def revisao(dominios, xi, xj):
    revisado = False

def backtrack():
    pass

def jogoAtualizado(tabela, jogo):

    for i in range(0,9):
        for j in range(0,9):
            if len(tabela[i][j]) == 1:
                jogo[i][j] = tabela[i][j].pop()
    
    return jogo

    

def main(jogo):
    print(gerarPares())
        
   
    

if __name__ == "__main__":
    
    sudoku = [
        [8, 1, 3, 9, 0, 5, 7, 0, 6],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [4, 7, 2, 3, 6, 1, 8, 0, 5],
        [6, 0, 4, 0, 1, 0, 5, 0, 0],
        [0, 9, 5, 0, 3, 8, 0, 2, 1],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 3, 0, 0, 7, 4, 0, 0, 9],
        [5, 4, 0, 0, 8, 0, 1, 0, 3],
        [0, 6, 7, 5, 9, 0, 0, 0, 4]
    ]

    main(sudoku)