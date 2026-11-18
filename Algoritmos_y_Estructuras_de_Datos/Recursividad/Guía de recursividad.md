# Recursividad

## Idea principal
Una función recursiva se llama a sí misma para resolver una versión más pequeña del problema.

Toda recursión tiene:
- **Caso base:** condición que detiene las llamadas.
- **Caso recursivo:** reduce el problema y vuelve a llamar a la función.

## Trabajar con vectores
Para un vector `v`:
- `v[0]`: primer elemento.
- `v[1:]`: todos menos el primero.
- `v[1:-1]`: todos menos el primero y el último.
- `len(v)`: cantidad de elementos.

## Ejemplo 1: sumar un vector
```python
def suma_vector(v):
    if len(v) == 0:
        return 0
    else:
        return v[0] + suma_vector(v[1:])
```
Caso base: el vector vacío devuelve `0`. Caso recursivo: suma el primer elemento con la suma del resto.

## Ejemplo 2: sumar retirando los extremos
```python
def suma_figura(v):
    if len(v) == 0:
        return 0
    else:
        return suma_vector(v) + suma_figura(v[1:-1])
```
En cada llamada se suma el vector actual y se continúa con el vector sin el primer y el último elemento.

## Para practicar
Anota el argumento de cada llamada hasta llegar al caso base. Después sigue cómo se devuelven los resultados.
