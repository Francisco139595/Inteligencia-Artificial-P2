def probabilidad_condicionada(p_interseccion, p_evidencia):
    """
    Calcula P(A|B) = P(A ∩ B) / P(B).
    Es la probabilidad de que ocurra A dado que ya ocurrió B.
    """
    if p_evidencia == 0: return 0
    return p_interseccion / p_evidencia

def normalizar(distribucion_no_normalizada):
    """
    La normalización asegura que la suma de las probabilidades 
    de una distribución sea exactamente 1.0 (Alpha).
    """
    suma = sum(distribucion_no_normalizada.values())
    return {k: v / suma for k, v in distribucion_no_normalizada.items()}

# Datos: P(Lluvia y Nublado) = 0.2, P(Nublado) = 0.3
p_lluvia_dado_nublado = probabilidad_condicionada(0.2, 0.3)
print(f"P(Lluvia|Nublado): {p_lluvia_dado_nublado:.2f}")

# Ejemplo Normalización
dist_sucia = {"Gripe": 0.005, "Sano": 0.1}
print(f"Distribución normalizada: {normalizar(dist_sucia)}")