import math
from typing import List

def svm_kernel_trick_rbf(x1: List[float], x2: List[float], gamma: float = 0.5) -> float:
    """
    Máquinas de Vectores de Soporte (SVM) - Truco del Núcleo (Kernel Trick).
    
    Las SVM buscan un hiperplano que separe las clases con el margen máximo.
    Cuando los datos NO son linealmente separables, el 'Kernel Trick' calcula la 
    similitud entre dos puntos proyectándolos implícitamente a una dimensión 
    superior (incluso infinita) donde SÍ pueden ser separados por un hiperplano.
    """
    if len(x1) != len(x2):
        raise ValueError("Los vectores x1 y x2 deben tener la misma dimensión.")
        
    # Calculamos la distancia euclidiana al cuadrado entre los vectores
    distancia_sq = sum((a - b)**2 for a, b in zip(x1, x2))
    
    # El Kernel RBF (Gaussiano) devuelve un valor entre 0 y 1.
    # 1.0 significa que los puntos son idénticos, 0.0 significa que están muy lejos.
    similitud = math.exp(-gamma * distancia_sq)
    return similitud

print("--- Simulación: Máquinas de Vectores de Soporte (Kernel RBF) ---")

# Puntos de prueba 2D
punto_A = [1.0, 2.0]
punto_B = [1.5, 2.0] # Muy cercano a A
punto_C = [8.0, 9.0] # Muy lejano a A

print(f"Similitud entre A{punto_A} y B{punto_B} (Cercanos): {svm_kernel_trick_rbf(punto_A, punto_B, gamma=1.0):.4f}")
print(f"Similitud entre A{punto_A} y C{punto_C} (Lejanos):  {svm_kernel_trick_rbf(punto_A, punto_C, gamma=1.0):.4f}")
print("\n-> Conclusión: El Kernel transforma distancias en similitudes en un espacio superior, permitiendo separar clases con fronteras curvas.")
