# Especificación – Torres de Hanói Animadas en 3D (Pilas + Recursividad)

## 1. Problema
Resolver las Torres de Hanói para N discos usando pilas y recursividad, y animar la solución en Blender (bpy), mostrando en pantalla el contenido de las tres pilas en cada movimiento.

## 2. Entradas y salidas
| | Detalle |
|---|---|
| **Entrada** | N = número de discos. Animación: N = 5 (31 movimientos). Métricas: N = 1 … 20. |
| **Salida 1** | Secuencia de movimientos `(disco, origen, destino)` – exactamente 2ⁿ − 1. |
| **Salida 2** | Registro de pasos: estado de las 3 pilas después de cada movimiento (interfaz entre algoritmo y Blender). |
| **Salida 3** | CSV de métricas + gráficos para el informe. |
| **Salida 4** | Escena `.blend` y video MP4 (30–90 s). |

## 3. Estructuras de datos
- **Clase `Pila` propia**: push, pop, peek, esta_vacia, tamaño.
- **3 torres = 3 instancias de `Pila`** (A, B, C).
- **Invariante**: nunca se apila un disco mayor sobre uno menor → si ocurre, error (sirve como prueba de corrección).

## 4. Algoritmos (dos versiones a comparar)
- **A. Recursivo**: caso base n = 0; mover n−1 a auxiliar, mover disco n a destino, mover n−1 a destino.
- **B. Iterativo con pila explícita**: simula la recursión guardando "marcos" (n, origen, destino, auxiliar) en una `Pila` propia, sin llamadas recursivas.
- **Verificación**: ambas versiones deben producir **la misma secuencia** de movimientos.

## 5. Métricas
| Métrica | Cómo se obtiene |
|---|---|
| Número de movimientos | Contar y verificar = 2ⁿ − 1 para N = 1 … 20 |
| Tiempo de ejecución | `timeit`, recursivo vs. iterativo, N = 1 … 20 |
| Memoria | Profundidad máx. de recursión (= n) vs. tamaño máx. de la pila explícita |
| Complejidad | Tiempo O(2ⁿ), espacio O(n) – contrastar con la curva medida |

Columnas del CSV: `n, movimientos, tiempo_recursivo_s, tiempo_iterativo_s, prof_max_recursion, tam_max_pila`.

## 6. Escena en Blender
- **Objetos**: base, 3 postes, N discos (cilindros de radio decreciente, un color por disco en degradado).
- **Movimiento de cada disco en 3 fases**: subir → desplazarse → bajar.
- **Texto en pantalla**: "Movimiento k de 31" y el contenido de las pilas, p. ej. `A [5, 4, 3]  B [2]  C [1]`.
- **Resaltado**: el disco en movimiento se ilumina (material emisivo).
- **Cámara** fija, ligeramente elevada, con las 3 torres en cuadro.
- **Decisión técnica**: el texto cambia en cada movimiento → se crea un objeto de texto por estado y se alterna su visibilidad con keyframes (funciona bien al renderizar, sin depender de handlers).

## 7. Guion del video (24 fps, ~70 s)
| Tramo | Duración |
|---|---|
| Título + N = 5, 2⁵ − 1 = 31 movimientos | ~3 s |
| 31 movimientos × ~2 s | ~62 s |
| Cierre: resumen de métricas | ~4 s |

## 8. Pruebas
- N = 1, 2, 3 verificados a mano (1, 3, 7 movimientos).
- Invariante de tamaño nunca violado.
- Estado final: A y B vacías, C = [N … 1].
- Secuencia recursiva == secuencia iterativa para N = 1 … 20.

## 9. Extras opcionales (para destacar)
- Visualizar la pila de llamadas recursivas como una cuarta "torre" lateral que crece y se vacía.
- Comparar N = 3, 4, 5 en un mismo video.
- Tercera versión iterativa clásica (por paridad) en las métricas.

## 10. Fuera de alcance
- Más de 3 torres (variante de Reve).
- Interacción en tiempo real; todo se genera por script.

## 11. Pendiente de definir
- Integrantes del grupo y reparto de tareas.
- Experiencia con Blender del grupo.
- Fecha límite de entrega.
