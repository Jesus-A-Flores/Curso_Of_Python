'''Estamos trabajando en un juego. Nuestra clase Player tiene
   atributos name y privados __lives.
   El metodo hit() deberia disminuir las vidas del jugador en 1
   En caso de que las vidas sean igual a 0, deberia mostrar "Game Over"
   Completa el metodo hit() para que el programa funcione como se espera'''
class Player:
    __a = 7
    def __init__(self,name,lives):
        self.name = name
        self.__lives = lives
    def hit(self):
        #my code
        self.__lives = self.__lives-1
        if self.__lives == 0:
            print("Game Over")
player = Player("Jesus",4)
player.hit()
player.hit()
player.hit()
player.hit()
print(Player._Player__a) #para acceder a un atributo privado desde fuera de la clase