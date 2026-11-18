# Listas enlazadas

## Conceptos básicos
- **Nodo:** una cajita que guarda un valor y una flecha al siguiente nodo.
- **`valor`:** dato almacenado.
- **`flecha`:** indica cuál es el siguiente nodo.
- **`listaR`:** señala al primer nodo.
- **`None`:** indica que no hay siguiente nodo; marca el final.

## Ejemplo 1: insertar al inicio
```python
n1 = Nodo(valor)
n1.flecha = self.listaR
self.listaR = n1
```
La secuencia es crear el nodo, conectar su flecha con el primer nodo actual y hacer que `listaR` señale al nuevo nodo.

## Ejemplo 2: recorrer y mostrar
```python
q = self.listaR
while q is not None:
    print(q.valor)
    q = q.flecha
```
`q` empieza en el primer nodo. Mientras señale a un nodo, se muestra su valor y luego avanza. Al llegar a `None`, termina. Se usa `q` para recorrer sin modificar `listaR`.

Si la lista es `10 → 20 → 30 → None`, se muestran 10, 20 y 30, en ese orden.

## Para practicar
Dibuja las cajitas y flechas, sigue el valor de `q` en cada paso y comprueba qué ocurre si `listaR is None`.
