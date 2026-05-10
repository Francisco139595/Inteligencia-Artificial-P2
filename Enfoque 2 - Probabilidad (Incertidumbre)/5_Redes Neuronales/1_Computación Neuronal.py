import math

# La computación neuronal imita el procesamiento distribuido del cerebro.
# Cada unidad (neurona) recibe entradas, las procesa y emite una señal.

def funcion_activacion_sigmoide(z):
    """
    Función de activación Sigmoide.
    Transforma el valor de la suma ponderada (z) a un rango entre 0 y 1.
    Es útil para representar probabilidades o decisiones suaves.
    """
    return 1 / (1 + math.exp(-z))

def funcion_activacion_relu(z):
    """
    Función de activación ReLU (Rectified Linear Unit).
    Devuelve z si es positivo, y 0 si es negativo.
    Es la función más utilizada en las redes neuronales profundas modernas.
    """
    return max(0.0, z)

def modelo_neuronal_basico(entradas, pesos, sesgo, funcion_activacion="relu"):
    """
    Representa el cálculo fundamental de una neurona matemática:
    1. Suma ponderada de las entradas (z).
    2. Aplicación de una función de activación para generar la salida final (a).
    """
    # Validamos que cada entrada tenga su peso correspondiente
    if len(entradas) != len(pesos):
        raise ValueError("La cantidad de entradas debe ser igual a la cantidad de pesos.")

    # Paso 1: Cálculo de la suma ponderada (z = Σ (w_i * x_i) + b)
    # Aquí se integra la información recibida multiplicada por su importancia (peso).
    suma_ponderada = sum(x * w for x, w in zip(entradas, pesos)) + sesgo

    # Paso 2: Aplicación de la función de activación
    # Esto determina si la neurona "se enciende" y con qué intensidad emite la señal.
    if funcion_activacion == "sigmoide":
        salida = funcion_activacion_sigmoide(suma_ponderada)
    elif funcion_activacion == "relu":
        salida = funcion_activacion_relu(suma_ponderada)
    else:
        salida = suma_ponderada # Salida lineal si no se reconoce la función
        
    return suma_ponderada, salida

# --- EJEMPLO DE USO Y PRUEBA ---
entradas = [1.0, 0.5, -1.2]
pesos = [0.2, 0.8, 0.5]
sesgo = 0.1

# Ejecutamos el modelo neuronal usando la función de activación ReLU
z, activacion = modelo_neuronal_basico(entradas, pesos, sesgo, funcion_activacion="relu")

# Mostramos los resultados con explicaciones detalladas
print("--- Resultados del Modelo Neuronal Ampliado ---")
print(f"Entradas recibidas: {entradas}")
print(f"Pesos aplicados:    {pesos}")
print(f"Sesgo (bias):       {sesgo}\n")
print(f"1. Suma Ponderada (z):       {z:.4f} (Señal cruda antes de activarse)")
print(f"2. Salida (Activación ReLU): {activacion:.4f} (Señal final que emitirá la neurona a la siguiente capa)")