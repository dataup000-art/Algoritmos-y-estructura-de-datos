
from estructuras.pila import Pila 


def hanoi_iterativo(n, origen, destino, auxiliar):
    movimientos = []
    tareas = Pila() 

    tareas.push(("resolver", n, origen, destino, auxiliar))


    while not tareas.estavacia(): 
        tarea = tareas.pop()

        if tarea[0] == "mover":
            movimientos.append((tarea[1], tarea[2]))
        else:
            _, k, o, d, a = tarea 
            if k ==0: 
                continue 
            tareas.push(("resolver", k-1, a, d, o))
            tareas.push(("mover",o, d))
            tareas.push(("resolver", k-1, o, a, d))


    return movimientos 


if __name__ == "__main__":
    print(hanoi_iterativo(2,0,2,1))
    print(hanoi_iterativo(3,0,2,1))