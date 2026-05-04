import random

def filtrado_particulas(n_particulas: int = 100, observacion: float = 5.0) -> float:
    """
    Utilizado en Redes Bayesianas Dinámicas cuando el sistema no es lineal.
    Usa una población de 'partículas' para representar la distribución de probabilidad.
    """
    if n_particulas <= 0:
        raise ValueError("El número de partículas debe ser mayor a cero.")

    # 1. Inicialización: Partículas en posiciones aleatorias
    particulas = [random.uniform(0, 10) for _ in range(n_particulas)]
    
    # 2. Predicción: Mover partículas según un modelo físico + ruido
    particulas = [p + 1 + random.normalvariate(0, 0.5) for p in particulas]
    
    # 3. Pesado: Dar más peso a partículas cerca de la observación
    pesos = [1.0 / (abs(p - observacion) + 0.1) for p in particulas]
    
    # 4. Resampleo: Seleccionar nuevas partículas basadas en los pesos
    total_w = sum(pesos)
    prob_w = [w/total_w for w in pesos]
    particulas = random.choices(particulas, weights=prob_w, k=n_particulas)
    
    estimacion_final = sum(particulas) / n_particulas
    print("--- Filtrado de Partículas ---")
    print(f"Observación del sensor: {observacion}")
    print(f"Centro de masa estimado: {estimacion_final:.2f}")
    return estimacion_final

resultado = filtrado_particulas(n_particulas=1000, observacion=6.5)
