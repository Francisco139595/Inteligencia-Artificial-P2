# El aprendizaje pasivo se basa en observar ejecuciones de una política fija.
# Se busca estimar la utilidad U(s) de cada estado.

def aprendizaje_pasivo_directo(episodios, gamma=0.9):
    """
    Estimación de utilidad mediante la media de recompensas futuras.
    """
    utilidades = {}
    conteos = {}

    for episodio in episodios:
        # Un episodio es una lista de (estado, recompensa)
        g = 0 # Retorno acumulado
        # Recorremos el episodio hacia atrás para calcular el retorno
        for estado, recompensa in reversed(episodio):
            g = recompensa + gamma * g
            
            # Actualizamos la media acumulada para el estado
            if estado not in utilidades:
                utilidades[estado] = 0.0
                conteos[estado] = 0
            
            conteos[estado] += 1
            # Fórmula de la media móvil: anterior + (nuevo - anterior) / n
            utilidades[estado] += (g - utilidades[estado]) / conteos[estado]
            
    return utilidades

# Simulación: 2 episodios en un mundo de 3 estados
# El agente siempre sigue la misma ruta: S1 -> S2 -> Meta
historial = [
    [("S1", -1), ("S2", -1), ("Meta", 10)],
    [("S1", -1), ("S2", -1), ("Meta", 10)]
]
print(f"Utilidades estimadas (Pasivo): {aprendizaje_pasivo_directo(historial)}")