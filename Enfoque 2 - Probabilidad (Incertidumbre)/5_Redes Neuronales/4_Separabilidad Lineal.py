# La separabilidad lineal determina si un modelo de una sola capa (como el Perceptrón) 
# puede o no resolver un problema. Si las clases no pueden dividirse con una línea recta 
# (o hiperplano en más dimensiones), se requiere una Red Neuronal Multicapa (Deep Learning).

def intentar_separacion_lineal(datos: list[tuple[list[int], int]], max_epocas: int = 20) -> tuple[bool, list[float]]:
    """
    Intenta entrenar un perceptrón simple. 
    Si logra 0 errores, el problema ES linealmente separable.
    Si agota las épocas sin lograr 0 errores, empíricamente asumimos que NO lo es.
    """
    pesos = [0.0, 0.0, 0.0]  # pesos[0] = sesgo (bias), pesos[1] = w1, pesos[2] = w2
    tasa_aprendizaje = 0.1

    for epoca in range(max_epocas):
        errores_epoca = 0
        for x, objetivo in datos:
            # z = bias + w1*x1 + w2*x2
            z = pesos[0] + pesos[1] * x[0] + pesos[2] * x[1]
            
            # Función escalón (paso unitario)
            prediccion = 1 if z > 0 else 0
            
            error = objetivo - prediccion
            if error != 0:
                # Actualización de pesos usando la regla del Perceptrón
                pesos[0] += tasa_aprendizaje * error        # Sesgo
                pesos[1] += tasa_aprendizaje * error * x[0] # W1
                pesos[2] += tasa_aprendizaje * error * x[1] # W2
                errores_epoca += 1
        
        # Si en una época completa no hubo errores, encontramos la línea recta (hiperplano)
        if errores_epoca == 0:
            return True, pesos
            
    # Si terminamos las épocas y sigue habiendo errores, la línea recta no sirve
    return False, pesos

def verificar_separabilidad():
    """
    Un problema es linealmente separable si existe un hiperplano (línea) 
    que puede dividir perfectamente las clases.
    """
    print("--- Demostración de Separabilidad Lineal ---\n")

    # 1. Conjunto de datos AND
    datos_and = [
        ([0, 0], 0),
        ([0, 1], 0),
        ([1, 0], 0),
        ([1, 1], 1)
    ]
    
    print("Evaluando compuerta AND:")
    separable_and, pesos_and = intentar_separacion_lineal(datos_and)
    if separable_and:
        print("  [ÉXITO] AND es linealmente separable.")
        print(f"  El perceptrón encontró una línea divisoria: Bias={pesos_and[0]:.1f}, W1={pesos_and[1]:.1f}, W2={pesos_and[2]:.1f}\n")

    # 2. Conjunto de datos XOR (Or exclusivo)
    datos_xor = [
        ([0, 0], 0),
        ([0, 1], 1),
        ([1, 0], 1),
        ([1, 1], 0)
    ]
    
    print("Evaluando compuerta XOR:")
    separable_xor, pesos_xor = intentar_separacion_lineal(datos_xor)
    if not separable_xor:
        print("  [FALLO] XOR NO es linealmente separable.")
        print("  El perceptrón agotó los intentos de aprendizaje sin llegar a 0 errores.")
        print("  Geométricamente, es imposible trazar una SOLA línea recta que separe los 1s de los 0s en un XOR.")

if __name__ == "__main__":
    verificar_separabilidad()