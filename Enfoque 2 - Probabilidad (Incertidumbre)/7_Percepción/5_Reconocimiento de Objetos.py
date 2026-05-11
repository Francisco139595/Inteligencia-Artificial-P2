from typing import List, Tuple

def template_matching_deslizante(imagen: List[List[int]], template: List[List[int]], umbral: int = 50) -> Tuple[bool, Tuple[int, int], int]:
    """
    Algoritmo de Reconocimiento de Objetos usando "Template Matching" con Ventana Deslizante.
    Utiliza el método de Suma de Diferencias Absolutas (SAD - Sum of Absolute Differences).
    
    En lugar de comparar matrices del mismo tamaño, este algoritmo desliza el 'template' 
    sobre toda la 'imagen' para encontrar en qué coordenadas (x, y) encaja mejor.
    """
    filas_img, col_img = len(imagen), len(imagen[0])
    filas_tpl, col_tpl = len(template), len(template[0])
    
    # Validación matemática: el patrón no puede ser más grande que el lienzo
    if filas_tpl > filas_img or col_tpl > col_img:
        raise ValueError("El template no puede ser más grande que la imagen.")
        
    mejor_error = float('inf')
    mejor_posicion = (-1, -1)
    
    # Deslizamos la ventana por toda la imagen.
    # Restamos el tamaño del template a los límites para no leer fuera de la imagen (Out of Bounds).
    for y in range(filas_img - filas_tpl + 1):
        for x in range(col_img - col_tpl + 1):
            
            # Calculamos el error SAD para la región actual de tamaño igual al template
            error_actual = 0
            for i in range(filas_tpl):
                for j in range(col_tpl):
                    pixel_imagen = imagen[y + i][x + j]
                    pixel_template = template[i][j]
                    error_actual += abs(pixel_imagen - pixel_template)
                    
            # Si este encaje es mejor (menor error) que los anteriores, lo guardamos
            if error_actual < mejor_error:
                mejor_error = error_actual
                mejor_posicion = (x, y)
                
    # Consideramos que el objeto fue reconocido si el error mínimo encontrado es menor al umbral
    objeto_reconocido = mejor_error <= umbral
    return objeto_reconocido, mejor_posicion, mejor_error

# --- EJEMPLO DE USO Y ANÁLISIS ---
if __name__ == "__main__":
    print("--- Percepción: Reconocimiento de Objetos (Template Matching) ---\n")
    
    # Simulamos una imagen grande (5x5). Píxeles en '10' representan un fondo oscuro.
    # El "objeto" está escondido empezando en las coordenadas (x=2, y=1).
    imagen_busqueda = [
        [10, 10,  10,  10, 10],
        [10, 10, 255,   0, 10],
        [10, 10,   0, 255, 10],
        [10, 10,  10,  10, 10],
        [10, 10,  10,  10, 10]
    ]
    
    # El patrón visual que queremos encontrar (2x2)
    patron = [
        [255,   0],
        [  0, 255]
    ]
    
    print("Buscando patrón:")
    for fila in patron: print(f"  {fila}")
        
    encontrado, coordenadas, error_minimo = template_matching_deslizante(imagen_busqueda, patron, umbral=20)
    
    if encontrado:
        print(f"\n[ÉXITO] Objeto reconocido en la coordenada X={coordenadas[0]}, Y={coordenadas[1]}.")
        print(f"Error mínimo encontrado (SAD): {error_minimo}")
    else:
        print(f"\n[FALLO] Objeto no encontrado. Mejor coincidencia tuvo un error de: {error_minimo}")