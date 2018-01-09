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