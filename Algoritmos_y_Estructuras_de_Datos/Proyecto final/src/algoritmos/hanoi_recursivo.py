

def hanoi(n, origen, destino, auxiliar, movimientos): 

    if n == 0: return 
    else: 

        hanoi(n-1, origen, auxiliar, destino, movimientos)
        movimientos.append((origen,destino))
        hanoi(n-1, auxiliar, destino, origen, movimientos)


if __name__ == "__main__":
    movs = []
    hanoi(3, 0, 2, 1, movs)
    print(movs)
