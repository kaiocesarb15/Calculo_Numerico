import numpy as np

# Definindo a matriz A e o vetor B
A = np.array([[3, 4, 7, 20],
              [20, 25, 40, 50],
              [10, 15, 20, 22],
              [10, 8, 10, 15]], dtype=float)

B = np.array([504, 1970, 970, 601], dtype=float)

# Função para verificar a convergência pelas linhas
def verificar_dominancia_linhas(A):
    n = A.shape[0]
    for i in range(n):
        soma_linha = np.sum(np.abs(A[i])) - np.abs(A[i][i])
        if np.abs(A[i][i]) <= soma_linha:
            return False
    return True

# Função para verificar a convergência pelas colunas
def verificar_dominancia_colunas(A):
    n = A.shape[1]
    for j in range(n):
        soma_coluna = np.sum(np.abs(A[:, j])) - np.abs(A[j][j])
        if np.abs(A[j][j]) <= soma_coluna:
            return False
    return True

# Função para verificar a convergência pelo critério de Sassenfeld
def verificar_sassenfeld(A, B):
    n = A.shape[0]
    beta = np.zeros(n)

    for i in range(n):
        soma_termos = 0
        for j in range(n):
            if j != i:
                soma_termos += np.abs(A[i][j]) * beta[j]
        beta[i] = (soma_termos + np.abs(B[i])) / np.abs(A[i][i])
        if beta[i] >= 1:
            return False
    return True

# Verificando a convergência
dominancia_linhas = verificar_dominancia_linhas(A)
dominancia_colunas = verificar_dominancia_colunas(A)
convergencia_sassenfeld = verificar_sassenfeld(A, B)

print("A matriz A é diagonalmente dominante pelas linhas:", dominancia_linhas)
print("A matriz A é diagonalmente dominante pelas colunas:", dominancia_colunas)
print("A matriz A satisfaz o critério de Sassenfeld:", convergencia_sassenfeld)
