
class HeapTree:
    def __init__(self):
        self.v = []
        self.n = 0

    def Insere(self,val):
        n = self.n
        self.v.append(val)
        pai = (int)((self.n - 1)/2)
        while pai >= 0:
            if self.v[n] < self.v[pai]:
                (self.v[pai], self.v[n]) = (self.v[n], self.v[pai])
                n = pai
                pai = (int)((pai - 1)/2)
            else:
                break
        self.n = self.n + 1

    def OlhaTopo(self):
        return self.v[0]

    def ImprimeHeap(self):
        print(self.v)

    def RemoveTopo(self):
        pai = 0
        (self.v[pai], self.v[self.n-1]) = (self.v[self.n-1], self.v[pai])
        self.v.pop()
        fdir = (2 * pai) + 2
        fesq = (2 * pai) + 1
        while fesq <= self.n-2:
            if fdir <= self.n-2:
                if self.v[fesq] < self.v[fdir] and self.v[fesq] < self.v[pai]:
                    (self.v[fesq], self.v[pai]) = (self.v[pai], self.v[fesq])
                    pai = fesq
                elif self.v[fdir] < self.v[fesq] and self.v[fdir] < self.v[pai]:
                    (self.v[fdir], self.v[pai]) = (self.v[pai], self.v[fdir])
                    pai = fdir
                else: #quando o pai ja eh menor que os filhos
                    break
            else:
                if self.v[fesq] < self.v[pai]:
                    (self.v[fesq], self.v[pai]) = (self.v[pai], self.v[fesq])
                    pai = fesq
                else: #quando o pai ja eh menor que os filhos
                    break
            fesq = (2 * pai) + 1
            fdir = (2 * pai) + 2
        self.n = self.n - 1

heap = HeapTree()
heap.ImprimeHeap()
heap.Insere(32)
heap.ImprimeHeap()
heap.Insere(18)
heap.ImprimeHeap()
heap.Insere(10)
heap.ImprimeHeap()
heap.Insere(9)
heap.ImprimeHeap()
heap.Insere(7)
heap.ImprimeHeap()
heap.Insere(1)
heap.ImprimeHeap()
heap.Insere(5)
heap.ImprimeHeap()
heap.Insere(12)
heap.ImprimeHeap()
heap.Insere(13)
heap.ImprimeHeap()
heap.Insere(17)
heap.ImprimeHeap()

heap.RemoveTopo()
heap.ImprimeHeap()
heap.Insere(1)
heap.ImprimeHeap()
print("-----------")
heap.RemoveTopo()
heap.ImprimeHeap()
print("-----------")
heap.Insere(2)
heap.ImprimeHeap()
print("-----------")
heap.RemoveTopo()
heap.ImprimeHeap()
print("-----------")
heap.RemoveTopo()
heap.ImprimeHeap()