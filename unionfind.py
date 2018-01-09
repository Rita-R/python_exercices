import numbers

class Pessoa:
  def __init__(self, idade):
    self.idade = idade
    self.maioridade = idade >= 18
  
  def FazAniversario(self):
    self.idade += 1

Denis = Pessoa(26)
#print(Denis.maioridade)
Denis.FazAniversario()
#print(Denis.idade)

v = [-1] * 10
#print(v)

#retorna o representante do conjunto de a
#versao recursiva
def Find(vector,a):
    if vector[a] < 0:
        return a
    else:
        v =  Find(vector, vector[a])
        vector[a] = v
        return v
    

# v = [-1,-4, 1, 2, 2]
# print(Find(v,4))
# print(v)

#retorna true se uniu b no conj de a, false se ja era um conj so
def Union(vector,a,b):
    if Find(vector,a) == Find(vector,b):
        return False
    else:
        finda = Find(vector,a)
        findb = Find(vector,b)
        if vector[finda] <= vector[findb]:
            vector[finda] += vector[findb]
            vector[findb] = finda
        else:
            vector[findb] += vector[finda]
            vector[finda] = findb
        return True

# v = [-2, 0, -2, 2]
# print(Union(v,1,3))
# print(v)

#retorna o numero de conjuntos no vetor
def Nsets(vector):
    nsets = 0
    for i in range(0, len(vector)):
        if vector[i] < 0:
            nsets += 1
    return nsets


# v = [-2, 0, -2, 2]
# print(Nsets(v))

#define quantos elementos há no conjunto de a
def SizeOf(vector, a):
    finda = Find(vector,a)
    numelem = abs(vector[finda])
    return numelem

# v = [-1,-4, 1, 2, 2]
# print(SizeOf(v,2))

#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------

class UnionFind:
    def __init__(self, n):
        self.v = [-1] * n
        self.nconj = n
  
    def Find(self,a):
        vector = self.v
        if vector[a] < 0:
            return a
        else:
            x =  Find(vector, vector[a])
            vector[a] = x
            return x

    def Union(self,a,b):
        vector = self.v
        if Find(vector,a) == Find(vector,b):
            return False
        else:
            self.nconj -= 1
            finda = Find(vector,a)
            findb = Find(vector,b)
            if vector[finda] <= vector[findb]:
                vector[finda] += vector[findb]
                vector[findb] = finda
            else:
                vector[findb] += vector[finda]
                vector[finda] = findb
            return True
    
    def NSets(self):
        return self.nconj

    #retora o tamanho
    def __len__(self):
        return self.nconj

    #metodo é chamada que nem função
    def __call__(self):
        return self.nconj


    def SizeOf(self, a):
        vector = self.v
        finda = Find(vector,a)
        numelem = abs(vector[finda])
        return numelem


# Denis = UnionFind(6)
# print(Denis.v)
# print(Denis.nconj)
# Denis.Union(1,2)
# print(Denis.v)
# print(Denis.nconj)
# print(Denis.SizeOf(1))
# print(Denis.Find(2))
# print(len(Denis))
# print(Denis())

#--------------------------------------
#--------------------------------------
#--------------------------------------

#dicionario

# d = {}
# d["chave"] = 20
# d["chave1"] = 21
# d["chave2"] = 22
# print(d)
# print(d["chave2"])

# if "chave" in d:
#     print("yes")

class Uid:
    def __init__(self):
        self.d = {}
        self.chave = -1
        self.v = []

    # def AddElemento(self, elem,chave):
    #     self.d[elem] = chave

    def Imprime(self):
        print(self.d)

    def GetId(self, string):
        if string in self.d:
            return self.d[string]
        else:
            self.chave = self.chave + 1
            self.d[string] = self.chave
            self.v.append(string)
            return self.d[string]

    def RecoverName(self, num):
        return self.v[num]
    
    def __call__(self, elem):
        if isinstance(elem, numbers.Number):
            return self.RecoverName(elem)
        else:
            return self.GetId(elem)


# ui1 = Uid()
# print(ui1.GetId("Rita"))
# print(ui1.GetId("Denis"))
# print(ui1.v)
# print(ui1.RecoverName(0))
# print(ui1.RecoverName(1))
# ui1.Imprime()
# print(ui1("Rose"))
# ui1.Imprime()

class GroupNetwork:
    def __init__(self, npessoas):
        self.uf = UnionFind(npessoas)
        self.uid = Uid()

    #dado o nome das pessoas, unir os grupos delas
    def Join (self, string1, string2):
        id1 = self.uid(string1)
        id2 = self.uid(string2)
        self.uf.Union(id1,id2)

    # dado duas pessoas, ver se estao conectadas, retorna bool
    def AreConnected(self, string1, string2):
        id1 = self.uid(string1)
        id2 = self.uid(string2)
        find1 = self.uf.Find(id1)
        find2 = self.uf.Find(id2)
        return find1 == find2


# sn = GroupNetwork(5)
# sn.Join("Rita", "Denis")
# print(sn.AreConnected("Rita", "Rose"))
# sn.Join("Rose", "Denis")
# print(sn.AreConnected("Rita", "Rose"))












