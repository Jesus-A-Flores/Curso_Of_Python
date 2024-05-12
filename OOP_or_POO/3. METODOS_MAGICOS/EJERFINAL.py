'''Sobrecarga de operadores
    Estamos mejorando nuestra aplicacion de dibujo.
    Nuestra aplicacion necesita soportar la adicion
    y comparacion de dos objetos Shape.
    Agregar los metodos correspondientes para habilitar la adiccion +
    y la comparacion utilizando el operados mayor que > para la clase Shape.
    
    La adicion deberia devolver un nuevo objeto con la suma de los anchos 
    y las alturas de los operandos, mientras que la comparacion deberia devolber
    el resultado de comparar las areas de los objetos.'''
class Shape:
    def __init__(self,w,h): #inicializacion de una instancia
        self.width = w
        self.height = h
    
    def area(self): #calcula el area
        return self.width*self.height
    #My code
    #metodo magico +
    def __add__(self,other):
        #retorna un nuevo objeto con la suma de altos y anchos
        return Shape(self.width+other.width,self.height+other.height)
    #metodo magico >
    def __gt__(self,other):
        return self.area() > other.area()
w1 = int(input())
h1 = int(input())
w2 = int(input())
h2 = int(input())

s1 = Shape(w1,h1) #primer objeto
s2 = Shape(w2,h2) #segundo objeto
result = s1 + s2 #objeto resultado

print(result.area())
print(s1 > s2) #compara el area de cada objeto