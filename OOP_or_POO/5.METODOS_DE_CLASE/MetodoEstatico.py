'''Metodos Estaticos: no reciben argumentos adicionales'''
class Pizza:
    def __init__(self,topping) -> None:
        self.topping = topping
    #metodo estatico
    def mostrar(self):
        print(self.topping)
    @staticmethod
    def val_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

ingredients = ["cheese","onions","spam","pineapple"]
if all(Pizza.val_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)
pizza.mostrar()