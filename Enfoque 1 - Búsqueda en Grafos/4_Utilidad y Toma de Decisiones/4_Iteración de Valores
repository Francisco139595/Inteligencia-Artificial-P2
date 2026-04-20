def value_iteration(estados, acciones, recompensas, transiciones, gamma=0.9, epsilon=0.01):
    """
    Algoritmo para hallar la política óptima en un MDP actualizando
    los valores de cada estado hasta la convergencia.
    """
    V = {s: 0 for s in estados}
    while True:
        delta = 0
        V_nueva = V.copy()
        for s in estados:
            if s == "Meta": continue
            # Ecuación de Bellman: V(s) = max [ R(s,a) + gamma * sum( P(s'|s,a) * V(s') ) ]
            valores_acciones = []
            for a in acciones:
                val = recompensas[s] + gamma * sum(prob * V[sig] for sig, prob in transiciones[s][a])
                valores_acciones.append(val)
            V_nueva[s] = max(valores_acciones)
            delta = max(delta, abs(V_nueva[s] - V[s]))
        V = V_nueva
        if delta < epsilon: break
    return V

# Datos mínimos para prueba
estados = ["A", "B", "Meta"]
acciones = ["Mover"]
recompensas = {"A": -1, "B": -1, "Meta": 10}
transiciones = {"A": {"Mover": [("B", 1.0)]}, "B": {"Mover": [("Meta", 1.0)]}}

print("Valores de estado óptimos:", value_iteration(estados, acciones, recompensas, transiciones))