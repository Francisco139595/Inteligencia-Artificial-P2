def calcular_priori(conteo_eventos, total_muestras):
    """
    La probabilidad a priori P(H) es el grado de creencia en una 
    hipótesis antes de observar cualquier evidencia.
    """
    # Ejemplo: En un conjunto de 100 correos, 20 son SPAM.
    # P(SPAM) = 20/100
    if total_muestras == 0: return 0
    return conteo_eventos / total_muestras

# Ejemplo: Probabilidad de que un paciente tenga gripe sin ver síntomas
print(f"P(Gripe) a priori: {calcular_priori(5, 1000)}")