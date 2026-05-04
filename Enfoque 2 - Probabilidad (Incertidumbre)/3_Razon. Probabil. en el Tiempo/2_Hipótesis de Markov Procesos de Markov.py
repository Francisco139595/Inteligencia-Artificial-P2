import random

def cadena_markov_simple(estado_inicial: str, pasos: int = 10) -> list:
    """
    La Hipótesis de Markov establece que el futuro depende SOLO del presente,
    no del pasado. P(Xt | X_0:t-1) = P(Xt | Xt-1).
    """
    # Matriz de transición: {EstadoActual: {Siguiente: Probabilidad}}
    transiciones = {
        "Sol": {"Sol": 0.8, "Lluvia": 0.2},
        "Lluvia": {"Sol": 0.4, "Lluvia": 0.6}
    }
    
    historial = [estado_inicial]
    actual = estado_inicial
    
    for _ in range(pasos):
        r = random.random() # Muestreo real para permitir variaciones (Sol/Lluvia)
        prob_sol = transiciones[actual]["Sol"]
        # Decidir siguiente estado basado en la probabilidad
        actual = "Sol" if r < prob_sol else "Lluvia"
        historial.append(actual)
        
    return historial

print(f"Cadena de Markov: {cadena_markov_simple('Sol')}")