import random

def simulacion_incertidumbre(n_intentos=1000):
    """
    Representa la incertidumbre mediante la frecuencia de eventos.
    En IA, la incertidumbre surge porque no podemos predecir con 
    total certeza el resultado de un evento estocástico.
    """
    exitos = 0
    # Simulamos un evento con un 70% de probabilidad de éxito
    prob_real = 0.73
    
    for _ in range(n_intentos):
        if random.random() < prob_real:
            exitos += 1
            
    # La probabilidad estimada se acerca a la real conforme aumenta N
    frecuencia_estimada = exitos / n_intentos
    return frecuencia_estimada

print(f"Probabilidad estimada tras simulación: {simulacion_incertidumbre()}")