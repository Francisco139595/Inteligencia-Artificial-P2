def distribucion_discreta(resultados):
    """
    Representa una distribución de probabilidad completa para 
    una variable aleatoria discreta (ej. un dado).
    """
    total = sum(resultados.values())
    distribucion = {k: v / total for k, v in resultados.items()}
    
    # Verificación de axioma: suma debe ser 1
    assert round(sum(distribucion.values()), 5) == 1.0
    return distribucion

# Lanzamientos de un dado cargado
lanzamientos = {1: 10, 2: 10, 3: 10, 4: 10, 5: 10, 6: 50}
print(f"Distribución del dado: {distribucion_discreta(lanzamientos)}")