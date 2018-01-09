class Animal:
   def __init__(self, peso):
      self.peso = peso

   def ImprimePeso(self):
      print(self.peso)


class Gato(Animal):
   def __init__(self,pesogato,miaumiau="Miau"):
      super().__init__(pesogato)
      self.tipoMiau = miaumiau

   def MiaOPeso(self):
      print("%s %s %d %s" % (self.tipoMiau, self.tipoMiau, self.peso, self.tipoMiau))

denis = Gato(190)
rita = Gato(20)

denis.ImprimePeso()
rita.ImprimePeso()

denis.MiaOPeso()






