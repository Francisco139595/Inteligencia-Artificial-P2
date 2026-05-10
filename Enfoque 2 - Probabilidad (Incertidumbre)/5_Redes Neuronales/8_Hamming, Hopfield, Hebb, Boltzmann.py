# Este archivo resume las reglas de aprendizaje históricas.

def regla_hebbiana(w, x, y):
    """
    Regla de Hebb: 'Neuronas que se activan juntas, se conectan juntas'.
    El peso aumenta si la entrada y la salida son positivas simultáneamente.
    """
    delta_w = x * y
    return w + delta_w

def red_hopfield_energia(estado, pesos):
    """
    Red de Hopfield: Memoria asociativa. La red evoluciona hacia 
    un estado de mínima energía.
    """
    energia = 0
    for i in range(len(estado)):
        for j in range(len(estado)):
            energia += -0.5 * pesos[i][j] * estado[i] * estado[j]
    return energia

print(f"Nueva conexión Hebbiana: {regla_hebbiana(0.5, 1, 1)}")