import math
from typing import Tuple, List

class TransformacionesGraficas2D:
    """
    Representa los fundamentos matemáticos de la Computación Gráfica.
    En la práctica, estas transformaciones permiten a la computadora proyectar,
    mover y animar objetos (como en videojuegos o interfaces) en la pantalla.
    """
    
    @staticmethod
    def rotar_punto(punto: Tuple[float, float], angulo_grados: float) -> Tuple[float, float]:
        """
        Rota un punto (x, y) alrededor del origen (0,0) en sentido antihorario.
        """
        x, y = punto
        # Convertir a radianes porque las funciones trigonométricas lo requieren
        angulo_rad = math.radians(angulo_grados)
        
        # Multiplicación por Matriz de Rotación Clásica:
        # [ cos(θ) -sin(θ) ] [ x ]
        # [ sin(θ)  cos(θ) ] [ y ]
        x_nueva = x * math.cos(angulo_rad) - y * math.sin(angulo_rad)
        y_nueva = x * math.sin(angulo_rad) + y * math.cos(angulo_rad)
        
        return round(x_nueva, 2), round(y_nueva, 2)

    @staticmethod
    def trasladar_punto(punto: Tuple[float, float], dx: float, dy: float) -> Tuple[float, float]:
        """Desplaza un punto en el plano cartesiano sumando deltas a sus ejes."""
        return (round(punto[0] + dx, 2), round(punto[1] + dy, 2))

    @staticmethod
    def escalar_punto(punto: Tuple[float, float], sx: float, sy: float) -> Tuple[float, float]:
        """Cambia la escala (tamaño) multiplicando las coordenadas."""
        return (round(punto[0] * sx, 2), round(punto[1] * sy, 2))

def transformar_poligono(poligono: List[Tuple[float, float]], transformacion, *args) -> List[Tuple[float, float]]:
    """Aplica una transformación geométrica a TODOS los vértices de un objeto (polígono)."""
    return [transformacion(v, *args) for v in poligono]

# --- EJEMPLO DE USO Y ANÁLISIS ---
if __name__ == "__main__":
    print("--- Gráficos por Computador: Transformaciones 2D ---\n")
    
    # Definimos un objeto simple: un triángulo mediante sus 3 vértices
    triangulo = [(0.0, 0.0), (10.0, 0.0), (5.0, 10.0)]
    print(f"Objeto original (Triángulo): {triangulo}\n")
    
    print(f"1. Rotación (90°):         {transformar_poligono(triangulo, TransformacionesGraficas2D.rotar_punto, 90)}")
    print(f"2. Traslación (x+5, y-2):  {transformar_poligono(triangulo, TransformacionesGraficas2D.trasladar_punto, 5, -2)}")
    print(f"3. Escalado (x*2, y*0.5):  {transformar_poligono(triangulo, TransformacionesGraficas2D.escalar_punto, 2.0, 0.5)}")