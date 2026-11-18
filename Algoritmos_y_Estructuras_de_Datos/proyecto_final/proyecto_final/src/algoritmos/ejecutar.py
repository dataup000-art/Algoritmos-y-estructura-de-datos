

from estructuras.pila import Pila 
from algoritmos.hanoi_recursivo import hanoi 
def ejecutar(n, movimientos): 
    torres = [Pila(), Pila(), Pila()]
    
    for i in range(n,0,-1):
        torres[0].push(i)

    pasos = []
    for origen, destino in movimientos: 
        disco = torres[origen].pop()
        if not torres[destino].estavacia() and torres[destino].ver_tope() < disco: 
            raise ValueError("NO SE PUEDE PONER UN DISCO GRANDE SOBRE UNO CHICO") 
        else:
            torres[destino].push(disco)

        pasos.append({
            "disco": disco,
            "origen": origen,
            "destino": destino,
            "torres": [torres[0].listapila(), torres[1].listapila(), torres[2].listapila()]
        })

    return pasos 

if __name__ == "__main__":
    movs =[]
    hanoi(3,0,2,1, movs)
    pasos = ejecutar(3, movs)
    for p in pasos:
        print(p)
