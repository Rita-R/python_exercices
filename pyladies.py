import sys

k = 1
while True:
    line = int(sys.stdin.readline())
    if line == 0:
        break
    print("Coding Dojo %d" %(k))
    n = int(line)
    namePar = sys.stdin.readline()[:-1]
    nameImpar = sys.stdin.readline()[:-1]
    for i in range(1, n):
        sys.stdin.readline()
    v = sys.stdin.readline().split(" ")
    result = int(v[0]) + int(v[1])
    if result % 2 == 0:
        print("O Piloto sera %s e o Copiloto sera %s!" %(namePar, nameImpar))
    else:
        print("O Piloto sera %s e o Copiloto sera %s!" %(nameImpar, namePar))
    print()
    k = k+1
    


import sys

total = int(sys.stdin.readline()) 
if total == 0:
    exit(0)
maximo = 0
hoje = 0
ano = 0
total = total - 1
for line in sys.stdin:
    v = line.split(" ")
    s = int(v[0])
    e = int(v[1])
    hoje = (hoje - s ) + e
    if hoje >= maximo:
        maximo = hoje
        ano = 2017 - total
    total = total - 1
    
print("Record: %d, %d alunas!" %(ano, maximo))


import sys

k = 1

while True:
    line = int(sys.stdin.readline())
    if line == 0:
        break
    print("Evento %d" %(k))
    maximo = 0
    ganhadora = []
    for i in range(line):
        v = sys.stdin.readline().split(" ")
        cod = v[0] 
        pontos = int(v[1])
        if pontos > maximo:
            maximo = pontos
            ganhadora = [cod]
        elif pontos == maximo:
            ganhadora.append(cod)
    k = k+1
    print(" ".join(ganhadora))
    print()