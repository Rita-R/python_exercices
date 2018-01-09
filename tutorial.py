
def Soma1(numero):
  return numero + 1

Soma1 = lambda x: x ** 2


def PrintaAplicandoEmTudo(funcao, vetor):
  for x in vetor:
    print(funcao(x))


PrintaAplicandoEmTudo(lambda x: x * (-1), [1, 2, 3])

print(len([1, 2, 3, 4]))

X = [9, 15, 20]
print(X)
X.append(13)
print(X)
X += [27]
print(X)

X[0] = -X[0]
print(X)

print("----------")

for i in range(0, len(X)):
  print(i, X[i])

for val in X:
  print(val)


print(max(-5, 9, 1000))

if 1 > 2:
  print('Impossible')
elif 2 > 3:
  print('Still impossible')
else:
  print('Aha!')

x = 0
while x < 10:
  print("Inside while", x)
  x = x + 1

def Ret2Coisas():
  return (24, 35)

(a, b) = Ret2Coisas()
print(a)
print(b)

tupla = Ret2Coisas()
print(tupla)
print(tupla[0])
print(tupla[1])
print(len(tupla))

x = 0
while x < 10:
  print("Inside while", x)
  if x == 5:
    break
  x = x + 1

for i in range(0, 10):
  if i == 5:
    continue
  print('In for with continue', i)

# Retorna o indice do ultimo elemento de uma sequencia crescente
# de tras pra frente. Ex
# IndiceReversoCrescente([12, 4, 5, 9, 7, 5, 2, 2, 1])
# Retorno esperado: 3
# Porque 3 eh o indice de 9, da sequencia
# 1, 2, 2, 5, 7, 9
def IndiceReversoCrescente(vetor):
  pass
  

