import math
# Retorna o indice do ultimo elemento de uma sequencia crescente
# de tras pra frente. Ex
# IndiceReversoCrescente([12, 4, 5, 9, 7, 5, 2, 2, 1])
# Retorno esperado: 3
# Porque 3 eh o indice de 9, da sequencia
# 1, 2, 2, 5, 7, 9
def IndiceReversoCrescente(X):
    for i in range(len(X) - 2, -1, -1):
        if X[i+1] <= X[i]:
            pass
        else: 
            return i+1
    return 0

#inverter o vetor nessa faixa de i a j
# ex X = [12, 4, 5, 9, 7, 5, 2, 2, 1] de 0 a 3
# resposta: X = [9, 5, 4, 12, 7, 5, 2, 2, 1]
# retorna o vetor
def Inverte(vector, i, j):
    val = (int)(((j-i)+1)/2)
    x = j
    for y in range(i, i+val):
        (vector[y], vector[x]) = (vector[x], vector[y])
        x = x - 1
    return vector

# retorno: indice do menor valor que é maior q val dentro do intervalo
# retorna -1 se nao tiver
# ex X = [12, 4, 5, 9, 7, 5, 2, 2, 1] , i = 0 j = 4
# val = 5 , retorna 4 que é o indice do numero 7
def MenorMaior(vector, i, j, val):
    indice = -1
    menor = math.inf
    for k in range(i, j+1):
        if val < vector[k] and vector[k] < menor:
            indice = k
            menor = vector[k]
    return indice


def NextPermutation(vector):
    j = len(vector)-1
    i = IndiceReversoCrescente(vector)
    if i == 0:
        return None
    val = vector[i-1]
    k = MenorMaior(vector, i, j, val)
    (vector[k], vector[i-1]) = (vector[i-1], vector[k])
    Inverte(vector, i, j)
    return vector

X = [1, 2, 3, 4]
print(X)
while NextPermutation(X) != None:
    print(X)


