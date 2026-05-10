import math

def sigmoide(x: float) -> float:
    """
    Función de activación Sigmoide.
    Fórmula: f(x) = 1 / (1 + e^-x)
    Escala cualquier valor real a un rango entre 0 y 1. 
    Es ideal para modelos que necesitan predecir probabilidades.
    """
    return 1 / (1 + math.exp(-x))

def relu(x: float) -> float:
    """
    Función de activación ReLU (Rectified Linear Unit).
    Fórmula: f(x) = max(0, x)
    Deja pasar los valores positivos intactos y bloquea (convierte en 0) los negativos.
    Ayuda a mitigar el problema del desvanecimiento del gradiente en redes profundas.
    """
    return max(0.0, float(x))

def tanh(x: float) -> float:
    """
    Función de activación Tangente Hiperbólica.
    Fórmula: f(x) = (e^x - e^-x) / (e^x + e^-x)
    Escala los valores a un rango entre -1 y 1.
    A menudo funciona mejor que la sigmoide en capas ocultas porque centra los datos en 0.
    """
    return math.tanh(x)

def paso_unitario(x: float) -> int:
    """
    Función de activación de Paso Unitario (Escalón o Heaviside).
    Fórmula: f(x) = 1 si x >= 0, de lo contrario 0.
    Es una función de umbral simple, históricamente usada en el Perceptrón original.
    """
    return 1 if x >= 0 else 0

# --- EJEMPLO DE USO Y ANÁLISIS ---
# Evaluaremos cómo se comporta cada función ante diferentes tipos de entradas
valores_prueba = [-2.0, 0.0, 1.5]

print("--- Análisis de Funciones de Activación ---")
for val in valores_prueba:
    print(f"\nEntrada (x) = {val}")
    print(f"  Sigmoide:       {sigmoide(val):.4f}  (Mapeado entre 0 y 1)")
    print(f"  ReLU:           {relu(val):.4f}  (Cero si es negativo, lineal si es positivo)")
    print(f"  Tanh:           {tanh(val):.4f}  (Mapeado entre -1 y 1)")
    print(f"  Paso Unitario:  {paso_unitario(val)}       (0 o 1 estricto)")