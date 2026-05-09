def aprendizaje_bayesiano_map(priori, verosimilitud):
    """
    El aprendizaje Bayesiano estima la probabilidad de una hipótesis dada la evidencia.
    El método MAP (Maximum A Posteriori) elige la hipótesis más probable.
    """
    # Posterior proportional to Priori * Likelihood
    posteriores = {h: priori[h] * verosimilitud[h] for h in priori}
    
    # Seleccionamos la hipótesis que maximiza el posterior
    mejor_h = max(posteriores, key=posteriores.get)
    return mejor_h, posteriores

# Ejemplo: Diagnóstico médico con priori y verosimilitud
priori = {'Gripe': 0.7, 'Sano': 0.9}
verosimilitud = {'Gripe': 0.8, 'Sano': 0.05} # P(Fiebre | H)
print(f"Hipótesis MAP: {aprendizaje_bayesiano_map(priori, verosimilitud)}")