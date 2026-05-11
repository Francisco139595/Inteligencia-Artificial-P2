def estimar_movimiento(frame1, frame2, x, y):
    """
    Estima el desplazamiento de un píxel entre dos fotogramas consecutivos.
    Concepto básico de Flujo Óptico.
    """
    # Buscar dónde quedó el píxel (x, y) en el frame2 (vecindad simple)
    valor_buscado = frame1[x][y]
    
    mejor_dx, mejor_dy = 0, 0
    min_dif = float('inf')
    
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            dif = abs(frame2[x+dx][y+dy] - valor_buscado)
            if dif < min_dif:
                min_dif = dif
                mejor_dx, mejor_dy = dx, dy
                
    return (mejor_dx, mejor_dy)

f1 = [[0,0,0], [0,255,0], [0,0,0]]
f2 = [[0,0,0], [0,0,255], [0,0,0]] # El punto blanco se movió a la derecha
print(f"Vector de movimiento detectado: {estimar_movimiento(f1, f2, 1, 1)}")