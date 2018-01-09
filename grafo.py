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
