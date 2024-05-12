'''METODOS MAGICOS PARA OPERADORES COMUNES
    1. __sub__ -> para -
    2. __mul__ -> para *
    3. __truediv__ -> para /
    4. __floordriv__ -> para //
    5. __mod__ -> para %
    6. __pow__ -> para **
    7. __and__ -> para &
    8. __or__ -> para |
    9. __xor__ -> para ^
    10. __add__ para +'''
'''METODOS MAGICOS PARA COMPARACION
    1. __lt__ para <
    2. __le__ para <=
    3. __eq__ para ==
    4. __ne__ para !=
    5. __gt__ para >
    5. __ge__ par >=
    '''
'''OTROS METODOS MAGICOS
    1. __len__ para len()
    2. __getitem__ para indexar
    3. __setitem__ para para asignar a valores indexados
    4. __delitem__ para eliminar valores indexados
    5. __iter__ para iterar sobre objetos como un bucle for
    5. __contains__ para in
'''
class SpecialString:
    def __init__(self,cont): #metodo magico para crear una instancia
        self.cont = cont
    
    def __truediv__(self,other):
        line = '=' * len(other.cont)
        return '\n'.join([self.cont,line,other.cont])
    
    def __mul__(self,other):
        line = '=' * len(other.cont)
        return '\n'.join([self.cont,line,other.cont])
spam = SpecialString('spam')
hello = SpecialString("Hello world")
nose = SpecialString("nose")
print(f"{spam/hello}\n{spam*nose}")
