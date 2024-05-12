class Queue:
    def __init__(self,contents): #inicializacion de instancia
        self._hiddenlist = list(contents)
    
    def push(self,vaule):#insertar datos a la cola
        self._hiddenlist.insert(0,vaule)
    def pop(self): #eliminar datos de la cola
        return self._hiddenlist.pop(-1)
    
    def __repr__(self): #Sepresentacion de cadena de la instancia
        return "Queue({})".format(self._hiddenlist)
queue = Queue([4,7,8])
print(queue)
queue.push(6)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)