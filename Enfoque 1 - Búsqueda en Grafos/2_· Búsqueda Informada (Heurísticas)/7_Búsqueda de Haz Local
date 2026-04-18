import random

def beam_search(k=3, iteraciones=100):
    """
    Mantiene 'k' estados paralelos. En cada paso, genera todos los sucesores
    de los 'k' estados y selecciona los 'k' mejores de toda la lista.
    """
    def evaluar(x): return -(x**2) + 50
    
    # Inicializamos k puntos aleatorios
    estados = [random.uniform(-20, 20) for _ in range(k)]
    
    for _ in range(iteraciones):
        sucesores = []
        for e in estados:
            # Generar variantes de cada estado
            sucesores.append(e + random.uniform(-0.5, 0.5))
            sucesores.append(e + random.uniform(-0.5, 0.5))
            
        # Seleccionamos los k mejores entre todos los sucesores generados
        estados = sorted(sucesores, key=evaluar, reverse=True)[:k]
        
    return estados[0]

print(f"Mejor estado tras Beam Search: {beam_search():.4f}")