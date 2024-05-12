#@classmethod
#calculo de area con metodo de clase
class Rectangle:
    def __init__(self,w,h) -> None:
        self.width = w
        self.height = h
    
    def area(self):
        return self.width*self.height
    #metodo de clase
    @classmethod
    def square(cls,length,lg):
        return cls(length,lg)

w = int(input("Ingrese el ancho: "))
h = int(input("ingrese la altura: "))    
square = Rectangle.square(w,h)
print(square.area())