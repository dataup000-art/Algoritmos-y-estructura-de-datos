# Colas

## Idea principal
Una cola trabaja con la regla **FIFO**: el primero que entra es el primero que sale. Es como una fila de personas.

## Operaciones y términos
- **Encolar:** agregar al final.
- **Desencolar:** retirar del frente.
- **Frente:** primer elemento.
- **Final:** último elemento.
- **`esta_vacia`:** comprueba si no hay elementos.
- **`ver_frente`:** consulta el elemento del frente.
- **`tamanio`:** puede devolver la cantidad de elementos si la implementación lleva un contador.

## Ejemplo 1: orden de atención
Si encolas `4`, `7` y `9`, salen `4`, `7` y `9`.

## Ejemplo 2: guardar la cantidad inicial
En una implementación con `self.cantidad`:
```python
def tamanio(self):
    return self.cantidad
```
Al ejecutar `n = cola.tamanio()`, `n` guarda la cantidad de elementos en ese momento. Puede servir para procesar la cantidad original mientras se desencola y se vuelve a encolar:
```python
n = cola.tamanio()
for i in range(n):
    dato = cola.desencolar()
    # Procesar el dato.
```
La acción posterior depende del enunciado.

## Para practicar
Dibuja el frente y el final después de cada operación. Sigue el orden de entrada y salida y observa cuándo cambia la cantidad.
