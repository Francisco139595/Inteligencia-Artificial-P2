# Backpropagation: Algoritmo para entrenar redes neuronales profundas.
# Propaga el error desde la salida hacia atrás para ajustar los pesos.

def retropropagacion_paso_simple(valor_real, valor_predicho, entrada):
    """
    Muestra la lógica del gradiente descendente para ajustar un peso.
    """
    # 1. Calcular el error (Gradiente de la función de coste)
    error = valor_predicho - valor_real
    
    # 2. Calcular la derivada de la activación (ej. Sigmoide)
    derivada_activacion = valor_predicho * (1 - valor_predicho)
    
    # 3. Delta para el peso: Error * Derivada * Entrada
    delta_w = error * derivada_activacion * entrada
    
    print(f"Ajuste sugerido para el peso: {-delta_w:.4f}")
    return delta_w

retropropagacion_paso_simple(1.7, 0.8, 0.5)