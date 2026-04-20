def dbn_filtrado(prior, sensor_model, transition_model, evidencia):
    """
    Realiza el filtrado (estimación del estado actual dada la evidencia).
    Estructura simplificada de una DBN: P(X_t | e_1:t)
    """
    # Predicción: P(X_t | e_1:t-1)
    prediccion = sum(prior[s] * transition_model[s] for s in prior)
    
    # Actualización: P(X_t | e_1:t)
    post = sensor_model[evidencia] * prediccion
    # Normalización simple para 2 estados (Binario: Verdadero/Falso)
        # Nota: Asume P(e | ~X) = 1 - P(e | X). En problemas reales suele darse como dato aparte.
    return post / (post + (1 - sensor_model[evidencia]) * (1 - prediccion))

# Ejemplo: Predecir si llueve hoy basado en si ayer llovió y si hay paraguas
# Convertimos los parámetros a diccionarios para que iteren correctamente en la función:
prior_ayer = {'Lluvia': 0.5, 'No_Lluvia': 0.5}
modelo_transicion = {'Lluvia': 0.7, 'No_Lluvia': 0.3} # P(Lluvia hoy | estado de ayer)
modelo_sensor = {'ver_paraguas': 0.9}                 # P(ver_paraguas | Lluvia hoy)

print(f"Probabilidad de lluvia actual: {dbn_filtrado(prior_ayer, modelo_sensor, modelo_transicion, 'ver_paraguas'):.2f}")