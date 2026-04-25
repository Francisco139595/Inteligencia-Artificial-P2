def regla_de_bayes(p_priori_h, p_evidencia_dado_h, p_evidencia_total):
    """
    Implementa el Teorema de Bayes:
    P(H|E) = ( P(E|H) * P(H) ) / P(E)
    
    Permite actualizar nuestra creencia en una hipótesis (H) 
    después de observar nueva evidencia (E).
    """
    # P(H|E) = Posterior
    # P(E|H) = Verosimilitud (Likelihood)
    # P(H) = Priori
    # P(E) = Evidencia total (Marginalización)
    
    posterior = (p_evidencia_dado_h * p_priori_h) / p_evidencia_total
    return posterior

# Caso de estudio: Prueba médica
# P(Cáncer) = 0.01 (Priori)
# P(Positivo | Cáncer) = 0.9 (Sensibilidad)
# P(Positivo | No Cáncer) = 0.05 (Falso positivo)
p_cancer = 0.09
p_pos_dado_cancer = 0.7
p_pos_dado_no_cancer = 0.08

# P(E) = P(E|H)P(H) + P(E|¬H)P(¬H)
p_positivo_total = (p_pos_dado_cancer * p_cancer) + (p_pos_dado_no_cancer * (1 - p_cancer))

resultado = regla_de_bayes(p_cancer, p_pos_dado_cancer, p_positivo_total)
print(f"Probabilidad real de tener la enfermedad tras test positivo: {resultado:.4f}")