def policy_iteration(estados, acciones, recompensas, transiciones, gamma=0.9, epsilon=0.01):
    """
    Alterna entre evaluar una política y mejorarla hasta que no haya cambios.
    """
    politica = {s: acciones[0] for s in estados if s != "Meta"}
    V = {s: 0 for s in estados}

    while True:
        # 1. Evaluación de política
        while True:
            delta = 0
            V_nueva = V.copy()
            for s in politica:
                a = politica[s]
                V_nueva[s] = recompensas[s] + gamma * sum(prob * V[sig] for sig, prob in transiciones[s][a])
                delta = max(delta, abs(V_nueva[s] - V[s]))
            V = V_nueva
            if delta < epsilon:
                break
        
        # 2. Mejora de política
        estable = True
        for s in politica:
            vieja_accion = politica[s]
            mejor_a = None
            mejor_val = -float('inf')
            for a in acciones:
                val = recompensas[s] + gamma * sum(prob * V[sig] for sig, prob in transiciones[s][a])
                if val > mejor_val:
                    mejor_val, mejor_a = val, a
            politica[s] = mejor_a
            if vieja_accion != mejor_a: estable = False
        
        if estable: break
    return politica

# Datos del ejemplo (necesarios para que el script funcione de forma independiente)
estados = ["A", "B", "Meta"]
acciones = ["Mover"]
recompensas = {"A": -1, "B": -1, "Meta": 10}
transiciones = {"A": {"Mover": [("B", 1.0)]}, "B": {"Mover": [("Meta", 1.0)]}}

print("Política óptima hallada:", policy_iteration(estados, acciones, recompensas, transiciones))