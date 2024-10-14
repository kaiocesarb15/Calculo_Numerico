import numpy as np

# Definindo a matriz A e o vetor B
A = np.array([[3, 4, 7, 20],
              [20, 25, 40, 50],
              [10, 15, 20, 22],
              [10, 8, 10, 15]], dtype=float)

B = np.array([504, 1970, 970, 601], dtype=float)

# Função para realizar a eliminação de Gauss
def eliminacao_gauss(A, B):
    n = len(B)
    # Formando a matriz aumentada
    matriz_aum = np.hstack((A, B.reshape(-1, 1)))

    # Eliminação
    for i in range(n):
        # Encontra o maior elemento da coluna para evitar erros de precisão
        linha_max = np.argmax(np.abs(matriz_aum[i:, i])) + i
        # Troca as linhas
        matriz_aum[[i, linha_max]] = matriz_aum[[linha_max, i]]

        # Faz a eliminação
        for j in range(i + 1, n):
            fator = matriz_aum[j, i] / matriz_aum[i, i]
            matriz_aum[j] -= fator * matriz_aum[i]

    # Resolvendo pela substituição retroativa
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (matriz_aum[i, -1]
               - np.dot(matriz_aum[i, i+1:n],
               x[i+1:n])) / matriz_aum[i, i]

    return x

# Resolvendo o sistema
solucao = eliminacao_gauss(A, B)

# Exibindo a solução
print("Solução encontrada:")
for i, val in enumerate(solucao):
    print(f"x{i+1} = {val:.2f}")

# Validando a solução
for i in range(len(B)):
    sol = sum(A[i][j] * solucao[j] for j in range(len(solucao)))
    print(f'Valor desejado: {B[i]} | Solução encontrada:{sol:.2f}')
