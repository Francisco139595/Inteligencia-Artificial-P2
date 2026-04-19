def ac3(dominios, arcos):
    """
    Algoritmo AC-3 para asegurar la consistencia de arco. 
    Reduce los dominios antes de iniciar la búsqueda.
    """
    queue = list(arcos)
    while queue:
        (xi, xj) = queue.pop(0)
        if revisar(dominios, xi, xj):
            if not dominios[xi]:
                return False # Sin solución
            for xk in arcos: # Re-agregar arcos afectados
                if xk[1] == xi and xk[0] != xj:
                    queue.append(xk)
    return True

def revisar(dominios, xi, xj):
    """Elimina valores de xi que no tienen correspondencia en xj."""
    revisado = False
    for x in dominios[xi][:]:
        # Si no hay ningún valor en xj que cumpla la restricción (xi != xj)
        if not any(y != x for y in dominios[xj]):
            dominios[xi].remove(x)
            revisado = True
    return revisado

doms_ac3 = {"A": [1], "B": [1, 2, 3]}
arcos_ac3 = [("A", "B"), ("B", "A")]
ac3(doms_ac3, arcos_ac3)
print(f"Dominios tras AC-3: {doms_ac3}")