import math
import random

def temple_simulado():
    """
    Metaheurística que acepta soluciones peores al inicio (alta temperatura)
    para explorar el espacio y luego se vuelve más selectiva (baja temperatura).
    """
    actual = random.uniform(-10, 10)
    temp = 1000.0 # Temperatura inicial
    enfriamiento = 0.99 # Factor de reducción de temperatura
    
    def costo(x): return x**2 # Queremos minimizar esta función (mínimo en 0)

    for i in range(2000):
        vecino = actual + random.uniform(-1, 1)
        delta = costo(vecino) - costo(actual)
        
        # Si el vecino es mejor, lo aceptamos.
        # Si es peor, lo aceptamos con una probabilidad basada en la temperatura.
        if delta < 0 or random.random() < math.exp(-delta / temp):
            actual = vecino
            
        temp *= enfriamiento # El sistema se "congela" poco a poco
        
    return actual

print(f"Mínimo hallado por Temple Simulado: {temple_simulado():.4f}")