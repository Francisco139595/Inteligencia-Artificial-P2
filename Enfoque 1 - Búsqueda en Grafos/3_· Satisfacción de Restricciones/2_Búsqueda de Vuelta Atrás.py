def backtracking_search(asignacion, variables, dominios, restricciones):
    """
    Algoritmo de búsqueda en profundidad que intenta asignar valores uno a uno,
    retrocediendo cuando encuentra una inconsistencia.
    """
    # Si todos los elementos están asignados, terminamos
    if len(asignacion) == len(variables):
        return asignacion

    # Seleccionar una variable no asignada
    var = [v for v in variables if v not in asignacion][0]

    for valor in dominios[var]:
        # Verificamos consistencia local
        consistente = True
        for vecino in restricciones.get(var, []):
            if vecino in asignacion and asignacion[vecino] == valor:
                consistente = False
                break
        
        if consistente:
            asignacion[var] = valor
            resultado = backtracking_search(asignacion, variables, dominios, restricciones)
            if resultado is not None:
                return resultado
            # Si no funcionó, eliminamos la asignación (vuelta atrás)
            del asignacion[var]

    return None

# Prueba con coloreado de 3 nodos
vars_b = ["A", "B", "C"]
doms_b = {v: ["Rojo", "Azul"] for v in vars_b}
rest_b = {"A": ["B"], "B": ["A", "C"], "C": ["B"]}
print(f"Solución Backtracking: {backtracking_search({}, vars_b, doms_b, rest_b)}")