
class Shape:
   def __init__(self):
      raise Exception("Do not instantiate a shape!")

   def Area(self):
      raise Exception("Not implemented in the super class")

   def PrintArea(self):
      print(self.Area())

class Rectangle(Shape):
   def __init__(self, base, height):
      self.base = base
      self.height = height

   def Area(self):
      return self.base * self.height

class Square(Rectangle):
   def __init__(self, side):
      super().__init__(side, side)

class Circle(Shape):
   def __init__(self, radius):
      self.radius = radius

   def Area(self):
      return 3.14159 * self.radius * self.radius

r = Rectangle(3, 4)
print(r.Area())

s = Square(5)
print(s.Area())

c = Circle(3)
print(c.Area())

print("----")
print(isinstance(r, Rectangle))
print(isinstance(s, Rectangle))
print(isinstance(c, Rectangle))
print("----")
print(isinstance(r, Square))
print(isinstance(s, Square))
print(isinstance(c, Square))
print("----")
print(isinstance(r, Circle))
print(isinstance(s, Circle))
print(isinstance(c, Circle))
print("----")
print(isinstance(r, Shape))
print(isinstance(s, Shape))
print(isinstance(c, Shape))


def TotalArea(l):
   a = 0
   for s in l:
      if not isinstance(s, Shape):
         raise Exception("TotalArea requires a list of shapes!")
      a += s.Area()
   return a

print(TotalArea([r, s, c]))

r.PrintArea()


class C1:
   def __init__(self):
      pass

   def HelloWorld(self):
      print("Hello from C1")

   def Boom(self):
      print("Boom!")

   def Vrau(self):
      print("Vrau")

class C2(C1):
   def __init__(self):
      pass

   def HelloWorld(self):
      super().HelloWorld()
      super().Boom()
      self.Boom()
      print("Hello from C2")

   def HelloWorld2(self):
      super().HelloWorld()

   def Boom2(self):
      self.Boom()


c = C2()
c.Boom()
c.HelloWorld()
c.Vrau()

