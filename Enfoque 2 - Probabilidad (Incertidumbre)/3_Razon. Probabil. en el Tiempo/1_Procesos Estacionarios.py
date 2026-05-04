import random

def simular_proceso_estacionario(pasos=100):
    """
    Un proceso es estacionario si sus propiedades estadísticas (media, varianza)
    no cambian con el tiempo. Aquí simulamos un ruido blanco estacionario.
    """
    # La media teórica es 0 y la varianza es constante
    proceso = [random.normalvariate(0, 1) for _ in range(pasos)]
    
    media_estimada = sum(proceso) / pasos
    print(f"Media del proceso (estacionaria cerca de 0): {media_estimada:.4f}")
    return proceso

simular_proceso_estacionario()