def heuristica_manhattan(pos_actual, pos_objetivo):
    """
    Calcula la distancia de Manhattan entre dos puntos (x, y).
    Útil para problemas de movimiento en cuadrículas.
    """
    x1, y1 = pos_actual
    x2, y2 = pos_objetivo
    return abs(x1 - x2) + abs(y1 - y2)

# Ejemplo de uso
print(f"Costo estimado: {heuristica_manhattan((0,0), (3,3))}")