from typing import List

def aplicar_filtro_media(imagen: List[List[int]]) -> List[List[int]]:
    """
    Aplica un filtro de media (Mean Filter / Blur) a TODA la imagen.
    
    En Visión Computacional, esto es una forma de "Convolución Espacial".
    Actúa como un filtro de paso-bajo: permite pasar las frecuencias bajas 
    (áreas de color suave) y atenúa las frecuencias altas (ruido y bordes abruptos).
    
    Utiliza un "Kernel" (ventana o máscara) implícito de 3x3.
    """
    filas = len(imagen)
    columnas = len(imagen[0]) if filas > 0 else 0
    
    # IMPORTANTE: Creamos un "lienzo" en blanco para guardar el resultado.
    # En la convolución, NUNCA debes sobreescribir la imagen original mientras 
    # la recorres, o los cálculos siguientes usarán píxeles ya modificados/contaminados.
    imagen_filtrada = [[0 for _ in range(columnas)] for _ in range(filas)]
    
    # Iteramos sobre cada píxel de la imagen original (x = fila, y = columna)
    for x in range(filas):
        for y in range(columnas):
            suma = 0
            elementos_validos = 0
            
            # Desplazamos nuestra ventana "Kernel" de 3x3 centrada en el píxel (x, y).
            # 'i' y 'j' toman valores -1, 0, 1 para explorar los 8 vecinos y el centro.
            for i in range(-1, 2):
                for j in range(-1, 2):
                    nx, ny = x + i, y + j
                    
                    # Manejo de Bordes (Boundary Condition):
                    # Si el píxel está en la orilla, el kernel intentará leer fuera de la matriz.
                    # Verificamos que nx y ny existan dentro de los límites de la imagen.
                    if 0 <= nx < filas and 0 <= ny < columnas:
                        suma += imagen[nx][ny]
                        elementos_validos += 1
                        
            # El nuevo valor es el promedio aritmético de la vecindad válida.
            # Si es un píxel central, se divide entre 9. En una esquina, se divide entre 4.
            imagen_filtrada[x][y] = suma // elementos_validos
            
    return imagen_filtrada

# --- EJEMPLO DE USO Y ANÁLISIS ---
if __name__ == "__main__":
    # Simulamos una imagen de 5x5 gris oscuro (valor 10)
    img = [[10 for _ in range(5)] for _ in range(5)]
    img[2][2] = 100 # Píxel ruidoso muy brillante (Ruido "Sal") en el centro
    img[0][4] = 90  # Otro píxel ruidoso en una esquina (para probar el límite de bordes)

    print("--- Preprocesado: Filtro de Media (Suavizado/Blur) ---\n")
    print("Imagen Original (Con ruido):")
    for fila in img: print([f"{p:3d}" for p in fila])
        
    print("\nImagen Filtrada:")
    img_suavizada = aplicar_filtro_media(img)
    for fila in img_suavizada: print([f"{p:3d}" for p in fila])
    
    print(f"\nAnálisis: El ruido central bajó de 100 a {img_suavizada[2][2]}.")
    print("Al promediar, el filtro reparte el 'brillo' anómalo entre los vecinos.")
