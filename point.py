import math 
import numbers

class Point2D:
   def __init__(self, x, y):
      self.x = x
      self.y = y

   def __str__(self):
      return "( %f , %f )" %(self.x , self.y)

   def __add__(self, p):
      return Point2D(self.x + p.x, self.y + p.y)

   def __sub__(self, p):
      return Point2D(self.x - p.x, self.y - p.y)

   def tamanho(self):
      return math.sqrt((self.x**2) + (self.y**2)) 

   #nao cria um terceiro ponto +=
   def __iadd__(self, p):
      self.x += p.x
      self.y += p.y
      return self

   def MudaSinal(self):
      self.x = -self.x
      self.y = -self.y
      return self

   def __neg__(self):
      return Point2D(-self.x, -self.y)

   def __mul__(self, p):
      if isinstance(p, numbers.Number):
         return Point2D(self.x * p, self.y * p)

      elif isinstance(p, Point2D):
         return ((self.x * p.x) + (self.y * p.y))


   #def __rmul__(self, p):
      #return Point2D(self.x * p, self.y * p)

   __rmul__ = __mul__




ponto = Point2D(1, 1)
#vai usar o metodo string
print(ponto)
print("meu ponto é %s" %(ponto))
print(ponto + Point2D(1, 1))
print(ponto - Point2D(1, 1))
print(ponto.tamanho())
ponto += Point2D(4,5)
print(ponto)
#usa o neg
print(-ponto)


ponto2 = Point2D(1, 1)
#usa rmul, objeto da classe aparece so do lado direito
ponto3 = 2 * ponto2
#usa mul
ponto3 = -ponto2 * 2  
print(ponto3)
print(-ponto2 * ponto3)

def TextoPonto(p):
   return " x: %.2f , y: %.2f " %(p.x, p.y)

Point2D.__str__ = TextoPonto
print(ponto3)
#print(TextoPonto(ponto3))


