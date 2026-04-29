import copy

def forward_checking(asignacion, dominios, restricciones):
    """
    Mejora el backtracking eliminando valores de los dominios de las variables
    vecinas que ya no son posibles tras una asignación.
    """
    if len(asignacion) == len(dominios):
        return asignacion

    var = [v for v in dominios if v not in asignacion][0]
    
    for valor in dominios[var]:
        # Creamos una copia temporal de los dominios para no corromper la búsqueda
        dominios_copia = copy.deepcopy(dominios)
        asignacion[var] = valor
        
        # Poda de dominios vecinos
        posible = True
        for vecino in restricciones.get(var, []):
            if vecino not in asignacion:
                if valor in dominios_copia[vecino]:
                    dominios_copia[vecino].remove(valor)
                # Si un vecino se queda sin valores, esta rama es inválida
                if not dominios_copia[vecino]:
                    posible = False
                    break
        
        if posible:
            res = forward_checking(asignacion, dominios_copia, restricciones)
            if res: return res
        
        del asignacion[var]
    return None

doms_fc = {"A": [1, 2], "B": [1, 2], "C": [1, 2]}
rest_fc = {"A": ["B"], "B": ["A", "C"], "C": ["B"]}
print(f"Solución Forward Checking: {forward_checking({}, doms_fc, rest_fc)}")