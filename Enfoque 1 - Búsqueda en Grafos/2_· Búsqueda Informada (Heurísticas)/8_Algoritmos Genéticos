import random

def genetic_algorithm(pob_size=10, gen_max=100):
    """
    Resuelve el problema de maximizar la cantidad de 1s en una cadena de bits.
    Incluye: Población, Selección, Cruce y Mutación.
    """
    # 1. Población inicial (listas de 0s y 1s)
    poblacion = [[random.randint(0, 1) for _ in range(8)] for _ in range(pob_size)]
    
    for g in range(gen_max):
        # Evaluación (Fitness)
        poblacion = sorted(poblacion, key=lambda ind: sum(ind), reverse=True)
        
        # Selección de los mejores (Elite)
        padres = poblacion[:pob_size//2]
        
        # 2. Cruce (Crossover)
        hijos = []
        for _ in range(pob_size // 2):
            p1, p2 = random.sample(padres, 2)
            punto = random.randint(1, 6)
            hijos.append(p1[:punto] + p2[punto:])
            
        # 3. Mutación (Probabilidad del 10%)
        for h in hijos:
            if random.random() < 0.1:
                idx = random.randint(0, 7)
                h[idx] = 1 - h[idx]
        
        poblacion = padres + hijos
        
    return poblacion[0]

print(f"Mejor individuo evolucionado: {genetic_algorithm()}")