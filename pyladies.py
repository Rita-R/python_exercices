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
    
------------------------------------------------

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

--------------------------------------------------

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

-------------------------------------------------------------------------

O PyLadies Brasil decidiu fazer uma reunião com representantes de todos os grupos PyLadies do país para discutir melhorias do PyLadies
 Handbook - o kit usado para a criação de novos grupos, já que nos últimos anos muitos novos grupos surgiram. Como as representantes 
 estão espalhadas por diversas cidades, a escolha da sede da reunião será feita de modo que não prejudique demais nenhuma PyLadie. 
 Para isso, a maior distância percorrida por uma delas para chegar ao local da reunião deve ser a menor possível. 
 Em outras palavras, a distância percorrida pela PyLadie que vai percorrer a maior distância entre todas deve ser menor possível. 
 Dadas as cidades onde as Ladies se encontram e a descrição das entradas que interligam essas cidades, escreva um programa que determine 
 qual será a menor distância máxima percorrida por uma PyLadie para chegar até o local da reunião. Elas sempre fazer o menor caminho possível 
 até a cidade da reunião e sempre existe um caminho ligando quaisquer duas cidades.

Input Format

A primeira linha da entrada possui dois números inteiros N (2 ≤ N ≤ 100) e M (N − 1 ≤ M ≤ 10000), que representam, respectivamente, 
o número de cidades e o número de estradas que as interligam. As cidades são identificadas por números inteiros entre 0 e N − 1. 
As próximas M linhas da entrada possuem, cada uma, a descrição de uma estrada. Cada descrição de entrada é composta por três números inteiros: 
U, V e W, onde U e V representam cidades (0 ≤ U ≤ N − 1 e 0 ≤ V ≤ N − 1) e W representa o comprimento da estrada que une essas duas cidades 
(todas as estradas são mão dupla, 1 ≤ W ≤ 100). É sempre possível viajar entre quaisquer duas cidades com as estradas existente,s 
mas pode haver mais de uma estrada ligando o mesmo par de cidades.

Constraints

2 ≤ N ≤ 100 N − 1 ≤ M ≤ 10000 0 ≤ U ≤ N − 1 e 0 ≤ V ≤ N − 1 todas as estradas são mão dupla, 1 ≤ W ≤ 100

Output Format

Seu programa deve imprimir uma única linha contendo um número inteiro, a distância máxima percorrida por uma PyLadie para ir até a reunião, 
obedecidas as restrições estabelecidas (ou seja, essa distância máxima deve ser a menor possível).

Sample Input 0

4 4
0 1 2
0 2 4
1 3 1
2 3 5
Sample Output 0

4


# python pl4.py < input.txt

import math
import sys

v = sys.stdin.readline().split(" ")
n = int(v[0]) 
line = int(v[1])

m = [None] * n 
for i in range(n):
    m[i] = [math.inf] * n 

for i in range(line):
    v = sys.stdin.readline().split(" ")
    city1 = int(v[0])
    city2 = int(v[1])
    w = int(v[2])
    m[city1][city2] = w 
    m[city2][city1] = w

for k in range(n):
    for i in range(n):
        for j in range(n):
            if m[i][j] > ( m[i][k] + m[k][j] ):
                m[i][j] = m[i][k] + m[k][j]

maximo = [0] * n 
for i in range(n):
    maximo[i] = max(m[i])

print(min(maximo))
    
-----------------------------------------------

Você entrou no PyLadies no início desse ano por achar que o grupo tinha muitas atividades que te interessavam, mas exatamente por esse 
contingente de opções você ficou um pouco confusa sobre qual atividade quer participar. Como você simplesmente não conseguia descartar
 nenhuma da sua lista de interesses, resolveu que participará do maior número de atividades possíveis! De acordo com o número de horas 
 livres que você tem na semana e o número de horas gastas em cada uma das atividades, você gostaria de alocar o maior número de atividades 
 possíveis nas suas horas livres, independente de quais forem essas atividades. Como todo tempo livre é bem-vindo, se houver dois grupos 
 de atividades que satisfaçam essa condição, você tentará escolher aquele te propicie algum tempo realmente livre para descansar. 
 O problema é dada a gama de atividades, você tem medo de errar essa alocação se a fizer à mão, por isso resolveu usar seus conhecimentos 
 em python para garantir a melhor combinação!

Input Format

A entrada é composta por diversas linhas. A primeira linha da entrada contém o texto "horas livres", seguido de um inteiro N que as representa 
(Nós vivemos num planeta onde os dias têm muuuuitas horas <3 ). As linhas seguintes representam cada uma, uma atividade. Cada atividade tem 
seu nome (contendo estritamente letras, minúsculas e maiúsculas, espaços em branco e hifens) e uma quantidade C de horas que esta atividade
consome por semana. A entrada termina com final de arquivo. (0 < N,C < 100000)

Output Format

Seu programa deve imprimir apenas o nome das atividades, ordenados lexicograficamente. Se houver mais uma possibilidade de combinação de 
atividades que satisfaça as condições, escolha de acordo com a ordem alfabética. Existe ao menos uma atividade que cabe nos seus 
horários livres.

Sample Input 0

horas livres 20
RoadSec 20
Atualizacao do site 20
Recepcao aos calouros 2
IGEM 6
Minicurso na SECOMP 8
Minicurso Interno 20
Apresentacao 2
Sample Output 0

Apresentacao
IGEM
Minicurso na SECOMP
Recepcao aos calouros
Explanation 0

As atividades Coding Dojo e PyLadies nas Escolas têm a mesma carga horária, por isso foram distintas alfabeticamente.

Sample Input 1

horas livres 4
PyLadies nas Escolas 2
Coding Dojo 2
Meet-up 2
Recepcao aos Calouros 2
Reuniao 2
Evento 2
Apresentacao do PyLadies 2
Sample Output 1

Apresentacao do PyLadies
Coding Dojo
Explanation 1

Como todos os eventos tem a mesma carga horária e necessário distingui-los alfabeticamente.

---------------------------------------------

