class AgenteExplorador:
    """
    Implementación de Learning Real-Time A*.
    El agente no conoce el entorno y aprende los costos mientras se mueve.
    """
    def __init__(self):
        self.H_aprendida = {} # Tabla de valores heurísticos actualizados

    def obtener_h(self, estado):
        # Si no conocemos el estado, devolvemos una heurística inicial (distancia al 0)
        return self.H_aprendida.get(estado, abs(estado))

    def mover(self, actual, vecinos):
        # Si ya llegamos a la meta (estado 0)
        if actual == 0: return 0
        
        # Calculamos f(s') para cada vecino: costo de paso (1) + H aprendida del vecino
        costos = []
        for v in vecinos:
            f = 1 + self.obtener_h(v)
            costos.append((f, v))
        
        # Elegimos el mejor vecino
        mejor_f, mejor_vecino = min(costos)
        
        # ACTUALIZACIÓN: El agente aprende que el costo para llegar a la meta
        # desde 'actual' es al menos mejor_f.
        self.H_aprendida[actual] = mejor_f
        
        return mejor_vecino

# Simulación de un agente en una línea numérica tratando de llegar al 0
agente = AgenteExplorador()
pos = 4
print(f"Inicio en posición: {pos}")
for paso in range(10):
    pos = agente.mover(pos, [pos-1, pos+1])
    print(f"Paso {paso+1}: Movido a {pos}")
    if pos == 0: break