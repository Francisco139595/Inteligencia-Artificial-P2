import random

def min_conflicts(variables, dominios, restricciones, max_pasos=100):
    """
    Algoritmo de búsqueda local que selecciona una variable en conflicto 
    y le asigna el valor que minimice el número de conflictos totales.
    """
    # Asignación inicial aleatoria
    asignacion = {v: random.choice(dominios[v]) for v in variables}

    for i in range(max_pasos):
        # Identificar variables que violan restricciones
        en_conflicto = []
        for v in variables:
            for vecino in restricciones.get(v, []):
                if asignacion[v] == asignacion[vecino]:
                    en_conflicto.append(v)
                    break
        
        if not en_conflicto: return asignacion # Solución hallada

        var = random.choice(en_conflicto)
        
        # Elegir valor que minimice conflictos
        def contar_conflictos(valor):
            c = 0
            for vecino in restricciones.get(var, []):
                if valor == asignacion[vecino]: c += 1
            return c

        mejor_valor = min(dominios[var], key=contar_conflictos)
        asignacion[var] = mejor_valor

    return None # No se halló en max_pasos

vars_mc = ["A", "B", "C", "D"]
doms_mc = {v: [1, 2] for v in vars_mc}
rest_mc = {"A": ["B"], "B": ["A", "C"], "C": ["B", "D"], "D": ["C"]}
print(f"Solución Min-Conflicts: {min_conflicts(vars_mc, doms_mc, rest_mc)}")