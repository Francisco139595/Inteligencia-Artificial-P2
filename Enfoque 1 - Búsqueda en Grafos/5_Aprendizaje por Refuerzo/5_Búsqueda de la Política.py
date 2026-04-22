# La búsqueda de política parametriza la política pi(s, a).
# Aquí usamos una versión simple basada en pesos (Hill Climbing en políticas).

import random

def evaluar_politica(pesos):
    """Simula qué tan buena es una política basada en un vector de pesos."""
    # En un caso real, esto ejecutaría al agente en el entorno.
    # Aquí simulamos que el 'score' mejora si los pesos se acercan a un valor ideal.
    objetivo = [0.5, 0.5]
    error = sum((p - o)**2 for p, o in zip(pesos, objetivo))
    return -error # Retornamos negativo porque queremos maximizar (minimizar error)

def buscar_mejor_politica(iteraciones=100):
    # Iniciamos con pesos aleatorios para nuestra política
    mejor_pesos = [random.random(), random.random()]
    mejor_score = evaluar_politica(mejor_pesos)
    pesos_iniciales = mejor_pesos.copy()

    for _ in range(iteraciones):
        # Aplicamos una pequeña variación (mutación) a la política
        nuevos_pesos = [p + random.uniform(-0.1, 0.1) for p in mejor_pesos]
        nuevo_score = evaluar_politica(nuevos_pesos)

        # Si la nueva política es mejor, la guardamos
        if nuevo_score > mejor_score:
            mejor_pesos, mejor_score = nuevos_pesos, nuevo_score

    return pesos_iniciales, mejor_pesos, mejor_score

pesos_ini, pesos_fin, score_fin = buscar_mejor_politica(1000)
print("--- Optimización de Política (Hill Climbing) ---")
print(f"Objetivo ideal: [0.5, 0.5]")
print(f"Pesos iniciales aleatorios: [{pesos_ini[0]:.4f}, {pesos_ini[1]:.4f}]")
print(f"Mejor política (pesos) hallada: [{pesos_fin[0]:.4f}, {pesos_fin[1]:.4f}]")
print(f"Score final (más cerca de 0 es mejor): {score_fin:.6f}")