def ocr_por_zonas(matriz_caracter):
    """
    OCR simplificado basado en la densidad de píxeles por zonas.
    Divide el carácter en regiones y cuenta píxeles activos.
    """
    mitad = len(matriz_caracter) // 2
    zona_superior = sum(sum(fila) for fila in matriz_caracter[:mitad])
    zona_inferior = sum(sum(fila) for fila in matriz_caracter[mitad:])
    
    # Lógica simple: si hay más peso abajo, podría ser una 'L' o 'J'
    if zona_inferior > zona_superior * 2:
        return "L"
    return "Desconocido"

letra_L = [[1, 0], [1, 1]]
print(f"Carácter detectado: {ocr_por_zonas(letra_L)}")