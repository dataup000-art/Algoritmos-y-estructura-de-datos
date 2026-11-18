

class Nodo: 

    def __init__(self, valor): 
        self.valor = valor 
        self.siguiente = None 


class Pila: 

    def __init__(self):
        self.tope = None 
        self.contador = 0 

    def push(self,valor):
        n1 = Nodo(valor)
        n1.siguiente = self.tope 
        self.tope = n1 
        self.contador += 1 
        
    def pop(self):
        if self.estavacia() == False:
            q = self.tope 
            valor = q.valor 
            self.tope = self.tope.siguiente
            self.contador -=1 
            return valor 
        else:
            raise IndexError("pila vacia")

    def estavacia(self): 
        return self.tope is None 

    def listapila(self):
        q = self.tope
        L = []
        R= [] 
        while q is not None:
           L.append(q.valor)
           q = q.siguiente

        for i in range(len(L)-1, -1, -1):
            R.append(L[i]) 

        return R 
    def tamaño(self):
        return self.contador 
    def ver_tope(self):
        if self.estavacia() == False:
            return self.tope.valor 
        else:
            raise IndexError("pila vacia")

    
