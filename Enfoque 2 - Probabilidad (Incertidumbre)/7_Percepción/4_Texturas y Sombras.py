import math
from typing import List

def normalizar_vector(v: List[float]) -> List[float]:
    """
    Calcula la magnitud (longitud) de un vector y lo normaliza para que mida exactamente 1.
    Esto es un paso obligatorio en gráficos 3D antes de calcular ángulos.
    """
    magnitud = math.sqrt(sum(coord ** 2 for coord in v))
    if magnitud == 0:
        return v
    return [coord / magnitud for coord in v]

def calculo_iluminacion_lambertiana(normal_superficie: List[float], direccion_luz: List[float]) -> float:
    """
    Simula el sombreado difuso basado en la Ley de Reflexión de Lambert.
    
    En Percepción y Gráficos 3D, la intensidad de luz reflejada por una superficie mate 
    es directamente proporcional al coseno del ángulo entre:
    1. El vector Normal (N): La dirección hacia la que "apunta" la superficie.
    2. El vector de Luz (L): La dirección hacia la fuente de luz.
    
    Matemáticamente, este coseno se obtiene mediante el Producto Punto (N · L).
    """
    # 1. Aseguramos que ambos vectores estén normalizados (|N| = 1, |L| = 1)
    n_norm = normalizar_vector(normal_superficie)
    l_norm = normalizar_vector(direccion_luz)
    
    # 2. Producto Punto: Intensidad = N · L
    intensidad = sum(n * l for n, l in zip(n_norm, l_norm))
    
    # 3. La iluminación no puede ser negativa (si la luz viene por detrás de la pared, está oscura = 0)
    return max(0.0, float(intensidad))

# --- EJEMPLO DE USO Y ANÁLISIS ---
if __name__ == "__main__":
    print("--- Percepción: Sombreado y Reflexión (Ley de Lambert) ---\n")
    
    # Imaginemos el suelo plano apuntando directamente hacia arriba (Eje Y positivo) en un mundo 3D
    superficie_normal = [0.0, 1.0, 0.0]  
    print(f"Vector Normal de la Superficie (Suelo): {superficie_normal}\n")
    
    # Diferentes posiciones del "Sol"
    escenarios_luz = {
        "Mediodía (Luz directamente arriba)": [0.0, 1.0, 0.0],
        "Media Tarde (Sol a ~45 grados)":     [1.0, 1.0, 0.0],
        "Atardecer (Luz casi horizontal)":    [1.0, 0.1, 0.0],
        "Subterránea (Luz desde abajo)":      [0.0, -1.0, 0.0]
    }
    
    for descripcion, vector_luz in escenarios_luz.items():
        intensidad = calculo_iluminacion_lambertiana(superficie_normal, vector_luz)
        
        # Convertimos a porcentaje para mejor legibilidad
        print(f"Escenario: {descripcion}")
        print(f"  -> Dirección de Luz: {vector_luz}")
        print(f"  -> Intensidad Reflejada: {intensidad:.4f} ({intensidad * 100:.1f}% de luz)\n")