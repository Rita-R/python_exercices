class Casal:
  class Pessoa:
    def __init__(self, nome):
      self.nome = nome

  def __init__(self, homi, muie):
    self.homi = homi
    self.muie = muie

homi = Casal.Pessoa('Denis')
muie = Casal.Pessoa('Rita')
casal = Casal(homi, muie)

print(casal.homi.nome)
print(casal.muie.nome)

class Stack:

  class Node:
    def __init__(self, value, previous):
      self.value = value
      self.previous = previous
  
  def __init__(self):
    self.top = None
  
  def Push(self, value):
    self.top = Stack.Node(value, self.top)

  def Pop(self):
    top = self.top
    self.top = top.previous
    return top.value

  def IsEmpty(self):
    return self.top == None

stack = Stack()
stack.Push('Hey')
stack.Push('How')
stack.Push('Cow')

while not stack.IsEmpty():
  print(stack.Pop())

class Fila:
    class No:
        def __init__(self, val, next):
            self.val = val
            self.next = next

    def __init__(self):
        self.top = None
        self.last = None
    
    def IsEmpty(self):
        return self.top == None
    
    def Push(self, val):
        if self.top == None:
            self.top = Fila.No(val, None)
            self.last = self.top
        else:
            new = Fila.No(val,None)
            self.last.next = new
            self.last = new

    def Pop(self):
        top = self.top
        self.top = top.next
        return top.val

fila = Fila()
fila.Push('Hey')
fila.Push('How')
fila.Push('Cow')

#while not fila.IsEmpty():
  #print(fila.Pop())

class Grafo:
    def __init__(self, nodes):
        self.nodes = nodes
        self.v = [[]]
        for i in range(0, self.nodes):
            self.v.append([])
    
    def Inicio(self):
        return self.v[0]


    def Conecta(self, A, B):
        self.v[A].append(B)
        self.v[B].append(A)

    def Print(self):
        for i in range(0, self.nodes):
            print(self.v[i])

grafo = Grafo(6)
grafo.Conecta(0,1)
grafo.Conecta(1,2)
grafo.Conecta(1,3)
grafo.Conecta(2,4)
grafo.Conecta(3,4)
grafo.Print()
print(grafo.Inicio())

class BFS:
    def __init__(self, nodes, fila, grafo):
        self.pai = [-1] * nodes
        self.dist = [-1] * nodes
        self.fila = fila
        self.grafo = grafo

    def MenorCaminho (self, A, B):
        self.fila.Push(A)
        self.pai[A] = A 
        self.dist[A] = 0
        while not self.fila.IsEmpty():
            pop = self.fila.Pop()
            for viz in self.grafo.v[pop]:
                if self.pai[viz] == -1:
                    self.pai[viz] = pop
                    self.dist[viz] = self.dist[pop] + 1
                    self.fila.Push(viz)
        print(self.pai)
        print(self.dist)

    def Caminho(self, A, B):
        i = B
        caminho = [i]
        while self.pai[i] != A:
            caminho.append(self.pai[i])
            i = self.pai[i]
        caminho.append(A)
        print(caminho)


grafo = Grafo(6)
grafo.Conecta(0,1)
grafo.Conecta(1,2)
grafo.Conecta(1,3)
grafo.Conecta(2,4)
grafo.Conecta(3,4)
fila = Fila()
bfs = BFS(6, fila, grafo)
bfs.MenorCaminho(0,4)
bfs.Caminho(0,4)




    




