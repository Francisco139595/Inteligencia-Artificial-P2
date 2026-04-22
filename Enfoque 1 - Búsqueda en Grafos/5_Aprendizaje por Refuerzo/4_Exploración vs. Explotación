import random

def dilema_bandido(epsilon, iteraciones=1000):
    """
    Simula una máquina con 3 palancas. Cada una tiene una probabilidad oculta de ganar.
    - Explotación: Jalar la palanca que más ha pagado.
    - Exploración: Probar palancas nuevas para ver si son mejores.
    """
    probabilidades_reales = [0.1, 0.5, 0.8] # La palanca 2 es la mejor
    recompensas_acumuladas = [0, 0, 0]
    intentos = [0, 0, 0]
    
    recompensa_total = 0

    for _ in range(iteraciones):
        # ¿Exploramos o Explotamos?
        if random.random() < epsilon:
            # Exploración: elegir al azar
            seleccion = random.randint(0, 2)
        else:
            # Explotación: elegir la que tiene mejor promedio actual
            promedios = [recompensas_acumuladas[i]/intentos[i] if intentos[i]>0 else 0 for i in range(3)]
            seleccion = promedios.index(max(promedios))
        
        # Obtener recompensa real
        ganó = 1 if random.random() < probabilidades_reales[seleccion] else 0
        
        # Actualizar memoria
        intentos[seleccion] += 1
        recompensas_acumuladas[seleccion] += ganó
        recompensa_total += ganó

    return recompensa_total

print(f"Recompensa con Epsilon=0.1 (Balance): {dilema_bandido(0.1)}")
print(f"Recompensa con Epsilon=0.0 (Solo explotación): {dilema_bandido(0.0)}")  