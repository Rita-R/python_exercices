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
            #print("é menor")
            pass
        else: 
            #print(X[i])
            return i+1
    return 0


#X = [12, 4, 5, 9, 7, 5, 2, 2, 1]
#Y = [9, 7, 5, 2, 2, 1]
#print(IndiceReversoCrescente(Y))



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

def Inverte2(v, i, j):
    while i < j:
        (v[i], v[j]) = (v[j], v[i])
        i += 1
        j -= 1
    return v

#X = [12, 4, 5, 9, 7, 5, 2, 2, 1]
#print(X)
#print(Inverte2(X,3,5))

# retorno: indice do menor valor que é maior q val dentro do intervalo
# retorna -1 se nao tiver
# ex X = [12, 4, 5, 9, 7, 5, 2, 2, 1] , i = 0 j = 4
# val = 5 , retorna 4 que é o indice do numero 7
def MenorMaior(vector, i, j, val):
    indice = -1
    menor = math.inf
    print(math.inf)

    for k in range(i, j+1):
        if val < vector[k] and vector[k] < menor:
            indice = k
            menor = vector[k]
    return indice

#X = [12, 4, 5, 9, 7, 5, 2, 2, 1] 
#print(MenorMaior(X,0,4,5))

def IsPalindrome(vector):
    val = (int)((len(vector))/2)
    x = len(vector)-1
    for y in range(0, val+1):
        if vector[y] == vector[x]:
            x = x - 1
        else:
            return False
    return True

#X = [5, 4, 3, 2, 3, 4, 5]
#X = [5, 4, 4, 5]
#print(IsPalindrome(X))


def AplicaFNoIntervalo(f, i, j):
  for k in range(i, j + 1):
    f(k)

def AplicaFNoIntervaloRecursiva(f, i, j):
  if i <= j:
    f(i)
    AplicaFNoIntervaloRecursiva(f, i + 1, j)

#AplicaFNoIntervalo(print, 1, 4)
#AplicaFNoIntervaloRecursiva(print, 1, 4)

def FibIterativo(v, n):
    for k in range(2, n+1):
        v.append(v[k-1] + v[k-2])


def FibRecursiva(v, i, n):
  if i <= n:
    v.append(v[i-1] + v[i-2])
    FibRecursiva(v, i+1, n)

v1= [1,1]
v2 = [1,1]
#FibIterativo(v1, 4)
#print(v1)
#FibRecursiva(v2, 2, 4)
#print(v2)

#v = [0]*10
#print(v)

#entrada: vetor com numero positivos e negativos 
#retorno: dois indices, sao os indices que representam a sequencia com a maior soma no vetor


#coplexidade log p na base 2
def Potencia(b,p):
    if p == 0:
        return 1
    elif p == 1:
        return b
    elif p % 2 == 0:
        v = Potencia(b,p//2)
        return v*v
    else:
        v = Potencia(b,p//2)
        return v*v*b

print(Potencia(2,5))


